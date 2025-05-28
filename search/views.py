from django.shortcuts import render
from accounts.models import Profile
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from accounts.models import CustomUser
from django.db.models import Q

# Create your views here.
@login_required
def search(request):
    return render(request, 'search/search.html')


@login_required
def result(request):
    profile = Profile.objects.filter(user = request.user)


def filter_s(request):
    q = request.GET.get('q', '')
    matched_users = CustomUser.objects.filter(Q(username__icontains=q))[:10]

    results = []
    for user in matched_users:
        try:
            profile_pic = user.profile.profile_pic.url  # adjust based on your model
        except:
            profile_pic = '/static/default.jpg'  # fallback

        results.append({
            'username': user.username,
            'profile_pic': profile_pic,
            'id':user.id
        })

    return JsonResponse({'results': results, 'curr_user': request.user.id})