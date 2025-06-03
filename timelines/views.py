from django.shortcuts import render, get_object_or_404
from timelines.models import PostModel, LikeModel, CommentModel
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.http import require_POST

# Create your views here.
def timeline(request):
    # post_data = []
    # post_data = PostModel.objects.filter(user = request.user)
    post_data = PostModel.objects.all().order_by('-created_at')
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


def add_comment(request):
    content = request.POST.get('content')
    post_id = request.POST.get('post')

    if not content or not post_id:
        return HttpResponseBadRequest('missing data')
    
    try:
        post = PostModel.objects.get(pk=post_id)
        comment = CommentModel.objects.create(
            post=post,
            user = request.user,
            content = content
        )
        return JsonResponse({'status':'success', 'user':comment.user.username, 'content': comment.content})
    except PostModel.DoesNotExist:
        return JsonResponse({'status':'error', 'message': 'post not found'})
    
def post_post(request):
    if request.method == 'POST':
        images = request.FILES.get('img', None)
        contents = request.POST.get('content')
        if images == None and contents == '':
            return JsonResponse({'status':'Post is empty'})
        else:
            post = PostModel.objects.create(user=request.user,
                                            content = contents, 
                                            image = images)
            return JsonResponse({'status':'created post'})