from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from . import models
from . import forms
from categories.models import Category
from brands.models import Brand
from app import metrics
import random
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.views.decorators.csrf import csrf_exempt

class ProductListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    permission_required = 'products.view_product'

    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.GET.get('title')
        serie_number = self.request.GET.get('serie_number')
        category = self.request.GET.get('category')
        brand = self.request.GET.get('brand')

        if title:
            queryset = queryset.filter(title__icontains=title)

        if serie_number:
            queryset = queryset.filter(serie_number__icontains=serie_number)
        
        if category:
            queryset = queryset.filter(category__id=category)
        
        if brand:
            queryset = queryset.filter(brand__id=brand)
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product_matrics'] = metrics.get_product_metrics()
        context['categories'] = Category.objects.all()
        context['brands'] = Brand.objects.all()

        return context

class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Product
    template_name = 'product_create.html'
    form_class = forms.ProductForm
    success_url = reverse_lazy('product_list')
    permission_required = 'products.add_product'

    def gerar_codigo(self):
        return str(random.randint(10**12, 10**13 - 1))

    def get_initial(self):
        initial = super().get_initial()
        initial['internal_code'] = self.gerar_codigo()
        return initial

class ProductDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Product
    template_name = 'product_detail.html'
    permission_required = 'products.view_product'

class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Product
    template_name = 'product_update.html'
    form_class = forms.ProductForm
    success_url = reverse_lazy('product_list')
    permission_required = 'products.change_product'

class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Product
    success_url = reverse_lazy('product_list')
    permission_required = 'products.delete_product'

@require_GET
@csrf_exempt
def gerar_codigo_view(request):
    codigo = str(random.randint(10**12, 10**13 - 1))
    return JsonResponse({'codigo': codigo})