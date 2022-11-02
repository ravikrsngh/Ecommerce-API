from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
# Create your models here.


def user_directory_path(instance,filename):
    return 'media/ProfilePictures/user_{0}/{1}'.format(instance.email, filename)

class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.CharField(max_length=10,default="")
    address = models.TextField(default="")
    profile_pic = models.ImageField(upload_to = user_directory_path,null=True,blank=True)
    email = models.EmailField(unique=True, max_length=254)

    def __str__(self):
        return self.email



class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class State(models.Model):
    country = models.ForeignKey(Country,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class UserAddress(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    address_line1 = models.CharField(max_length=120)
    address_line2 = models.CharField(max_length=120)
    city = models.CharField(max_length=30)
    zipcode = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    receive_sms_notitication = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email


class RecentSearch(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
