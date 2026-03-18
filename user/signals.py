from django.db.models.signals import post_migrate
from django.contrib.auth.models import User
from .models import UserProfile
from django.dispatch import receiver


@receiver(post_migrate)
def create_admin_user(sender, **kwargs):
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(username="admin", password="admin1234")
    if not UserProfile.objects.filter(
        user=User.objects.get(username="admin")
    ).exists():
        user = User.objects.get(username="admin")
        UserProfile.objects.create(user=user)
