from django.db import models
from django.contrib.auth.models import User

# Create your models here.
def dir_image_user(instance, filename):
    # Configuración de ruta para almacenar la imagen de perfil de usuario
    return "user_image_{0}/{1}".format(instance.user.username, filename)


class UserProfile(models.Model):
    """
        Modelo de usuario basado en el usuario por defecto de Django
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField("Número de Teléfono", max_length=8, blank=True, null=True)
    image = models.ImageField(default="user_defoult.PNG", upload_to=dir_image_user, blank=True, null=True)

    def __str__(self):
        return self.user.username
