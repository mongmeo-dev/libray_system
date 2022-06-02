from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'name']

    def create(self, validated_data):
        user = User(username=validated_data['username'], email=validated_data['email'], name=validated_data['name'])
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=150, read_only=True)
    password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'name']

    def update(self, instance, validated_data):
        updated_user = super().update(instance, validated_data)

        if validated_data['password']:
            updated_user.set_password(validated_data['password'])

        updated_user.save()
        return updated_user


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
