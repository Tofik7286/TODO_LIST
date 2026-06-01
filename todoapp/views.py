from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, LoginForm, ProfileForm
from .models import Task


@login_required
def todo(request):
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'todoapp/todo.html', {'tasks': tasks})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'todoapp/register.html', {'form': form})


def login(request):
    if request.user.is_authenticated:
        return redirect('todo')

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('todo')
            form.add_error(None, 'Invalid email or password.')
    else:
        form = LoginForm()

    return render(request, 'todoapp/login.html', {'form': form})


@login_required
def logout_view(request):
    auth_logout(request)
    return redirect('login')


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, user=request.user)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name'].strip()
            if name:
                user.first_name = name
            new_password = form.cleaned_data.get('new_password')
            if new_password:
                user.set_password(new_password)
                update_session_auth_hash(request, user)
            user.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('profile')
    else:
        form = ProfileForm(user=request.user, initial={'name': request.user.first_name})
    return render(request, 'todoapp/profile.html', {'form': form})
