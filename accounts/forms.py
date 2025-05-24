from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from accounts.models import CustomUser


class CustomUserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2',)

class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username',)
    password = forms.CharField(widget=forms.PasswordInput)