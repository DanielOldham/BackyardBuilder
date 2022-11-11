from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class SignupForm(UserCreationForm):
    # Loops through fields and adds a bootstrap form-control class
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

    class Meta:
        model = User

        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

        labels = {
            "username": "Username",
            "email": "Email",
            "first_name": "First Name",
            "last_name": "Last Name",
            "password1": "Password",
            "password2": "Confirm Password",
        }


class LoginForm(AuthenticationForm):
    # Loops through fields and adds a bootstrap form-control class
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"

        self.fields['username'].widget.attrs.update({'placeholder': 'type your username'})
        self.fields['password'].widget.attrs.update({'placeholder': 'type your password'})

    class Meta:
        model = User

        fields = ['username', 'password']
