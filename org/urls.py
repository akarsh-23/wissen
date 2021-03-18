from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('form/contact', views.contactFormView, name='ContactForm'),
    path('form/subscriber', views.subscriberFormView, name='SubscriberForm'),
    path('form/team', views.teamFormView, name='teamFormUpload'),
    path('form/event', views.eventFormView, name='eventFormUpload'),
    path('form/testimonial', views.testimonialFormView, name='testimonialFormUpload'),
    path('thankYou', views.thankYouView, name='ThankYou'),
    path('paytm', views.paytm, name='paytm'),
    path('payment', views.payment, name='payment'),
    path('response/', views.response, name='response'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)