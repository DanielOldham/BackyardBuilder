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

        self.fields['username'].widget.attrs.update({'placeholder': 'type your username'})
        self.fields['email'].widget.attrs.update({'placeholder': 'type your email'})
        self.fields['first_name'].widget.attrs.update({'placeholder': 'type your first name'})
        self.fields['last_name'].widget.attrs.update({'placeholder': 'type your last name'})
        self.fields['password1'].widget.attrs.update({'placeholder': 'type your password'})
        self.fields['password2'].widget.attrs.update({'placeholder': 'confirm your password'})

    class Meta:
        model = User

        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']


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
