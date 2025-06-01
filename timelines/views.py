from django.shortcuts import render, get_object_or_404
from timelines.models import PostModel, LikeModel
from django.http import JsonResponse
from django.views.decorators.http import require_POST

# Create your views here.
def timeline(request):
    # post_data = []
    post_data = PostModel.objects.filter(user = request.user)
    liked_post = LikeModel.objects.filter(user=request.user).values_list('post_id',flat=True)
    return render(request, 'timelines/timeline.html', {'post_data':post_data,'user':request.user,'is_liked':liked_post})


@require_POST
def like_post(request, post_id):

    post = get_object_or_404(PostModel,id=post_id)
    user = request.user
    like, created = LikeModel.objects.get_or_create(post=post, user=user)
    if not created:
        like.delete()
        liked = False
    else:
        liked = True
    return JsonResponse({
        'success': True,
        'liked':liked,
        'l_count':post.like_count()
    })
    # if created:
    #     return JsonResponse({'success': True,'l_count':post.like_count()})
    # else:
    #     return JsonResponse({'success': False, 'error': 'Already liked'})