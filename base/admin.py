from django.contrib import admin
from .models import (
    ClaveConjunto,
    # * Q-chat-100
    TipoRiesgo,
    ValorRiesgo,
    RangoRiesgo,
)


# Register your models here.


# M-chat-R
admin.site.register(ClaveConjunto)

# Datos Personales

# Q-chat-10
admin.site.register(TipoRiesgo)
admin.site.register(ValorRiesgo)
admin.site.register(RangoRiesgo)
