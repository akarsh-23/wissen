from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import * 

urlpatterns = [
    path('', home, name='home'),
    path('Home/', home, name='home'),
    path('form/contact', contactFormView, name='ContactForm'),
    path('form/subscriber', subscriberFormView, name='SubscriberForm'),
    path('ThankYou/', thankYouView, name='ThankYou'),
    path('Events/', event, name='events'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# path('form/testimonial', views.testimonialFormView, name='testimonialFormUpload'),
# path('form/team', views.teamFormView, name='teamFormUpload'),
# path('form/event', views.eventFormView, name='eventFormUpload'),
# path('Team/', views.team, name='events'),
# path('Blog/', views.blog, name='blog'),