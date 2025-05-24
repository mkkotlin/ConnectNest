from django.shortcuts import render, redirect
from accounts.forms import CustomUserRegistrationForm, CustomLoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

# Create your views here.


def UserRegister(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "You are registered")
            return redirect('dashboard',)
        else:
            messages.error(request, 'Please use correct creds')
            return redirect('register')
    else:
        form = CustomUserRegistrationForm()
        return render(request, 'accounts/register.html', {'form': form})
    
def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # messages.success(request, "You are logged in")
            return redirect('dashboard')
        else:
            return render
    else:
        form = CustomLoginForm()
        return render(request, 'accounts/login.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('/')