from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, LoginForm
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
