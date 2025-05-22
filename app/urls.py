from django.contrib import admin
from django.urls import path, include
from . import views
from app.views import custom_500
from app.views import custom_404
from .views import force_500

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.home, name='home'),
    
    path('', include('brands.urls')),
    path('', include('categories.urls')),
    path('', include('suppliers.urls')),
    path('', include('inflows.urls')),
    path('', include('outflows.urls')),
    path('', include('products.urls')),
]

handler500 = custom_500
handler404 = custom_404