from django.shortcuts import render, HttpResponse, redirect
from .models import TodoItem
from .forms import AddTodoItem
from django.contrib.auth.decorators import login_required

# Views for the tasks app
@login_required(login_url='login')
def todos (requests):
    colour1 = "#a32cc4"
    colour2 = "#8904AE"
    items = TodoItem.objects.filter(user=requests.user)
    completed = TodoItem.completed
    return render(requests, 'tasks_app/todos.html', {'todos': items, 'bg_colour_body': colour1, 'bg_colour_navbar':colour2, 'completed': completed})

def home(requests):
     colour1 = "#a32cc4"
     colour2 = "#8904AE"
     if requests.user.is_authenticated:
          total_tasks = TodoItem.objects.filter(user=requests.user).count()
          tasks_completed = TodoItem.objects.filter(user=requests.user, completed=True).count()
          tasks_incomplete = TodoItem.objects.filter(user=requests.user, completed=False).count()
     else:
          total_tasks = 0
          tasks_completed = 0
          tasks_incomplete = 0
     return render(requests, 'tasks_app/home.html', {'bg_colour_body': colour1, 'bg_colour_navbar':colour2, 'total_tasks': total_tasks, 'tasks_completed': tasks_completed, 'tasks_incomplete': tasks_incomplete})

@login_required(login_url='login')
def add_todos(requests):
     colour1 = "#a32cc4"
     colour2 = "#8904AE"
     if requests.method == 'POST':
          form = AddTodoItem(requests.POST)
          if form.is_valid():
               todo = form.save(commit=False)
               todo.user = requests.user
               todo.save()
               return redirect('todos')
     else:
          form = AddTodoItem()

     return render(requests, 'tasks_app/add_todos.html', {'form':form, 'bg_colour_body':colour1, 'bg_colour_navbar':colour2})

def complete_todo(requests, todo_id):
     todo = TodoItem.objects.get(user=requests.user, id=todo_id)
     todo.completed = True
     todo.save()
     return redirect('todos')
     
def incomplete_todo(requests, todo_id):
     todo = TodoItem.objects.get(user=requests.user, id=todo_id)
     todo.completed = False
     todo.save()
     return redirect('todos')

def remove_todo(requests, todo_id):
     todo = TodoItem.objects.get(user=requests.user, id=todo_id)
     todo.delete()
     return redirect('todos')

def tasks_app (requests):
     return redirect('/admin/tasks_app/')

