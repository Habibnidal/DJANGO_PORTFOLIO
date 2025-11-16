from django.db import models
from django.core.validators import URLValidator

class Profile(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=300)
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    linkedin_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    background_image = models.ImageField(upload_to='backgrounds/', blank=True, null=True)
    
    class Meta:
        verbose_name_plural = "Profile"
    
    def __str__(self):
        return self.name

class Education(models.Model):
    degree = models.CharField(max_length=200)
    institution = models.CharField(max_length=300)
    start_year = models.IntegerField()
    end_year = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-end_year', '-start_year']
        verbose_name_plural = "Education"
    
    def __str__(self):
        return f"{self.degree} - {self.institution}"

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=500, help_text="Comma-separated list of technologies")
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)
    video = models.FileField(upload_to='project_videos/', blank=True, null=True)
    image = models.ImageField(upload_to='project_images/', blank=True, null=True)
    order = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order', '-created_at']
    
    def __str__(self):
        return self.title

class SkillCategory(models.Model):
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='skill_icons/', blank=True, null=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
        verbose_name_plural = "Skill Categories"
    
    def __str__(self):
        return self.name

class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='skill_icons/', blank=True, null=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['category', 'order']
    
    def __str__(self):
        return f"{self.category.name} - {self.name}"

class Certification(models.Model):
    title = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200, blank=True)
    certificate_image = models.ImageField(upload_to='certificates/', blank=True, null=True)
    certificate_file = models.FileField(upload_to='certificates/', blank=True, null=True)
    issue_date = models.DateField(blank=True, null=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order', '-issue_date']
        verbose_name_plural = "Certifications"
    
    def __str__(self):
        return self.title

class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} - {self.subject}"
