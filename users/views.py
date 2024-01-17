from django.shortcuts import render


def login(request):
    return render(request, 'profile/login.html')


def register(request):
    return render(request, 'profile/registration.html')


def profile(request):
    return render(request, 'profile/profile.html')


def password_change_done(request):
    return render(request, 'profile/password_change_done.html')


def password_change_form(request):
    return render(request, 'profile/password_change_form.html')


def password_reset_complete(request):
    return render(request, 'profile/password_reset_complete.html')


def password_reset_confirm(request):
    return render(request, 'profile/password_reset_confirm.html')


def password_reset_done(request):
    return render(request, 'profile/password_reset_done.html')


def password_reset_email(request):
    return render(request, 'profile/password_reset_email.html')


def password_reset_form(request):
    return render(request, 'profile/password_reset_form.html')