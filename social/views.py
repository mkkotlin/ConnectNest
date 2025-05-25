from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from accounts.models import Profile
from django.http import JsonResponse, HttpResponse

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
        return JsonResponse({'status':'success'}) #204 return empty page
    return JsonResponse({'status':'error'})


def update_pic(request):
    if request.method == 'POST':
        profile_pic = request.FILES.get('profile_pic')  # Correct: get file from FILES
        if profile_pic:
            profile = Profile.objects.get(user=request.user)
            profile.profile_pic = profile_pic
            profile.save()
            return JsonResponse({'status': 'success','new_profile_pic_url': profile.profile_pic.url})
        else:
            return JsonResponse({'status': 'error', 'message': 'No image uploaded'})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})