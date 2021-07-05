from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt

from .forms import (ContactForm, EventForm, SubscriberForm, TeamForm,
                    TestimonialForm)
from .models import Event, Team


def home(request):
    contact_form = ContactForm()
    subscriber_form = SubscriberForm()
    context = {'ContactForm': contact_form,
               'SubscriberForm': subscriber_form,
              }
    return render(request, 'home.html', context)

def event(request):
    try:
        if request.GET.get('Category'):
            subscriber_form = SubscriberForm()
            context = {
                'media_url': settings.MEDIA_URL,
                'upcomingevents': Event.objects.filter(status=True),
                'pastevents': Event.objects.filter(status=False, category=request.GET.get('Category', None)),
                'categories': Event.objects.values('category').distinct(),
                'SubscriberForm': subscriber_form,
            }
            return render(request, 'events.html', context)
        else:
            subscriber_form = SubscriberForm()
            context = {
                'media_url': settings.MEDIA_URL,
                'upcomingevents': Event.objects.filter(status=True),
                'pastevents': Event.objects.filter(status=False), 
                'categories': Event.objects.values('category').distinct(),
                'SubscriberForm': subscriber_form,
            }
            return render(request, 'events.html', context)
    except:
        return redirect('../?error=Something went worng!')

def contactFormView(request):
    try:
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            contact_form = ContactForm(request.POST)
            # check whether it's valid:
            if contact_form.is_valid():
                # process the data in form.cleaned_data as required
                new_contact = contact_form.save()
                new_contact.save()
                # redirect to a new URL:
                return HttpResponseRedirect('../ThankYou')
            else:
                raise Exception
        else:
            raise Exception        
    except:
        return HttpResponseRedirect('../')

def subscriberFormView(request):
    try:
        if request.method == 'POST':
            # create a form instance and populate it with data from the request:
            subscriber_form = SubscriberForm(request.POST)
            # check whether it's valid:
            if subscriber_form.is_valid():
                # process the data in form.cleaned_data as required
                new_subscriber = subscriber_form.save()
                new_subscriber.save()
                # redirect to a new URL:
                return HttpResponseRedirect('../ThankYou')
            else:
                raise Exception
        else:
            raise Exception
    except:
        return HttpResponseRedirect('../')

def thankYouView(request):
    subscriber_form = SubscriberForm()
    context = {'SubscriberForm': subscriber_form }
    return render(request, 'thanks.html', context)