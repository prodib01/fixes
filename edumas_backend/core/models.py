from django.db import models
from accounts.models import UserProfile


class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class School(models.Model):
    SCHOOL_TYPE_CHOICES = (
        ("primary", "Primary School"),
        ("secondary", "Secondary School"),
        ("kindergarten", "Kindergarten"),
        ("university", "University"),
        ("technical", "Technical Institute"),
    )

    CATEGORY_CHOICES = (
        ("mixed", "Mixed"),
        ("girls", "Girls Only"),
        ("boys", "Boys Only"),
    )

    owner = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="owned_schools"
    )
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, unique=True, blank=True, null=True)
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name="schools"
    )
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    logo = models.ImageField(upload_to="school_logos/", blank=True, null=True)
    is_active = models.BooleanField(default=True)
    school_type = models.CharField(max_length=20, choices=SCHOOL_TYPE_CHOICES)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class SchoolSettings(models.Model):
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name="settings"
    )
    setting_key = models.CharField(max_length=100)
    setting_value = models.TextField()
    is_system = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ["school", "setting_key"]

    def __str__(self):
        return f"{self.school.name} - {self.setting_key}"


class AcademicYear(models.Model):
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name="academic_years"
    )
    academic_year = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ["school", "academic_year"]

    def __str__(self):
        return f"{self.school.name} - {self.academic_year}"


class Campus(models.Model):
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name="campuses"
    )
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)
    coordinates = models.DecimalField(
        max_digits=12, decimal_places=8, blank=True, null=True
    )
    code = models.CharField(max_length=50)
    director = models.ForeignKey(
        "academics.Staff",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="directed_campuses",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ["school", "code"]
        verbose_name_plural = "Campuses"

    def __str__(self):
        return f"{self.school.name} - {self.name}"


class ClassRoom(models.Model):
    campus = models.ForeignKey(
        Campus, on_delete=models.CASCADE, related_name="classrooms"
    )
    name = models.CharField(max_length=100)
    sitting_capacity = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ["campus", "name"]

    def __str__(self):
        return f"{self.campus.name} - {self.name}"


class Department(models.Model):
    DEPARTMENT_TYPE_CHOICES = (
        ("academic", "Academic"),
        ("administrative", "Administrative"),
        ("support", "Support"),
    )

    campus = models.ForeignKey(
        Campus, on_delete=models.CASCADE, related_name="departments"
    )
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50)
    type = models.CharField(max_length=20, choices=DEPARTMENT_TYPE_CHOICES)
    description = models.TextField(blank=True, null=True)
    head_of_department = models.ForeignKey(
        "academics.Staff",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="headed_departments",
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ["campus", "code"]

    def __str__(self):
        return f"{self.campus.name} - {self.name}"


class Event(models.Model):
    AUDIENCE_CHOICES = (
        ("staff", "Staff"),
        ("students", "Students"),
        ("parents", "Parents"),
        ("all", "All"),
    )

    campus = models.ForeignKey(Campus, on_delete=models.CASCADE, related_name="events")
    title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()
    created_by = models.ForeignKey(
        "academics.Staff", on_delete=models.CASCADE, related_name="created_events"
    )
    audience = models.CharField(max_length=20, choices=AUDIENCE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.campus.name} - {self.title}"
