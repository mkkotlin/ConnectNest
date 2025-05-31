from django.shortcuts import render
from timelines.models import PostModel, LikeModel
from django.http import JsonResponse

# Create your views here.
def timeline(request):
    # post_data = []
    post_data = PostModel.objects.filter(user = request.user)
    return render(request, 'timelines/timeline.html', {'post_data':post_data})


# def like_post(request):
#     print(request.method)
#     if request.method == 'POST':
#         print(request.POST.get('post_id'))
#         post_id = request.POST.get('post_id')
#         post = PostModel.objects.get(id=post_id)
#         print(post_id,post)
#         like, created = LikeModel.objects.get_or_create(user=request.user, post = post)
#         if not created:
#             like.delete()
#     return JsonResponse({'liked':created, 'like_count':post.like_count()})


def like_post(request, post_id):
    if request.method == 'POST':
        post = PostModel.objects.get(id=post_id)
        user = request.user
        like, created = LikeModel.objects.get_or_create(post=post, user=user)
        if created:
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'error': 'Already liked'})