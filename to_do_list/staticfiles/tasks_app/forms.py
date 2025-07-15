from django import forms 
from . import models

class AddTodoItem (forms.ModelForm):
    class Meta:
        model = models.TodoItem
        fields = ['title', 'description', 'completed', 'classification']

class AddClassification(forms.ModelForm):
    class Meta:
        model = models.Classification
        fields = ['name']