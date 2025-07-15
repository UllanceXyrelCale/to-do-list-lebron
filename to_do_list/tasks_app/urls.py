from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tasks/', views.todos, name='todos'),
    path('add_todos/', views.add_todos, name='add-todos'),
    path('add_classifications/', views.add_classifications, name='add-classifications'),
    path('admin-tasks/', views.tasks_app, name='tasks-app-admin'),
    path('complete/<int:todo_id>/', views.complete_todo, name='complete-todo'),
    path('incomplete/<int:todo_id>/', views.incomplete_todo, name='incomplete-todo'),
    path('remove-todo/<int:todo_id>/', views.remove_todo, name='remove-todo'),
    path('remove-classification/<int:classification_id>/', views.remove_classification, name='remove-classification'),
]