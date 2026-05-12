from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth.validators import UnicodeUsernameValidator


class UserSerializers(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True, required=False)

    created_date = serializers.DateField(read_only=True)

    updated_date = serializers.DateField(read_only=True)

    class Meta:
        model = UserProfile

        fields = ["id", "username", "first_name", "last_name", "email", "phone_number", "password", "image",
                  "created_date", "updated_date"]

        extra_kwargs = {
            "username": {
                "validators": [UnicodeUsernameValidator()],
            }
        }

    def to_representation(self, instance: UserProfile):
        return {
            "id": instance.id,
            "image": instance.image.url,
            "username": instance.username,
            "first_name": instance.first_name,
            "last_name": instance.last_name,
            "phone_number": instance.phone_number,
            "email": instance.email,
            "is_staff": instance.is_staff,
            "is_superuser": instance.is_superuser,
            "created_date": instance.created_date,
            "updated_date": instance.updated_date
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = UserProfile(**validated_data)
        user.set_password(password)
        user.save()
        return user
