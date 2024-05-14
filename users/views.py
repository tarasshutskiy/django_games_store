from django.shortcuts import render
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetView, PasswordResetConfirmView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect, reverse
from .forms import LoginForm, UserRegisterForm, UserProfileForm, UserPasswordChangeForm, UserPasswordResetForm, UserPasswordResetConfirmForm
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
    success_url = reverse_lazy('users:game_list')

    def form_valid(self, form):
        user = form.save()
        # Явно вказуємо бекенд аутентифікації (ваш EmailAuthBackend)
        user = authenticate(username=user.username,
                            password=form.cleaned_data['password1'],
                            backend='users.authentication.EmailAuthBackend')
        if user is not None:
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


class UserPasswordChangeView(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("users:password_change_done")
    template_name = "users/password_change_form.html"


class UserPasswordResetView(PasswordResetView):
    form_class = UserPasswordResetForm
    success_url = reverse_lazy("users:password_reset_done")
    email_template_name = "users/password_reset_email.html"
    template_name = "users/password_reset_form.html"


class UserPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = UserPasswordResetConfirmForm
    success_url = reverse_lazy("users:password_reset_complete")
    template_name = "users/password_reset_confirm.html"


