from django.contrib import admin
from .models import TodoItem, Classification
from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

# Register your models here.
admin.site.register(TodoItem)
admin.site.register(Classification)

# Changes the title heading of the admin page.
admin.site.site_title = "LeBron's To-Do Admin"
admin.site.site_header = format_html(
    "LeBron's To-Do Admin | <a href='{}' style='color:white;'>Back to Home</a>",
    reverse('todos')  
)
