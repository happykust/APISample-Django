from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from users.models import User


class UserModelSerializer(serializers.ModelSerializer):
    """
    User model serializer
    """
    class Meta:
        # Select model with which serializer will work
        model = User
        # All fields of out model, which we will use in our serializer
        fields = ['id', 'username', 'password', 'created_at', 'updated_at']
        # Fields, which users can't change via API
        read_only_fields = ['created_at', 'updated_at']
        # Let's secure field 'password' from view via GET request
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """
        Modified function create from class ModelSerializer.
        By default function 'create' from class 'ModelSerializer' doesn't hash incoming passwords.
        Let's fix this to provide normal authentication process.
        :param validated_data:
        :return:
        """
        # Hash incoming password and replace it in validated_data
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        """
        Modified function create from class ModelSerializer.
        By default function 'update' from class 'ModelSerializer' doesn't hash incoming passwords.
        Let's fix this to provide normal authentication process.
        :param instance:
        :param validated_data:
        :return:
        """
        # Hash incoming password and replace it in validated_data
        password_ = validated_data.get('password')
        if password_:
            validated_data['password'] = make_password(password_)
        return super().update(instance, validated_data)
