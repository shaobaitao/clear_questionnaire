from django.contrib import admin

from .models import USER_INFO, USER, USER_LOGIN

# Register your models here.
admin.site.register([USER_INFO, USER, USER_LOGIN])
