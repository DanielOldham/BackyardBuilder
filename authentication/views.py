from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .forms import SignupForm, LoginForm


# Create your views here.
def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'authentication/login.html', {'form': form})

    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard:dashboard')
        else:
            # User is not created
            # If there were errors, we render the form with these
            return render(request, 'authentication/login.html', {'form': form, 'page_title': "Login"})




