from django.contrib import admin
from .models import Profile, Education, Project, SkillCategory, Skill, Certification, ContactMessage

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'email', 'phone']
    
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'start_year', 'end_year', 'order']
    list_editable = ['order']
    
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'created_at']
    list_editable = ['order']
    list_filter = ['created_at']
    
@admin.register(SkillCategory)
class SkillCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'order']
    list_editable = ['order']
    
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'order']
    list_editable = ['order']
    list_filter = ['category']
    
@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['title', 'issuer', 'issue_date', 'order']
    list_editable = ['order']
    
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    readonly_fields = ['created_at']
    list_editable = ['is_read']
