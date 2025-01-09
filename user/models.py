from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


# Create your models here.
def perfil_directorio_ruta(instance, filename):
    return "user_image_{0}/{1}".format(instance.usuario.username, filename)


# Create your models here.
class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen_perfil = models.ImageField(
        default="user_defoult.PNG", upload_to=perfil_directorio_ruta
    )

    def __str__(self):
        return self.usuario.username


# Signals
@receiver(post_save, sender=User)
def crear_usuario_perfil(sender, instance, created, **kwargs):
    if created:
        PerfilUsuario.objects.create(usuario=instance)


@receiver(post_save, sender=User)
def guardar_usuario_perfil(sender, instance, **kwargs):
    instance.perfilusuario.save()


@receiver(post_delete, sender=PerfilUsuario)
def eliminar_usuario_perfil(sender, instance, **kwargs):
    user = instance.usuario
    user.delete()
