from .views import UsersViewSet
from rest_framework.routers import DefaultRouter

route = DefaultRouter()
route.register("user", UsersViewSet, basename="user")
app_name = "usuarios"
urlpatterns = route.urls
