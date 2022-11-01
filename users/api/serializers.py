from rest_framework import serializers
from users.models import *

class RegisterUserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['email'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            phone_number=validated_data['phone_number']
        )
        user.set_password(validated_data['password'])
        #user.is_active = False
        user.save()
        return user

    def update(self,instance,validated_data):
        instance.username=validated_data['email']
        instance.email=validated_data['email']
        instance.first_name=validated_data['first_name']
        instance.phone_number=validated_data['phone_number']
        #instance.set_password(validated_data['password'])
        #instance.is_active = False
        instance.save()
        return instance

    class Meta:
        model = CustomUser
        fields = ('password', 'email', 'first_name','phone_number')


class UpdateUserSerializer(serializers.ModelSerializer):
    profile_pic = serializers.ImageField(required=False)
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name','phone_number','profile_pic','address','date_of_birth')


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = ('password',)

class AddressSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        request = self.context.get('request')
        instance = UserAddress.objects.create(user=request.user,**validated_data)
        return instance

    class Meta:
        model = UserAddress
        exclude = ('user','receive_sms_notitication',)
