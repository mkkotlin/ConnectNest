from django.shortcuts import render, redirect
from accounts.forms import CustomUserRegistrationForm, CustomLoginForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.


def UserRegister(request):
    if request.method == 'POST':
        form = CustomUserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserRegistrationForm()
        return render(request, 'accounts/register.html', {'form': form})
    
def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomLoginForm()
        return render(request, 'accounts/login.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('login')