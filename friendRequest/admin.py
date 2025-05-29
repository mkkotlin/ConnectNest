from django.contrib import admin
from friendRequest.models import FriendRequest

# Register your models here.
# admin.site.register(FriendRequest)
@admin.register(FriendRequest)
class FriendRequestAdmin(admin.ModelAdmin):
    list_display = ('from_user','to_user','status','created_at')
    list_filter = ('status','created_at')
    search_fields = ('status',)