from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Task

admin.site.unregister(User)

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'first_name', 'is_active', 'date_joined')
    search_fields = ('email', 'first_name')


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category', 'priority', 'status', 'due_date', 'created_at')
    list_filter = ('priority', 'status', 'category')
    search_fields = ('title', 'user__email')
