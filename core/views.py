import logging

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from .models import Contact, CompanyInfo


logger = logging.getLogger(__name__)

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
    if request.method == 'POST':
        # Get form data
        first_name = request.POST.get('firstName', '').strip()
        last_name = request.POST.get('lastName', '').strip()
        email = request.POST.get('email', '').strip()
        company = request.POST.get('company', '').strip()
        phone = request.POST.get('phone', '').strip()
        service = request.POST.get('service', '').strip()
        timeline = request.POST.get('timeline', '').strip()
        message = request.POST.get('message', '').strip()
        newsletter = request.POST.get('newsletter') == 'on'

        # Basic validation for required fields
        if not all([first_name, last_name, email, message]):
            messages.error(request, 'Please fill in all required fields.')
            return redirect('core:contact')

        # Save to database
        contact_submission = Contact.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            company=company if company else None,
            phone=phone if phone else None,
            service=service if service else None,
            timeline=timeline if timeline else None,
            message=message,
            newsletter=newsletter
        )

        # Get company email from CompanyInfo model
        try:
            company_info = CompanyInfo.objects.first()
            business_email = 'flowproja@gmail.com'
        except:
            business_email = 'flowproja@gmail.com'

        # Prepare email content
        subject = "FloPro Website New Lead"
        email_message = f"""
New contact form submission from FloPro website:

Name: {first_name} {last_name}
Email: {email}
Company: {company or 'Not provided'}
Phone: {phone or 'Not provided'}
Service of Interest: {dict(Contact.SERVICE_CHOICES).get(service, 'Not specified')}
Project Timeline: {dict(Contact.TIMELINE_CHOICES).get(timeline, 'Not specified')}
Newsletter Subscription: {'Yes' if newsletter else 'No'}

Message:
{message}

Submitted at: {contact_submission.submitted_at}
"""

        email_config = {
            'EMAIL_HOST': getattr(settings, 'EMAIL_HOST', None),
            'EMAIL_HOST_USER': getattr(settings, 'EMAIL_HOST_USER', None),
            'EMAIL_HOST_PASSWORD': getattr(settings, 'EMAIL_HOST_PASSWORD', None),
        }

        missing_config = [key for key, value in email_config.items() if not value]
        if missing_config:
            logger.error('Cannot send contact email; missing settings: %s', ', '.join(missing_config))
            messages.error(
                request,
                'Email configuration is incomplete. Please contact support directly while we resolve the issue.'
            )
        else:
            try:
                # Send email
                send_mail(
                    subject=subject,
                    message=email_message,
                    from_email=settings.EMAIL_HOST_USER,  # Your personal Gmail
                    recipient_list=[business_email],  # Your business email
                    fail_silently=False,
                )
                messages.success(request, 'Thank you for your message! We\'ll get back to you within 24 hours.')
            except Exception:
                logger.exception('Failed to send contact email')
                if getattr(settings, 'DEBUG', False):
                    raise
                messages.error(request, 'There was an error sending your message. Please try again or contact us directly.')

        return redirect('core:contact')

    return render(request, 'core/contact.html')

def eula(request):
    """End User License Agreement page view"""
    return render(request, 'core/eula.html')

def privacy(request):
    """Privacy Policy page view"""
    return render(request, 'core/privacy.html')
