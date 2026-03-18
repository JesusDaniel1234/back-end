from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


# Create your models here.
def dir_image_user(instance, filename):
    # Configuración de ruta para almacenar la imagen de perfil de usuario
    return "user_image_{0}/{1}".format(instance.usuario.username, filename)


class UserProfile(models.Model):
    """
        Modelo de usuario basado en el usuario por defecto de Django
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(
        default="user_defoult.PNG", upload_to=dir_image_user
    )

    def __str__(self):
        return self.user.username


# Signals para la gestion del modelo User (Modelo propio de Django)
@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(usuario=instance)


@receiver(post_save, sender=User)
def save_user(sender, instance, **kwargs):
    instance.perfilusuario.save()


@receiver(post_delete, sender=UserProfile)
def delete_user(sender, instance, **kwargs):
    user = instance.usuario
    user.delete()
