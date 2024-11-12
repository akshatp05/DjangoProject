from django.urls import path
from .views import signup, login, get_all_users, get_user_by_email, update_user, delete_user

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('users/', get_all_users, name='get_all_users'),  # Get all users
    path('user/<str:email>/', get_user_by_email, name='get_user_by_email'),  # Get a single user by email
    path('update_user/<str:email>/', update_user, name='update_user'),  # Update user details
    path('delete_user/<str:email>/', delete_user, name='delete_user'),  # Delete user by email
]
