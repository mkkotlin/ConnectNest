from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import Profile

# Create your views here.
@login_required
def dashboard_view(request):

    
    try:
        profile = Profile.objects.get(user = request.user)
    except Profile.DoesNotExist:
        profile = None

    return render(request, "profiles/dashboard.html", {'profile':profile})



def update_bio(request):
    if request.method == 'POST':
        bio = request.POST.get('bio')
        profile = Profile.objects.get(user = request.user)
        profile.bio = bio
        profile.save()
        return redirect('dashboard')
