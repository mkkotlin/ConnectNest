from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from accounts.models import CustomUser


class CustomUserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
            "password1",
            "password2",
        )

        help_texts = {
            "username": None,
            "email": None,
            "password1": "",
            "password2": None,
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name in self.fields:
                self.fields[field_name].help_texts = None


class CustomLoginForm(AuthenticationForm):
    username = forms.CharField(
        label="Username",
    )
    password = forms.CharField(widget=forms.PasswordInput)
