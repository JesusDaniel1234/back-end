from django.contrib import admin
from .models import PatientData

# Register your models here.
admin.site.register(PatientData)

class PatientDataAdmin(admin.ModelAdmin):
    list_display = ["patient_name", "CI", "tutor_name"]
