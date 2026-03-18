from django.contrib import admin
from .models import UserProfile


# Register your models here.
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["user__username", "user__first_name", "user__last_name", "user__email"]


admin.site.register(UserProfile, UserProfileAdmin)
