from django.shortcuts import render
from accounts.models import Profile
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def search(request):
    return render(request, 'search/search.html')


@login_required
def result(request):
    profile = Profile.objects.filter(user = request.user)