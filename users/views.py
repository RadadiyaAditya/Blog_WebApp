from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        #request.POST contains all form data
        form = UserRegisterForm(request.POST)
        #check all the username and password critera
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to login{username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users_temp/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users_temp/profile.html')