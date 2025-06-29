from django.shortcuts import render, HttpResponse, redirect
from .models import TodoItem

# Create your views here.
def todos (requests):
    colour1 = "#a32cc4"
    colour2 = "#8904AE"
    items = TodoItem.objects.all()
    return render(requests, 'tasks_app/todos.html', {'todos': items, 'bg_colour_body': colour1, 'bg_colour_navbar':colour2})

def home(requests):
     colour1 = "#a32cc4"
     colour2 = "#8904AE"
     return render(requests, 'tasks_app/home.html', {'bg_colour_body': colour1, 'bg_colour_navbar':colour2})

def tasks_app (requests):
     return redirect('/admin/tasks_app/')
