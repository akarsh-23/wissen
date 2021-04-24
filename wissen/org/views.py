from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import ContactForm,SubscriberForm,TeamForm, EventForm, TestimonialForm
from .models import Event, Team
from django.conf import settings

from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def home(request):
    contact_form = ContactForm()
    subscriber_form = SubscriberForm()
    context = {'ContactForm': contact_form, 'SubscriberForm': subscriber_form }
    return render(request, 'home.html', context)

def event(request):
    data = Event.objects.all()
    media = settings.MEDIA_URL
    subscriber_form = SubscriberForm()
    context = {
        'media': media,
        'data': data,
        'SubscriberForm': subscriber_form 
    }
    return render(request, 'events.html', context)

def team(request):
    data = Team.objects.all()
    media = settings.MEDIA_URL
    context = {
        'media': media,
        'data': data,
    }
    return render(request, 'Team.html', context)

def contactFormView(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        contact_form = ContactForm(request.POST)
        # check whether it's valid:
        if contact_form.is_valid():
            # process the data in form.cleaned_data as required
            new_contact = contact_form.save()
            new_contact.save()
            # redirect to a new URL:
            return HttpResponseRedirect('http://127.0.0.1:8000/ThankYou')

    # if a GET (or any other method) we'll create a blank form
    else:
        return HttpResponseRedirect('http://127.0.0.1:8000/')

def subscriberFormView(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        subscriber_form = SubscriberForm(request.POST)
        # check whether it's valid:
        if subscriber_form.is_valid():
            # process the data in form.cleaned_data as required
            new_subscriber = subscriber_form.save()
            new_subscriber.save()
            # redirect to a new URL:
            return HttpResponseRedirect('http://127.0.0.1:8000/ThankYou')

    # if a GET (or any other method) we'll create a blank form
    else:
        return HttpResponseRedirect('http://127.0.0.1:8000/')

def thankYouView(request):
    subscriber_form = SubscriberForm()
    context = {'SubscriberForm': subscriber_form }
    return render(request, 'thanks.html', context)

def teamFormView(request):
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/')
    else:
        form = TeamForm()
    return render(request, 'upload.html', {
        'form': form
    })

def eventFormView(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/')
    else:
        form = EventForm()
    return render(request, 'upload.html', {
        'form': form
    })

def testimonialFormView(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/')
    else:
        form = TestimonialForm()
    return render(request, 'upload.html', {
        'form': form
    })
