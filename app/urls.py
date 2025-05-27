from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from app.views import custom_500
from app.views import custom_404
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('/', auth_views.LogoutView.as_view(), name='logout'),

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