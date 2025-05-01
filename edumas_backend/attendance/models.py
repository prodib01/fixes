
from django.db import models
from accounts.models import CustomUser
from core.models import School, Campus
from academics.models import Staff, Student, Stream, Class


class Attendance(models.Model):
    ATTENDANCE_TYPE_CHOICES = (
        ('student', 'Student'),
        ('staff', 'Staff'),
    )
    
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='attendance_records')  # For multi-tenancy
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE, related_name='attendance_records')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='attendance_records')
    attendance_type = models.CharField(max_length=10, choices=ATTENDANCE_TYPE_CHOICES)
    date = models.DateField()
    present = models.BooleanField(default=False)
    check_in_time = models.TimeField(null=True, blank=True)
    check_out_time = models.TimeField(null=True, blank=True)
    recorded_by = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, related_name='recorded_attendance')
    reason_for_absence = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ['user', 'date']
        
    def __str__(self):
        return f"{self.user.get_full_name()} - {self.date} - {'Present' if self.present else 'Absent'}"


class ClassAttendance(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='class_attendance')  # For multi-tenancy
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE, related_name='class_attendance')
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE, related_name='attendance_records')
    date = models.DateField()
    taken_by = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='taken_class_attendance')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ['stream', 'date']
        
    def __str__(self):
        return f"{self.stream.class_obj.name} {self.stream.name} - {self.date}"


class ClassAttendanceDetail(models.Model):
    class_attendance = models.ForeignKey(ClassAttendance, on_delete=models.CASCADE, related_name='details')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='class_attendance_details')
    present = models.BooleanField(default=False)
    reason_for_absence = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ['class_attendance', 'student']
        
    def __str__(self):
        return f"{self.student.user.get_full_name()} - {self.class_attendance.date} - {'Present' if self.present else 'Absent'}"


class AttendanceReport(models.Model):
    REPORT_TYPE_CHOICES = (
        ('daily', 'Daily'),
        ('weekly', 'Weekly'),
        ('monthly', 'Monthly'),
        ('term', 'Term'),
        ('annual', 'Annual'),
    )
    
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='attendance_reports')  # For multi-tenancy
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE, related_name='attendance_reports', null=True, blank=True)
    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='attendance_reports', null=True, blank=True)
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE, related_name='attendance_reports', null=True, blank=True)
    report_type = models.CharField(max_length=10, choices=REPORT_TYPE_CHOICES)
    start_date = models.DateField()
    end_date = models.DateField()
    generated_by = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='generated_attendance_reports')
    report_data = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        if self.stream:
            target = f"{self.stream.class_obj.name} {self.stream.name}"
        elif self.class_obj:
            target = f"{self.class_obj.name}"
        elif self.campus:
            target = f"{self.campus.name}"
        else:
            target = f"{self.school.name}"
        
        return f"{self.get_report_type_display()} Report for {target} ({self.start_date} to {self.end_date})"