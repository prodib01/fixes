from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import UserProfile, UserProfileManager, Role, Permission, UserRole, Document
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group

admin.site.register(Permission)
admin.site.register(UserProfile)
admin.site.register(Role)
admin.site.register(UserRole)
admin.site.register(Document)
