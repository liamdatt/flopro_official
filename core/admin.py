from django.contrib import admin
from .models import SocialMedia, TeamMember, Service, CompanyInfo, Contact

@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ['platform', 'url', 'is_active']
    list_filter = ['platform', 'is_active']

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'is_active', 'order']
    list_filter = ['is_active']
    ordering = ['order', 'name']

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_featured', 'is_active', 'order']
    list_filter = ['is_featured', 'is_active']
    ordering = ['order', 'title']

@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ['name', 'tagline']

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'service', 'timeline', 'submitted_at']
    list_filter = ['service', 'timeline', 'newsletter', 'submitted_at']
    search_fields = ['first_name', 'last_name', 'email', 'company']
    readonly_fields = ['submitted_at']
    ordering = ['-submitted_at']
