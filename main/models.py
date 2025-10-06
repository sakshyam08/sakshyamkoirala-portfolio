from django.db import models
from django.core.validators import URLValidator


class Skill(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=[
        ('programming', 'Programming'),
        ('design', 'Design'),
        ('networking', 'Networking'),
        ('system', 'System Administration'),
        ('other', 'Other'),
    ])
    proficiency = models.IntegerField(default=80, help_text="Proficiency level (0-100)")
    icon = models.CharField(max_length=50, blank=True, help_text="Font Awesome icon class")
    
    class Meta:
        ordering = ['category', 'name']
    
    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    short_description = models.CharField(max_length=300, blank=True)
    tech_stack = models.CharField(max_length=500, help_text="Comma-separated technologies")
    github_url = models.URLField(blank=True, validators=[URLValidator()])
    live_url = models.URLField(blank=True, validators=[URLValidator()])
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-featured', '-created_at']
    
    def __str__(self):
        return self.title
    
    def get_tech_list(self):
        return [tech.strip() for tech in self.tech_stack.split(',')]


class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200)
    start_year = models.IntegerField()
    end_year = models.IntegerField(null=True, blank=True)
    gpa = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    description = models.TextField(blank=True)
    current = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-end_year', '-start_year']
    
    def __str__(self):
        return f"{self.degree} - {self.institution}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Message from {self.name} - {self.subject}"


class PersonalInfo(models.Model):
    name = models.CharField(max_length=100, default="Sakshyam Koirala")
    title = models.CharField(max_length=200, default="Computer Science Student")
    tagline = models.CharField(max_length=300, default="Passionate about technology and innovation")
    bio = models.TextField(default="I am a dedicated Computer Science student with a passion for technology, cybersecurity, and web development. I enjoy exploring new technologies and building innovative solutions.")
    email = models.EmailField(default="sakshyamkoirala67@gmail.com")
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=100, default="Nepal")
    linkedin_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    resume_file = models.FileField(upload_to='resume/', blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    
    def __str__(self):
        return self.name