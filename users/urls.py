from django.urls import path
from .views import toggle_user_status, manage_user_permissions
from . import views


urlpatterns = [
    path('users/list/', views.UserListView.as_view(), name='users_list'),
    path('toggle-status/<int:user_id>/', toggle_user_status, name='toggle_user_status'),
    path('users/<int:user_id>/permissions/', manage_user_permissions, name='manage_user_permissions'),
    path('users/<int:pk>/detail/', views.UserDetailView.as_view(), name='users_detail'),
    path('users/create/', views.UserCreateView.as_view(), name='users_create'),
]