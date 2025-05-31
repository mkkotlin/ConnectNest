from django.contrib import admin
from timelines.models import PostModel, CommentModel, LikeModel

# Register your models here.
@admin.register(PostModel)
class PostModel(admin.ModelAdmin):
    list_display = ('user', 'content','image', 'created_at',)
    list_filter = ('created_at','user')