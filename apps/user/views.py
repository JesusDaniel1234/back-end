from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter

from .models import UserProfile
from .serializers import UserSerializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken

from ..base.pagination import MediumPaginationClass


# Create your views here.
class UsersViewSet(ModelViewSet):
    """
        Clase para la gestión de usuarios
    """

    permission_classes = [IsAuthenticated, ]

    pagination_class = MediumPaginationClass

    queryset = UserProfile.objects.all()

    serializer_class = UserSerializers

    filter_backends = [SearchFilter, DjangoFilterBackend]

    search_fields = [
        "username",
        "first_name",
        "last_name",
        "email",
    ]

    def get_permissions(self):

        permissions = {
            "create": [IsAuthenticated(), IsAdminUser()],
            "destroy": [IsAuthenticated(), IsAdminUser()],
            "list": [IsAuthenticated()],
        }

        return permissions.get(self.action, super().get_permissions())

    def get_queryset(self):

        return UserProfile.objects.exclude(id=1).order_by('id')

    def create(self, request, *args, **kwargs):

        print(request.data)

        serializers = self.get_serializer(data=request.data)

        serializers.is_valid(raise_exception=True)
        serializers.save()

        return Response({ "message": "Usuario creado correctamente", "user": serializers.data },
                        status=status.HTTP_201_CREATED)

    @action(methods=["post"], detail=False)
    def logout(self, request):
        try:

            refresh_token = request.data["refresh_token"]

            token = RefreshToken(refresh_token)

            token.blacklist()

            return Response({ "message": "Sesión Cerrada Correctamente" }, status=status.HTTP_200_OK)

        except Exception as e:

            return Response({ "message": e }, status=status.HTTP_400_BAD_REQUEST)
