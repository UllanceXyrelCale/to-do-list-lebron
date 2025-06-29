from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def register(request):
    # Handles the registration of a new user.
    return render(request, 'register.html')