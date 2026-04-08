from .views import PatientDataViewSet
from rest_framework.routers import SimpleRouter

app_name = "patient"

router = SimpleRouter()

router.register(r"patient", PatientDataViewSet)

urlpatterns =  router.urls


