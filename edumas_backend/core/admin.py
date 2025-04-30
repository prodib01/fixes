from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import School, SchoolSettings, AcademicYear, Campus, ClassRoom, Department, Event

admin.site.register(School)
admin.site.register(SchoolSettings)
admin.site.register(AcademicYear)   
admin.site.register(Campus)
admin.site.register(ClassRoom)
admin.site.register(Department)
admin.site.register(Event)
