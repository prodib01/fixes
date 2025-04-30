from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import HealthRecord, MedicalVisit, MedicalIncident

admin.site.register(HealthRecord)
admin.site.register(MedicalVisit)
admin.site.register(MedicalIncident)
