from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

app_name = 'users'
urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('profile/', UserProfileView.as_view(), name='profile'),

    path('password_change_done/', password_change_done, name='password_change_done'),
    path('password_change_form/', password_change_form, name='password_change_form'),
    path('password_reset_complete/', password_reset_complete, name='password_reset_complete'),
    path('password_reset_confirm/', password_reset_confirm, name='password_reset_confirm'),
    path('password_reset_done/', password_reset_done, name='password_reset_done'),
    path('password_reset_email/', password_reset_email, name='password_reset_email'),
    path('password_reset_form/', password_reset_form, name='password_reset_form'),
]
