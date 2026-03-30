from .views import PatientDataViewSet
from rest_framework.routers import DefaultRouter

app_name = "patient"

router = DefaultRouter()

router.register(r"patient", PatientDataViewSet)

urlpatterns =  router.urls


