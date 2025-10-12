from django.urls import path
from django.views.generic import RedirectView
from . import views

app_name = 'core'

urlpatterns = [
    path('', RedirectView.as_view(url='/home/', permanent=True), name='home_redirect'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('team/', views.team, name='team'),
    path('contact/', views.contact, name='contact'),
]
