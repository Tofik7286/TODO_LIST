from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, LoginForm, ProfileForm, TaskForm
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
def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            messages.success(request, 'Task created successfully.')
            return redirect('todo')
    else:
        form = TaskForm()
    return render(request, 'todoapp/add_task.html', {'form': form})


@login_required
def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated successfully.')
            return redirect('todo')
    else:
        form = TaskForm(instance=task)
    return render(request, 'todoapp/edit_task.html', {'form': form, 'task': task})


@login_required
def bulk_delete_tasks(request):
    if request.method == 'POST':
        task_ids = request.POST.getlist('task_ids')
        if task_ids:
            deleted_count, _ = Task.objects.filter(pk__in=task_ids, user=request.user).delete()
            if deleted_count:
                noun = 'task' if deleted_count == 1 else 'tasks'
                messages.success(request, f'{deleted_count} {noun} deleted successfully.')
        else:
            messages.warning(request, 'No tasks selected.')
    return redirect('todo')


@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted successfully.')
    return redirect('todo')


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
