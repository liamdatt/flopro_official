from django.db import models

class SocialMedia(models.Model):
    """Model for social media links"""
    PLATFORM_CHOICES = [
        ('linkedin', 'LinkedIn'),
        ('instagram', 'Instagram'),
        ('youtube', 'YouTube'),
        ('twitter', 'Twitter'),
        ('facebook', 'Facebook'),
    ]

    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES, unique=True)
    url = models.URLField()
    icon_class = models.CharField(max_length=50, help_text="CSS class for the icon")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.get_platform_display()}"

    class Meta:
        verbose_name = "Social Media"
        verbose_name_plural = "Social Media"


class TeamMember(models.Model):
    """Model for team members"""
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    bio = models.TextField()
    # image = models.ImageField(upload_to='team/', blank=True, null=True)  # Commented out until Pillow is installed
    linkedin_url = models.URLField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0, help_text="Display order")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['order', 'name']


class Service(models.Model):
    """Model for services offered"""
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon_class = models.CharField(max_length=50, help_text="CSS class for the icon", blank=True)
    is_featured = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0, help_text="Display order")
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['order', 'title']


class CompanyInfo(models.Model):
    """Model for company information"""
    name = models.CharField(max_length=100, default="FloPro")
    tagline = models.CharField(max_length=200, default="Automate your workflows")
    description = models.TextField()
    address = models.TextField(default="161 Constant Spring Road, Kingston 8, Jamaica")
    phone = models.CharField(max_length=20, default="+1 (876) 824-2268")
    email = models.EmailField(default="autom8@floproja.com")
    youtube_video_id = models.CharField(max_length=20, blank=True, help_text="YouTube video ID for homepage")
    about_content = models.TextField(blank=True)
    contact_content = models.TextField(blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Company Information"
        verbose_name_plural = "Company Information"


class Contact(models.Model):
    """Model for contact form submissions"""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    company = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)

    SERVICE_CHOICES = [
        ('rpa', 'Robotic Process Automation (RPA)'),
        ('analytics', 'Data Analytics & Business Intelligence'),
        ('training', 'Professional Training & Certification'),
        ('accounting', 'Accounting & Business Filing Automation'),
        ('consultation', 'Strategic Automation Consultation'),
        ('other', 'Other Services'),
    ]
    service = models.CharField(max_length=20, choices=SERVICE_CHOICES, blank=True, null=True)

    TIMELINE_CHOICES = [
        ('immediate', 'Immediately'),
        ('1-3months', 'Within 1-3 months'),
        ('3-6months', 'Within 3-6 months'),
        ('planning', 'Still planning'),
    ]
    timeline = models.CharField(max_length=20, choices=TIMELINE_CHOICES, blank=True, null=True)

    message = models.TextField()
    newsletter = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"

    class Meta:
        ordering = ['-submitted_at']
