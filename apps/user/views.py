from rest_framework.decorators import action
from .models import UserProfile
from .serializers import UserSerializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.tokens import RefreshToken


# Create your views here.
class UsersViewSet(ModelViewSet):
    """
        Clase para la gestión de usuarios
    """

    permission_classes = [IsAuthenticated, ]

    queryset = UserProfile.objects.all()

    serializer_class = UserSerializers

    def get_permissions(self):

        permissions = {
            "create": [IsAuthenticated(), IsAdminUser()],
            "destroy": [IsAuthenticated(), IsAdminUser()],
            "list": [IsAuthenticated()],
        }

        return permissions.get(self.action, super().get_permissions())

    def create(self, request, *args, **kwargs):

        serializers = self.get_serializer(data=request.data)

        serializers.is_valid(raise_exception=True)

        serializers.save()

        return Response({ "message": "Usuario creado correctamente", "user": serializers.data },
                        status=status.HTTP_201_CREATED)

    @action(methods=["post"], detail="false")
    def logout(self, request):
        try:

            refresh_token = request.data["refresh_token"]

            token = RefreshToken(refresh_token)

            token.blacklist()

            return Response({ "message": "Sesión Cerrada Correctamente" }, status=status.HTTP_200_OK)

        except Exception as e:

            return Response({ "message": e }, status=status.HTTP_400_BAD_REQUEST)
