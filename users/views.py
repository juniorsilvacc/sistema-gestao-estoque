from django.contrib.auth.models import User
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse


class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'user_list.html'
    context_object_name = 'users'

@login_required
def toggle_user_status(request, user_id):
    user = get_object_or_404(User, id=user_id)
    
    # Alterna o status
    user.profile.is_checked = not user.profile.is_checked
    user.is_active = user.profile.is_checked  # Garante que login siga o status
    user.profile.save()
    user.save()
    
    return redirect(reverse('users_list'))