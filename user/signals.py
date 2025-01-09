from django.db.models.signals import post_migrate
from django.contrib.auth.models import User
from .models import PerfilUsuario
from django.dispatch import receiver


@receiver(post_migrate)
def create_admin_user(sender, **kwargs):
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser(username="admin", password="admin1234")
    if not PerfilUsuario.objects.filter(
        usuario=User.objects.get(username="admin")
    ).exists():
        usuario = User.objects.get(username="admin")
        PerfilUsuario.objects.create(usuario=usuario)
