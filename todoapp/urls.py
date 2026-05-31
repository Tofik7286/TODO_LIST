from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo, name='todo'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
]