from django.contrib import admin
from timelines.models import PostModel, CommentModel, LikeModel

# Register your models here.
@admin.register(PostModel)
class PostModel(admin.ModelAdmin):
    list_display = ('user', 'content','image', 'created_at',)
    list_filter = ('created_at','user')


@admin.register(CommentModel)
class CommenttModel(admin.ModelAdmin):
    list_display = ('user', 'post','content', 'created_at',)
    list_filter = ('created_at','user')


@admin.register(LikeModel)
class LikeModel(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at',)
    list_filter = ('created_at','post',)