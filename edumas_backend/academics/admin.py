from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import Staff, Subject, CampusSubject, Class, ClassSubject, ClassCampus, Stream, Term, Student, ParentGuardian, GradingScale, Assessment, AssessmentResult, ReportCard

admin.site.register(Staff)
admin.site.register(Subject)
admin.site.register(CampusSubject)
admin.site.register(Class)
admin.site.register(ClassSubject)
admin.site.register(ClassCampus)
admin.site.register(Stream)
admin.site.register(Term)
admin.site.register(Student)
admin.site.register(ParentGuardian)
admin.site.register(GradingScale)
admin.site.register(Assessment)
admin.site.register(AssessmentResult)
admin.site.register(ReportCard)
