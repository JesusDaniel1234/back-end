from django.contrib import admin
from .models import QchatResponses,QchatQuestion

# Register your models here.

admin.site.register(QchatQuestion)

admin.site.register(QchatResponses)
