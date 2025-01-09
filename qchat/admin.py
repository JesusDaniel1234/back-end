from django.contrib import admin
from .models import PreguntaQchat, RespuestaTutorQChat, RespuestasQChat

# Register your models here.

admin.site.register(PreguntaQchat)
admin.site.register(RespuestaTutorQChat)
admin.site.register(RespuestasQChat)
