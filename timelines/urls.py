from django.urls import path
from timelines.views import like_post, timeline, add_comment

urlpatterns = [
    path('like_post/<int:post_id>/',like_post, name='like_post'),
    path('timeline/', timeline, name = 'timeline'),
    path('add_comment/', add_comment, name = 'add_comment')
]