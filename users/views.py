from django.contrib.auth.models import User, Permission
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponseForbidden
from .permissions_dict import PERMISSION_TRANSLATIONS
from django.urls import reverse_lazy
from . import forms


class UserListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'users'
    permission_required = 'auth.view_user'

class UserDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = User
    template_name = 'user_detail.html'
    permission_required = 'auth.view_user'

class UserCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = User
    template_name = 'user_create.html'
    form_class = forms.UserForm
    success_url = reverse_lazy('users_list')
    permission_required = 'auth.add_user'

    def form_valid(self, form):
        user = form.save(commit=False)
        password = form.cleaned_data['password']
        user.set_password(password) # Aplicando hash
        user.save()

        # O signal já criou o Profile, agora só atualizamos (Se você não tiver o signal, precisa fazer Profile.objects.create(...))
        profile = user.profile
        profile.role = form.cleaned_data['role']
        profile.is_checked = form.cleaned_data['is_checked']
        profile.save()

        return super().form_valid(form)

@login_required
@permission_required('auth.change_user', raise_exception=True)
def toggle_user_status(request, user_id):
    user = get_object_or_404(User, id=user_id)
    
    # Alterna o status
    user.profile.is_checked = not user.profile.is_checked
    user.is_active = user.profile.is_checked  # Garante que login siga o status
    user.profile.save()
    user.save()
    
    return redirect(reverse('users_list'))

@login_required
@permission_required('auth.change_user', raise_exception=True)
def manage_user_permissions(request, user_id):
    if not request.user.is_superuser:
        return HttpResponseForbidden("Acesso negado")
    
    user = get_object_or_404(User, pk=user_id)
    all_permissions = Permission.objects.all()

    if request.method == 'POST':
        # Atualizar permissões
        selected_permissions = request.POST.getlist('permissions')
        user.user_permissions.set(selected_permissions)

        # Atualizar role
        new_role = request.POST.get('role')
        if new_role and hasattr(user, 'profile'):
            user.profile.role = new_role
            user.profile.save()

        return redirect(reverse('users_list'))

    context = {
        'user_obj': user,
        'all_permissions': all_permissions,
        'user_permissions': user.user_permissions.all(),
        'translations': PERMISSION_TRANSLATIONS,
    }
    return render(request, 'manage_user_permissions.html', context)