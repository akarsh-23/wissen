from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Home/', views.home, name='home'),
    path('form/contact', views.contactFormView, name='ContactForm'),
    path('form/subscriber', views.subscriberFormView, name='SubscriberForm'),
    path('form/team', views.teamFormView, name='teamFormUpload'),
    path('form/event', views.eventFormView, name='eventFormUpload'),
    path('form/testimonial', views.testimonialFormView, name='testimonialFormUpload'),
    path('ThankYou/', views.thankYouView, name='ThankYou'),
    path('Events/', views.event, name='events'),
    path('Team/', views.team, name='events'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)