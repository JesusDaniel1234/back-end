from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

api_version = "api/v1/"

urlpatterns = [
    path("admin/", admin.site.urls),
    path(f"{api_version}token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path(f"{api_version}token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path(f"{api_version}", include("base.urls", namespace="api")),
    # Tests
    path(f"{api_version}mchatr/", include("mchatr.urls", namespace="mchatr")),
    path(f"{api_version}qchat/", include("qchat.urls", namespace="qchat")),
    path(f"{api_version}qchat10/", include("qchat10.urls", namespace="qchat10")),
    path(f"{api_version}", include("user.urls", namespace="usuarios")),
    path(f"{api_version}pacientes/", include("pacientes.urls", namespace="pacientes")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
