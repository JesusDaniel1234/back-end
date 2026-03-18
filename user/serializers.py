from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth.validators import UnicodeUsernameValidator


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["id", "username", "first_name", "last_name", "email", "is_staff"]

        extra_kwargs = {
            "username": {
                "validators": [UnicodeUsernameValidator()],
            }
        }

    def to_representation(self, instance: UserProfile):
        user = instance.user
        return {
            "id": instance.id,
            "image": instance.image,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "is_staff": user.is_staff,
            "is_superuser": user.is_superuser
        }
