from django import forms 
from . import models

class AddTodoItem (forms.ModelForm):
    class Meta:
        model = models.TodoItem
        fields = ['title', 'description', 'completed']