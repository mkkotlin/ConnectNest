from django.shortcuts import render
from timelines.models import PostModel

# Create your views here.
def timeline(request):
    # post_data = []
    post_data = PostModel.objects.filter(user = request.user)
    return render(request, 'timelines/timeline.html', {'post_data':post_data})