# medical/models.py

from django.db import models
from accounts.models import CustomUser
from core.models import School, Campus
from academics.models import Student, Staff


class HealthRecord(models.Model):
    BLOOD_TYPE_CHOICES = (
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
        ('unknown', 'Unknown'),
    )
    
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='health_record')
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='health_records')  # For multi-tenancy
    blood_type = models.CharField(max_length=10, choices=BLOOD_TYPE_CHOICES, blank=True, null=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)  # in cm
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)  # in kg
    allergies = models.TextField(blank=True, null=True)
    chronic_conditions = models.TextField(blank=True, null=True)
    medications = models.TextField(blank=True, null=True)
    insurance_provider = models.CharField(max_length=255, blank=True, null=True)
    insurance_number = models.CharField(max_length=100, blank=True, null=True)
    last_physical_exam = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Health Record - {self.student.user.get_full_name()}"


class MedicalVisit(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='medical_visits')
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='medical_visits')  # For multi-tenancy
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE, related_name='medical_visits')
    attended_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='attended_medical_visits')
    date = models.DateField()
    time = models.TimeField()
    complaint = models.TextField()
    diagnosis = models.TextField(blank=True, null=True)
    treatment = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    follow_up_needed = models.BooleanField(default=False)
    followup_date = models.DateField(blank=True, null=True)
    parents_notified = models.BooleanField(default=False)
    notification_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.student.user.get_full_name()} - {self.date} - {self.complaint[:30]}..."


class MedicalIncident(models.Model):
    SEVERITY_CHOICES = (
        ('minor', 'Minor'),
        ('moderate', 'Moderate'),
        ('severe', 'Severe'),
        ('critical', 'Critical'),
    )
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='medical_incidents')
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='medical_incidents')  # For multi-tenancy
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE, related_name='medical_incidents')
    reported_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='reported_incidents')
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()
    severity = models.CharField(max_length=20, choices=SEVERITY_CHOICES)
    action_taken = models.TextField()
    location = models.CharField(max_length=255, blank=True, null=True)
    witnesses = models.TextField(blank=True, null=True)
    parents_notified = models.BooleanField(default=False)
    notification_date = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.student.user.get_full_name()} - {self.date} - {self.get_severity_display()}"

