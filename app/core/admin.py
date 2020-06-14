from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from . import models
# user admin class!


class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['email', 'name']


# Register the site
admin.site.register(models.User, UserAdmin)
