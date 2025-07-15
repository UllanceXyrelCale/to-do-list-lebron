from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Classification(models.Model):
    name = models.CharField(max_length=20, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class TodoItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    classification = models.ForeignKey(Classification, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default="Untitled")
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    

    def __str__(self):
        return self.title