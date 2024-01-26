from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.shortcuts import redirect, reverse
from .forms import LoginForm, UserRegisterForm, UserProfileForm
from django.views.generic import CreateView, UpdateView
from django.contrib.auth import get_user_model


class UserLoginView(LoginView):
    """Авторизація користувача"""
    form_class = LoginForm
    template_name = 'users/login.html'


class RegisterUserView(CreateView):
    """Реєстрація користувача"""
    form_class = UserRegisterForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('games:game_list')


class UserProfileView(UpdateView):
    model = get_user_model()
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        response = super().form_valid(form)
        print(form.errors)
        return redirect(reverse('users:profile'))


def password_change_done(request):
    return render(request, 'users/password_change_done.html')


def password_change_form(request):
    return render(request, 'users/password_change_form.html')


def password_reset_complete(request):
    return render(request, 'users/password_reset_complete.html')


def password_reset_confirm(request):
    return render(request, 'users/password_reset_confirm.html')


def password_reset_done(request):
    return render(request, 'users/password_reset_done.html')


def password_reset_email(request):
    return render(request, 'users/password_reset_email.html')


def password_reset_form(request):
    return render(request, 'users/password_reset_form.html')