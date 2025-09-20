from django.shortcuts import render, get_object_or_404
from .models import SocialMedia, TeamMember, Service, CompanyInfo

def home(request):
    """Home page view"""
    company_info = CompanyInfo.objects.first()
    social_media = SocialMedia.objects.filter(is_active=True)
    context = {
        'company_info': company_info,
        'social_media': social_media,
    }
    return render(request, 'core/home.html', context)

def about(request):
    """About Us page view"""
    company_info = CompanyInfo.objects.first()
    social_media = SocialMedia.objects.filter(is_active=True)
    context = {
        'company_info': company_info,
        'social_media': social_media,
    }
    return render(request, 'core/about.html', context)

def services(request):
    """Our Services page view"""
    services = Service.objects.filter(is_active=True)
    company_info = CompanyInfo.objects.first()
    social_media = SocialMedia.objects.filter(is_active=True)
    context = {
        'services': services,
        'company_info': company_info,
        'social_media': social_media,
    }
    return render(request, 'core/services.html', context)

def team(request):
    """Our Team page view"""
    team_members = TeamMember.objects.filter(is_active=True)
    company_info = CompanyInfo.objects.first()
    social_media = SocialMedia.objects.filter(is_active=True)
    context = {
        'team_members': team_members,
        'company_info': company_info,
        'social_media': social_media,
    }
    return render(request, 'core/team.html', context)

def contact(request):
    """Contact Us page view"""
    company_info = CompanyInfo.objects.first()
    social_media = SocialMedia.objects.filter(is_active=True)
    context = {
        'company_info': company_info,
        'social_media': social_media,
    }
    return render(request, 'core/contact.html', context)
