from django.shortcuts import render, HttpResponse, redirect
from .models import TodoItem, Classification
from .forms import AddTodoItem, AddClassification
from django.contrib.auth.decorators import login_required

# Views for the tasks app
def home(requests):
     colour1 = "#a32cc4"
     colour2 = "#8904AE"

     if requests.user.is_authenticated:
          classification = Classification.objects.filter(user=requests.user)
          classification_id = requests.GET.get('classification', None)
          selected_classification = int(classification_id) if classification_id else None
          current_classification = Classification.objects.get(id=selected_classification) if selected_classification else None

     else:
          classification = []
          classification_id = None
          selected_classification = 0
          current_classification = 0
          
     if requests.user.is_authenticated:
          if classification_id:
               total_tasks = TodoItem.objects.filter(user=requests.user, classification_id=classification_id).count()
               tasks_completed = TodoItem.objects.filter(user=requests.user, completed=True, classification_id=classification_id).count()
               tasks_incomplete = TodoItem.objects.filter(user=requests.user, completed=False, classification_id=classification_id).count()
          
          else:
               total_tasks = TodoItem.objects.filter(user=requests.user).count()
               tasks_completed = TodoItem.objects.filter(user=requests.user, completed=True).count()
               tasks_incomplete = TodoItem.objects.filter(user=requests.user, completed=False).count()
     else:
          total_tasks = 0
          tasks_completed = 0
          tasks_incomplete = 0
     return render(requests, 'tasks_app/home.html', {'bg_colour_body': colour1, 'bg_colour_navbar':colour2, 'total_tasks': total_tasks, 'tasks_completed': tasks_completed, 'tasks_incomplete': tasks_incomplete, 'current_classification': current_classification, 'classification': classification})

@login_required(login_url='login')
def todos (requests):
    colour1 = "#a32cc4"
    colour2 = "#8904AE"

    # Get the classification from the request, default to None if not provided
    classification_id = requests.GET.get('classification', None)
    
    if classification_id:
         items = TodoItem.objects.filter(user=requests.user, classification_id=classification_id)
    else:
         items = TodoItem.objects.filter(user=requests.user)

    # User specific stuff
    classification = Classification.objects.filter(user=requests.user)
    selected_classification = int(classification_id) if classification_id else None
    current_classification = Classification.objects.get(id=selected_classification) if selected_classification else None
    completed = TodoItem.completed

    return render(requests, 'tasks_app/todos.html', {'todos': items, 'bg_colour_body': colour1, 'bg_colour_navbar':colour2, 'completed': completed, 'classification': classification, 'selected_classification': selected_classification, 'current_classification': current_classification})

@login_required(login_url='login')
def add_classifications(requests):
     colour1 = "#a32cc4"
     colour2 = "#8904AE"
     if requests.method == 'POST':
          form = AddClassification(requests.POST)
          if form.is_valid():
               classification = form.save(commit=False)
               classification.user = requests.user
               classification.save()
               return redirect('todos')
     else:
          form = AddClassification()
     
     classifications = Classification.objects.filter(user=requests.user)

     return render(requests, 'tasks_app/add_classifications.html', {'classifications':classifications, 'form': form, 'bg_colour_body': colour1, 'bg_colour_navbar':colour2})

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

@login_required(login_url='login')
def complete_todo(requests, todo_id):
     todo = TodoItem.objects.get(user=requests.user, id=todo_id)
     todo.completed = True
     todo.save()
     return redirect('todos')

@login_required(login_url='login')
def incomplete_todo(requests, todo_id):
     todo = TodoItem.objects.get(user=requests.user, id=todo_id)
     todo.completed = False
     todo.save()
     return redirect('todos')

@login_required(login_url='login')
def remove_todo(requests, todo_id):
     todo = TodoItem.objects.get(user=requests.user, id=todo_id)
     todo.delete()
     return redirect('todos')

@login_required(login_url='login')
def remove_classification(requests, classification_id):
     classification = Classification.objects.get(user=requests.user, id=classification_id)
     classification.delete()
     return redirect('todos')

@login_required(login_url='login')
def tasks_app (requests):
     return redirect('/admin/tasks_app/')

