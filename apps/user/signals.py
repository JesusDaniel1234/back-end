from django.db.models.signals import post_migrate
from .models import UserProfile
from django.dispatch import receiver


@receiver(post_migrate)
def create_admin_user(sender, **kwargs):
    if not UserProfile.objects.filter(username="admin").exists():
        UserProfile.objects.create_superuser(username="admin",email="admin@admin.com", password="admin1234")
