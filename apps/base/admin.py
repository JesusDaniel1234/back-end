from django.contrib import admin
from .models import (
    TipoRiesgo,
    ValorRiesgo,
    RangoRiesgo,
)


# Register your models here.
admin.site.register(TipoRiesgo)
admin.site.register(ValorRiesgo)
admin.site.register(RangoRiesgo)
