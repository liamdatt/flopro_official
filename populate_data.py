#!/usr/bin/env python
"""
Script to populate FloPro database with initial data
"""
import os
import sys
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flopro_offical.settings')
django.setup()

from core.models import SocialMedia, TeamMember, Service, CompanyInfo

def populate_data():
    print("Populating FloPro database with initial data...")

    # Create company info
    company_info, created = CompanyInfo.objects.get_or_create(
        name="FloPro",
        defaults={
            'tagline': "Automate your workflows",
            'description': "FloPro is a Jamaica-based automation company focused on streamlining business workflows through Robotic Process Automation (RPA), data analytics, and professional training designed to optimize day-to-day operations.",
            'address': "161 Constant Spring Road, Kingston 8, Jamaica",
            'phone': "+1 (876) 824-2268",
            'email': "autom8@floproja.com",
            'youtube_video_id': "",  # Add YouTube video ID here
            'about_content': """
            <h2 class="text-primary mb-4">Our Mission</h2>
            <p class="lead mb-4">
                FloPro is a Jamaica-based automation company dedicated to streamlining business workflows through innovative technology solutions. We specialize in Robotic Process Automation (RPA), data analytics, and professional training to help organizations optimize their day-to-day operations.
            </p>

            <h3 class="text-warning mb-3">What We Do</h3>
            <div class="row g-4 mb-5">
                <div class="col-md-6">
                    <h5>RPA Implementation</h5>
                    <p>Automate routine, rules-based processes across accounting, client correspondence, and report generation using platforms like Microsoft Power Automate and UiPath.</p>
                </div>
                <div class="col-md-6">
                    <h5>Data Analytics</h5>
                    <p>Transform operational and financial data into actionable insights that drive data-driven decision making and reliable management reporting.</p>
                </div>
                <div class="col-md-6">
                    <h5>Professional Training</h5>
                    <p>Build internal capability with specialized training in automation technologies, workflow optimization, and productivity enhancement.</p>
                </div>
                <div class="col-md-6">
                    <h5>Consulting Services</h5>
                    <p>Expert consultation to identify automation opportunities and design optimal solutions tailored to your business needs.</p>
                </div>
            </div>

            <h3 class="text-warning mb-3">Why Jamaica?</h3>
            <p class="mb-4">
                Based in Kingston, Jamaica, we understand the unique challenges and opportunities facing Caribbean businesses. Our local expertise combined with global best practices allows us to deliver tailored solutions that work in our regional context.
            </p>
            """,
            'contact_content': """
            <p class="mb-4">
                Ready to transform your business operations? Contact us today for a free consultation. Our team of automation experts will work with you to identify opportunities and design solutions that deliver real ROI.
            </p>
            <p class="mb-4">
                <strong>What to expect:</strong>
            </p>
            <ul class="mb-4">
                <li>Free initial consultation</li>
                <li>Process analysis and automation roadmap</li>
                <li>Custom solution design</li>
                <li>Ongoing support and optimization</li>
            </ul>
            """
        }
    )
    if created:
        print("✓ Created company information")
    else:
        print("✓ Company information already exists")

    # Create social media links
    social_media_data = [
        {
            'platform': 'linkedin',
            'url': 'https://linkedin.com/company/flopro',
            'icon_class': 'fab fa-linkedin',
            'is_active': True
        },
        {
            'platform': 'youtube',
            'url': 'https://youtube.com/@flopro',
            'icon_class': 'fab fa-youtube',
            'is_active': True
        },
        {
            'platform': 'twitter',
            'url': 'https://twitter.com/flopro',
            'icon_class': 'fab fa-twitter',
            'is_active': True
        },
        {
            'platform': 'instagram',
            'url': 'https://instagram.com/flopro',
            'icon_class': 'fab fa-instagram',
            'is_active': True
        }
    ]

    for social_data in social_media_data:
        social, created = SocialMedia.objects.get_or_create(
            platform=social_data['platform'],
            defaults=social_data
        )
        if created:
            print(f"✓ Created {social.platform} social media link")
        else:
            print(f"✓ {social.platform} social media link already exists")

    # Create services
    services_data = [
        {
            'title': 'Robotic Process Automation (RPA)',
            'description': 'Automate routine, rules-based processes across common business functions including accounting, client correspondence, and report generation. We provide consulting and implementation services using industry-leading platforms such as Microsoft Power Automate and UiPath.',
            'icon_class': 'fas fa-robot',
            'is_featured': True,
            'order': 1
        },
        {
            'title': 'Data Analytics',
            'description': 'Transform your operational and financial data into actionable insights. Our analytics services help organizations build data-driven cultures and enable faster, more reliable management reporting and decision-making processes.',
            'icon_class': 'fas fa-chart-line',
            'is_featured': True,
            'order': 2
        },
        {
            'title': 'Education & Training',
            'description': 'Build internal capability in automation technologies through our specialized training programs. We focus on practical skills for automating repetitive tasks, streamlining workflows, and improving overall productivity.',
            'icon_class': 'fas fa-graduation-cap',
            'is_featured': True,
            'order': 3
        },
        {
            'title': 'Accounting & Business Filing',
            'description': 'Support for administrative compliance and finance workflows aligned with automation principles. We help streamline accounting processes and ensure regulatory compliance through intelligent automation solutions.',
            'icon_class': 'fas fa-file-invoice-dollar',
            'is_featured': False,
            'order': 4
        }
    ]

    for service_data in services_data:
        service, created = Service.objects.get_or_create(
            title=service_data['title'],
            defaults=service_data
        )
        if created:
            print(f"✓ Created service: {service.title}")
        else:
            print(f"✓ Service already exists: {service.title}")

    # Create team members
    team_data = [
        {
            'name': 'Mark Lewis',
            'title': 'Finance & Technology Professional',
            'bio': 'Mark brings extensive expertise in financial modeling, web development, and operational efficiency through automation. With a passion for leveraging technology to streamline business processes, Mark leads FloPro\'s initiatives in RPA and data analytics.',
            'linkedin_url': 'https://linkedin.com/in/mark-lewis-flopro',
            'order': 1
        }
    ]

    for member_data in team_data:
        member, created = TeamMember.objects.get_or_create(
            name=member_data['name'],
            defaults=member_data
        )
        if created:
            print(f"✓ Created team member: {member.name}")
        else:
            print(f"✓ Team member already exists: {member.name}")

    print("\n🎉 Database populated successfully!")
    print("\nNext steps:")
    print("1. Run 'python manage.py createsuperuser' to create an admin account")
    print("2. Run 'python manage.py runserver' to start the development server")
    print("3. Visit http://127.0.0.1:8000/admin/ to manage content")
    print("4. Visit http://127.0.0.1:8000/ to view the website")

if __name__ == '__main__':
    populate_data()
