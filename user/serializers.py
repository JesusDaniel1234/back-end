from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth.validators import UnicodeUsernameValidator


class UserSerializers(serializers.ModelSerializer):

    username = serializers.CharField(write_only=True)
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)

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

    def create(self, validated_data):
        user_data = {
            "username": validated_data.pop("username"),
            "first_name": validated_data.pop("first_name"),
            "last_name": validated_data.pop("last_name"),
            "email": validated_data.pop("email"),
            "password": validated_data.pop("password"),
        }

        user = User.objects.create(
            username=user_data["username"],
            first_name=user_data["first_name"],
            last_name=user_data["last_name"],
            email=user_data["email"],
        )

        user.set_password(user_data["password"])
        user.save()

        profile = UserProfile.objects.create(user=user, **validated_data)

        return profile
