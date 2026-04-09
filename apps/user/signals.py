from django.db.models.signals import post_migrate
from .models import UserProfile
from django.dispatch import receiver
from django.db import OperationalError, ProgrammingError

@receiver(post_migrate)
def create_admin_user(sender, **kwargs):
    try:
        if not UserProfile.objects.filter(username="admin").exists():
            UserProfile.objects.create_superuser(username="admin", email="admin@admin.com", password="admin1234")
    except (OperationalError, ProgrammingError):
        pass
