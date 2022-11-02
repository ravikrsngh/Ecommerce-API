from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import viewsets
from .serializers import *
from users.models import *
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['name'] = user.first_name
        try:
            token['profile_pic'] = user.profile_pic.url
        except Exception as e:
            token['profile_pic'] = ""

        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer



def start(request):
    return render(request,'index.html')

def test(request):
    return render(request,'<h1>Hey</h1>')


class RegisterUserAPI(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()

    def get_serializer_class(self):
        if self.action == "update":
            return UpdateUserSerializer
        elif self.action == "list":
            return UserDetailSerializer
        elif self.action == "retrieve":
            return UserDetailSerializer
        else:
            return RegisterUserSerializer


class UserAddressAPI(viewsets.ModelViewSet):
    queryset = UserAddress.objects.all()
    serializer_class = AddressSerializer
    permission_classes =[IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return UserAddress.objects.filter(user=user)


class RecentSearchAPI(viewsets.ModelViewSet):
    queryset = RecentSearch.objects.all()
    serializer_class = RecentSearchSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return RecentSearch.objects.filter(user=user)
