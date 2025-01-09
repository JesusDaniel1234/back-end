from django.db.models.signals import pre_delete
from .models import DatosPaciente
from django.dispatch import receiver

@receiver(pre_delete, sender=DatosPaciente)
def eliminar_tests(sender, instance, **kwargs):
    # Verificar si existen objetos relacionados antes de eliminarlos
    if hasattr(instance, 'respuestasmchtr_set'):
        instance.respuestasmchtr_set.all().delete()
    if hasattr(instance, 'respuestasqchat_set'):
        instance.respuestasqchat_set.all().delete()
    if hasattr(instance, 'respuestasqchat10_set'):
        instance.respuestasqchat10_set.all().delete()