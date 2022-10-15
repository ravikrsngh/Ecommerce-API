from rest_framework import serializers
from django.contrib.auth.models import User

class RegisterUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name')
