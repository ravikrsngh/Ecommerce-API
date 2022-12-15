from django.contrib import admin
from django_summernote.models import Attachment
from rest_framework_simplejwt.token_blacklist.models import *
# Register your models here.

admin.site.unregister(Attachment)
admin.site.unregister(OutstandingToken)
admin.site.unregister(BlacklistedToken)
