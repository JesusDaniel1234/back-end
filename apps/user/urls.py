from .views import UsersViewSet
from rest_framework.routers import SimpleRouter

route = SimpleRouter()

route.register("", UsersViewSet, basename="user")

app_name = "usuarios"

urlpatterns = route.urls
