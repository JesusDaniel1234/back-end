from django.db import models
from django.contrib.auth.models import User, BaseUserManager, AbstractBaseUser, PermissionsMixin


# Create your models here.
def dir_image_user(instance, filename):
    # Configuración de ruta para almacenar la imagen de perfil de usuario
    return "user_image_{0}/{1}".format(instance.user.username, filename)


class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, is_staff, is_superuser, **extra_fields):
        if not password:
            raise ValueError("La contraseña es obligatoria")

        user = self.model(
            username=username,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields,
        )

        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, is_staff=False, is_superuser=False, **extra_fields)

    def create_staff(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, is_staff=True, is_superuser=False, **extra_fields)

    def create_superuser(self, username, email, password=None, **extra_fields):
        return self._create_user(username, email, password, is_staff=True, is_superuser=True, **extra_fields)


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
        Modelo de usuario basado en el usuario por defecto de Django
    """

    username = models.CharField("Nombre de Usuario", max_length=255, unique=True)

    email = models.CharField("Correo Electrónico", max_length=255, unique=True, blank=True, null=True)

    first_name = models.CharField("Nombre", max_length=255, blank=True, null=True)

    last_name = models.CharField("Apellidos", max_length=255, blank=True, null=True)

    phone_number = models.CharField(
        "Número de Teléfono", max_length=8, unique=True, null=True, blank=True
    )
    image = models.ImageField(
        "Imagen de Perfil", default="user_default.PNG", upload_to=dir_image_user, max_length=255, null=True, blank=True
    )

    is_active = models.BooleanField("Está activo", default=True)

    is_staff = models.BooleanField("Es parte del equipo", default=False)

    is_superuser = models.BooleanField("Es un superusuario", default=False)

    created_date = models.DateField("Creado", auto_now=False, auto_now_add=True)

    updated_date = models.DateField("Actualizado", auto_now=True, auto_now_add=False)

    objects = UserManager()

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    USERNAME_FIELD = "username"

    def natural_key(self):
        return self.username

    def __str__(self):
        return self.first_name or self.username
