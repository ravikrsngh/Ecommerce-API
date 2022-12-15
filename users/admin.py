from django.contrib import admin
from django.contrib.auth.models import Group
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken,BlacklistedToken
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.


admin.site.site_header = 'Tawisa'
admin.site.site_title = 'Tawisa'
admin.site.index_title = 'Tawisa Admin'

class UserAddressInline(admin.TabularInline):
    model = UserAddress
    extra = 0

class CustomUserAdmin(UserAdmin):
    inlines = [UserAddressInline]
    fieldsets = (
        ('Authentication Details', {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ('phone_number','date_of_birth','address','profile_pic')
        })
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(RecentSearch)
admin.site.unregister(Group)
