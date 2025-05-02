from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Attendance, AttendanceReport, Attendance, ClassAttendance, ClassAttendanceDetail

admin.site.register(Attendance)
admin.site.register(ClassAttendance)
admin.site.register(ClassAttendanceDetail)
admin.site.register(AttendanceReport)