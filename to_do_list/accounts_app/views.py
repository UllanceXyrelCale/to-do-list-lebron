from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    # Handles the registration of a new user.
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todos')  # Redirect to the todos page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'accounts_app/register.html', {'form':form})