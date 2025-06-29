from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/', views.todos, name='todos'),
    path('admin-tasks/', views.tasks_app, name='tasks-app-admin')
]