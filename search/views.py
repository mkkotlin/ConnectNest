from django.shortcuts import render
from accounts.models import Profile
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from accounts.models import CustomUser
from django.db.models import Q
from friendRequest.models import FriendRequest


@login_required
def search(request):
    pending_request = FriendRequest.objects.filter(to_user=request.user, status='pending')
    return render(request, 'search/search.html', {'pending_request': pending_request})


@login_required
def notifications_api(request):
    """Returns pending friend requests as JSON — used by the nav bell dropdown."""
    pending = FriendRequest.objects.filter(
        to_user=request.user, status='pending'
    ).select_related('from_user').order_by('-created_at')

    data = [
        {
            'id': fr.id,
            'from_user': fr.from_user.username,
            'created_at': fr.created_at.strftime('%b %d'),
        }
        for fr in pending
    ]
    return JsonResponse({'notifications': data, 'count': len(data)})


@login_required
def result(request):
    profile = Profile.objects.filter(user = request.user)
    status_f = FriendRequest.objects.filter(user = request.user)


# def filter_s(request):
#     q = request.GET.get('q', '')
#     matched_users = CustomUser.objects.filter(Q(username__icontains=q))[:10]

#     results = []
#     for user in matched_users:
#         try:
#             profile_pic = user.profile.profile_pic.url  # adjust based on your model
#         except:
#             profile_pic = '/static/default.jpg'  # fallback

#         results.append({
#             'username': user.username,
#             'profile_pic': profile_pic,
#             'id':user.id
#         })

#     return JsonResponse({'results': results, 'curr_user': request.user.id,})

def filter_s(request):
    q = request.GET.get('q', '')
    curr_user = request.user
    matched_users = CustomUser.objects.filter(Q(username__icontains=q))#.exclude(id=curr_user.id)[:10]

    results = []
    for user in matched_users:
        # Default status
        status = 'none'

        # Check outgoing request from current user to this user
        outgoing = FriendRequest.objects.filter(from_user=curr_user, to_user=user).first()
        if outgoing:
            status = outgoing.status  # pending, accepted, rejected
        else:
            # Check incoming request from this user to current user
            incoming = FriendRequest.objects.filter(from_user=user, to_user=curr_user).first()
            if incoming:
                if incoming.status == 'accepted':
                    status = 'friends'
                else:
                    status = incoming.status

        try:
            profile_pic = user.profile.profile_pic.url
        except:
            profile_pic = '/static/default.jpg'

        results.append({
            'username': user.username,
            'profile_pic': profile_pic,
            'id': user.id,
            'status': status
        })

    return JsonResponse({
        'results': results,
        'curr_user': curr_user.id
    })


def friend_request(request):
    pending_request = FriendRequest.objects.filter(to_user = request.user, status = 'pending')
    return JsonResponse({'pending_request':pending_request}, status = 204)