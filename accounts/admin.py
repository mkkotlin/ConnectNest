from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import CustomUser, Profile

# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ("Social Info", {"fields": ("is_social_user",)}),
    )
    list_display = ("email", "username", "is_social_user", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active", "is_social_user")
    search_fields = ("email", "username")
    ordering = ("email",)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "bio"]
