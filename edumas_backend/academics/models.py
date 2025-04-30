from django.db import models
from accounts.models import UserProfile
from core.models import School, Department, Campus, ClassRoom


class Staff(models.Model):
    CONTRACT_TYPE_CHOICES = (
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('contract', 'Contract'),
        ('temporary', 'Temporary'),
    )
    
    STAFF_TYPE_CHOICES = (
        ('teaching', 'Teaching Staff'),
        ('non_teaching', 'Non-Teaching Staff'),
        ('administrative', 'Administrative Staff'),
        ('support', 'Support Staff'),
    )
    
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='staff_profile')
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='staff')  # Added for multi-tenancy
    staff_id = models.CharField(max_length=50)
    hire_date = models.DateField()
    contract_type = models.CharField(max_length=20, choices=CONTRACT_TYPE_CHOICES)
    contract_start_date = models.DateField()
    contract_end_date = models.DateField(blank=True, null=True)
    available_days = models.TextField(blank=True, null=True)
    available_hours = models.TextField(blank=True, null=True)
    probation_period = models.CharField(max_length=50, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, related_name='staff_members')
    qualifications = models.TextField(blank=True, null=True)
    experience = models.TextField(blank=True, null=True)
    specialization = models.CharField(max_length=255, blank=True, null=True)
    staff_type = models.CharField(max_length=20, choices=STAFF_TYPE_CHOICES)
    license_number = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ['school', 'staff_id']  # Staff IDs are unique within a school
    
    def __str__(self):
        return f"{self.user.get_full_name()} ({self.staff_id}) - {self.school.name}"


class Subject(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='subjects')
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    credits = models.DecimalField(max_digits=5, decimal_places=2, default=1.0)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='subjects')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ['school', 'code']
        
    def __str__(self):
        return f"{self.name} ({self.code}) - {self.school.name}"


class CampusSubject(models.Model):
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE, related_name='campus_subjects')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='campus_offerings')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['campus', 'subject']
        
    def __str__(self):
        return f"{self.campus.name} - {self.subject.name}"


class Class(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='classes')
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50)
    class_teacher = models.ForeignKey(Staff, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_classes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ['school', 'code']
        verbose_name_plural = 'Classes'
        
    def __str__(self):
        return f"{self.name} ({self.code}) - {self.school.name}"


class ClassSubject(models.Model):
    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='subjects')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='classes')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['class_obj', 'subject']
        
    def __str__(self):
        return f"{self.class_obj.name} - {self.subject.name}"


class ClassCampus(models.Model):
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE, related_name='campus_classes')
    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='campus_offerings')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['campus', 'class_obj']
        verbose_name_plural = 'Class Campus'
        
    def __str__(self):
        return f"{self.campus.name} - {self.class_obj.name}"


class Stream(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True, null=True)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE, related_name='streams')
    class_obj = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='streams')
    room = models.ForeignKey(ClassRoom, on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_streams')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ['class_obj', 'name', 'campus']
        
    def __str__(self):
        return f"{self.class_obj.name} - {self.name} ({self.campus.name})"


class Term(models.Model):
    academic_year = models.ForeignKey('core.AcademicYear', on_delete=models.CASCADE, related_name='terms')
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=False)
    campus = models.ForeignKey(Campus, on_delete=models.CASCADE, related_name='terms')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ['academic_year', 'name', 'campus']
        
    def __str__(self):
        return f"{self.academic_year.academic_year} - {self.name} ({self.campus.name})"


class Student(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='student_profile')
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students')
    student_id = models.CharField(max_length=50)
    admission_date = models.DateField()
    previous_school = models.TextField(blank=True, null=True)
    current_class = models.ForeignKey(Stream, on_delete=models.SET_NULL, null=True, blank=True, related_name='students')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ['school', 'student_id']  # Student IDs are unique within a school
    
    def __str__(self):
        return f"{self.user.get_full_name()} ({self.student_id}) - {self.school.name}"


class ParentGuardian(models.Model):
    RELATIONSHIP_CHOICES = (
        ('father', 'Father'),
        ('mother', 'Mother'),
        ('guardian', 'Guardian'),
        ('other', 'Other'),
    )
    
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='parent_profiles')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='parents_guardians')
    relationship = models.CharField(max_length=20, choices=RELATIONSHIP_CHOICES)
    occupation = models.CharField(max_length=255, blank=True, null=True)
    work_address = models.CharField(max_length=255, blank=True, null=True)
    has_custody = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.get_full_name()} ({self.get_relationship_display()} of {self.student.user.get_full_name()})"


class GradingScale(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='grading_scales')
    letter_grade = models.CharField(max_length=10)
    min_score = models.DecimalField(max_digits=5, decimal_places=2)
    max_score = models.DecimalField(max_digits=5, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ['school', 'letter_grade']
        
    def __str__(self):
        return f"{self.school.name} - {self.letter_grade} ({self.min_score}-{self.max_score})"


class Assessment(models.Model):
    ASSESSMENT_TYPE_CHOICES = (
        ('exam', 'Examination'),
        ('quiz', 'Quiz'),
        ('assignment', 'Assignment'),
        ('project', 'Project'),
        ('practical', 'Practical'),
        ('other', 'Other'),
    )
    
    campus_class = models.ForeignKey(ClassCampus, on_delete=models.CASCADE, related_name='assessments')
    assessment_type = models.CharField(max_length=20, choices=ASSESSMENT_TYPE_CHOICES)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='assessments')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    weight_percentage = models.PositiveIntegerField()
    passing_score = models.PositiveIntegerField()
    assessment_period = models.CharField(max_length=100)
    instructions = models.TextField(blank=True, null=True)
    questions = models.JSONField(blank=True, null=True)
    term = models.ForeignKey(Term, on_delete=models.CASCADE, related_name='assessments')
    created_by = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='created_assessments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title} - {self.subject.name} ({self.get_assessment_type_display()})"


class AssessmentResult(models.Model):
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name='results')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='assessment_results')
    score = models.DecimalField(max_digits=5, decimal_places=2)
    grade = models.CharField(max_length=10)
    graded_by = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name='graded_assessments')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ['assessment', 'student']
        
    def __str__(self):
        return f"{self.student.user.get_full_name()} - {self.assessment.title} - {self.score}"


class ReportCard(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    )
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='report_cards')
    academic_year = models.ForeignKey('core.AcademicYear', on_delete=models.CASCADE, related_name='report_cards')
    term = models.ForeignKey(Term, on_delete=models.CASCADE, related_name='report_cards')
    date = models.DateField()
    gpa = models.DecimalField(max_digits=5, decimal_places=2)
    attendance = models.JSONField()
    teacher_comments = models.TextField(blank=True, null=True)
    director_comments = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ['student', 'academic_year', 'term']
        
    def __str__(self):
        return f"{self.student.user.get_full_name()} - {self.academic_year.academic_year} - {self.term.name}"