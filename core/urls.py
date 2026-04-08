from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="EvaluaTEA API",
        default_version='v2',
        description="Documentación de los endpoints en EvaluaTEA API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="jesusdanielsanchezalarcon79@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

api_version = "api/v2/"

urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),
    # Swagger
    path(f'{api_version}swagger.<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path(f'{api_version}swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path(f'{api_version}redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # Base Configuration (Token and base app)
    path(f"{api_version}token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path(f"{api_version}token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path(f"{api_version}base/", include("apps.base.urls", namespace="api")),
    # Tests
    path(f"{api_version}qchat/", include("apps.qchat.urls")),
    path(f"{api_version}qchat10/", include("apps.qchat10.urls")),
    path(f"{api_version}mchatr/", include("apps.mchatr.urls")),
    # Users
    path(f"{api_version}user/", include("apps.user.urls", namespace="usuarios")),
    path(f"{api_version}patient/", include("apps.patient.urls", namespace="patient")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
