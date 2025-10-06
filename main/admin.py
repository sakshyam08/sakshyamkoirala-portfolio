from django.contrib import admin
from .models import Skill, Project, Education, ContactMessage, PersonalInfo


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency']
    list_filter = ['category']
    search_fields = ['name']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured', 'created_at']
    list_filter = ['featured', 'created_at']
    search_fields = ['title', 'description']
    prepopulated_fields = {'short_description': ('description',)}


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'start_year', 'end_year', 'current']
    list_filter = ['current', 'start_year']
    search_fields = ['degree', 'institution']


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'read']
    list_filter = ['read', 'created_at']
    search_fields = ['name', 'email', 'subject']
    readonly_fields = ['created_at']


@admin.register(PersonalInfo)
class PersonalInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'email']
    search_fields = ['name', 'title']