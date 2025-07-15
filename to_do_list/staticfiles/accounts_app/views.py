from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Views for the accounts app
def register_view(request):
    # Handles the registration of a new user.
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('todos')  # Redirect to the todos page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'accounts_app/register.html', {'form':form})

def login_view(request):
    # Handles user login.
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('todos') # Redirect to the todos page after successful login
    else:
        form = AuthenticationForm()
    return render(request, 'accounts_app/login.html', {'form':form})

def logout_view(request):
    # Handles user Logout.
    if request.method == 'POST':
        logout(request)
        return redirect('todos') # Redirect to the login page after successful logout