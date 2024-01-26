from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model


class LoginForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password')

    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', }),
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', }),
    )





class UserRegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(
        label='Username',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', }),
    )
    email = forms.CharField(
        label='Email',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email', }),
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password', }),
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password', }),
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already registered.')
        return email


class UserProfileForm(UserChangeForm):
    profile_picture = forms.ImageField(
        widget=forms.FileInput(attrs={'class': 'custom-file-label', }), required=False
    )

    class Meta:
        model = get_user_model()
        fields = ('profile_picture', 'email', 'first_name', 'last_name', 'country', 'phone')
        labels = {
            'email': 'Email',
            'first_name': 'First name',
            'last_name': 'Last name',
            'country': 'Country',
            'phone': 'Phone',
        }
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', }),
            'first_name': forms.TextInput(attrs={'class': 'form-control', }),
            'last_name': forms.TextInput(attrs={'class': 'form-control', }),
            'country': forms.TextInput(attrs={'class': 'form-control', }),
            'phone': forms.TextInput(attrs={'class': 'form-control', }),
        }



