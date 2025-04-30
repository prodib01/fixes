from django.db import models
from core.models import School, Campus, ClassRoom
from academics.models import Stream, Staff, Subject, Term


class Timetable(models.Model):
    DAY_CHOICES = (
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    )
    
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='timetables')  # For multi-tenancy
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE, related_name='timetables')
    term = models.ForeignKey(Term, on_delete=models.CASCADE, related_name='timetables', null=True, blank=True)
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    created_by = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='created_timetables')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        if self.term:
            return f"{self.name} - {self.campus.name} - {self.term.name}"
        return f"{self.name} - {self.campus.name} ({self.start_date} to {self.end_date})"


class TimeSlot(models.Model):
    """Represents a specific time period that can be used in timetable scheduling"""
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='time_slots')
    name = models.CharField(max_length=100)  # e.g., "Period 1", "Morning Session", "Lunch Break"
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_break = models.BooleanField(default=False)  # To identify breaks/lunch periods
    
    def __str__(self):
        return f"{self.name} ({self.start_time.strftime('%H:%M')} - {self.end_time.strftime('%H:%M')})"
    
    class Meta:
        ordering = ['start_time']


class TimetableSlot(models.Model):
    """Represents a specific teaching slot in the timetable with day, time, teacher, subject, etc."""
    timetable = models.ForeignKey(Timetable, on_delete=models.CASCADE, related_name='slots')
    day = models.CharField(max_length=20, choices=Timetable.DAY_CHOICES)
    time_slot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE, related_name='timetable_slots')
    stream = models.ForeignKey(Stream, on_delete=models.CASCADE, related_name='timetable_slots')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='timetable_slots')
    teacher = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='teaching_slots')
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE, related_name='timetable_slots', null=True, blank=True)
    is_recurring = models.BooleanField(default=True)  # If False, this is a one-time slot
    specific_date = models.DateField(null=True, blank=True)  # For non-recurring slots
    
    def __str__(self):
        class_info = f"{self.stream.name} - {self.subject.name}"
        if self.is_recurring:
            return f"{self.day.capitalize()} | {self.time_slot} | {class_info}"
        return f"{self.specific_date} | {self.time_slot} | {class_info}"
    
    class Meta:
        ordering = ['day', 'time_slot__start_time']
        constraints = [
            # Ensure we don't double-book a teacher at the same time
            models.UniqueConstraint(
                fields=['timetable', 'day', 'time_slot', 'teacher'],
                condition=models.Q(specific_date__isnull=True),
                name='unique_teacher_recurring_slot'
            ),
            # Ensure we don't double-book a classroom at the same time
            models.UniqueConstraint(
                fields=['timetable', 'day', 'time_slot', 'classroom'],
                condition=models.Q(specific_date__isnull=True, classroom__isnull=False),
                name='unique_classroom_recurring_slot'
            ),
            # Ensure we don't schedule the same stream twice at once
            models.UniqueConstraint(
                fields=['timetable', 'day', 'time_slot', 'stream'],
                condition=models.Q(specific_date__isnull=True),
                name='unique_stream_recurring_slot'
            ),
            # Same constraints for specific dates
            models.UniqueConstraint(
                fields=['timetable', 'specific_date', 'time_slot', 'teacher'],
                condition=models.Q(specific_date__isnull=False),
                name='unique_teacher_specific_slot'
            ),
            models.UniqueConstraint(
                fields=['timetable', 'specific_date', 'time_slot', 'classroom'],
                condition=models.Q(specific_date__isnull=False, classroom__isnull=False),
                name='unique_classroom_specific_slot'
            ),
            models.UniqueConstraint(
                fields=['timetable', 'specific_date', 'time_slot', 'stream'],
                condition=models.Q(specific_date__isnull=False),
                name='unique_stream_specific_slot'
            ),
        ]

