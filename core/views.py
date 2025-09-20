from django.shortcuts import render

def home(request):
    """Home page view"""
    return render(request, 'core/home.html')

def about(request):
    """About Us page view"""
    return render(request, 'core/about.html')

def services(request):
    """Our Services page view"""
    return render(request, 'core/services.html')

def team(request):
    """Our Team page view"""
    return render(request, 'core/team.html')

def contact(request):
    """Contact Us page view"""
    return render(request, 'core/contact.html')
