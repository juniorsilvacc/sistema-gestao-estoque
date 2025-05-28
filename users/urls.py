from django.urls import path
from .views import UserListView, toggle_user_status


urlpatterns = [
    path('users/list/', UserListView.as_view(), name='users_list'),
    path('toggle-status/<int:user_id>/', toggle_user_status, name='toggle_user_status'),
]