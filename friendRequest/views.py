from django.shortcuts import render, get_object_or_404
from accounts.models import CustomUser
from django.contrib import messages
from django.http import JsonResponse
from friendRequest.models import FriendRequest


# Create your views here.
def sendFrq(request, username):
    to_user = get_object_or_404(CustomUser, username = username)    
    if request.user == to_user:
        # messages.error(request, "You can send to yourself")
        return JsonResponse({'error': 'You can send to yourself'})
    
    friend_request, created = FriendRequest.objects.get_or_create(from_user=request.user, to_user=to_user)
    # print(friend_request.id)
    if not created:
        # messages.info(request, 'Aleady sent')
        return JsonResponse({'status':'Request alrady sent'})
    else:
        # messages.success(request, 'Request sent')
        return JsonResponse({'status':'Request sent'})


def acceptRequest(request, request_id):
    fr = get_object_or_404(FriendRequest, id = request_id, to_user = request.user)
    fr.status = 'accepted'
    fr.save()
    return JsonResponse({'message':'accepted'})

def rejectRequest(request, request_id):
    fr = get_object_or_404(FriendRequest, id = request_id, to_user = request.user)
    fr.status = 'rejected'
    fr.save()
    return JsonResponse({'message':'rejected'})