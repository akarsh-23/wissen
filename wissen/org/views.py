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
    context = {'ContactForm': contact_form, 'SubscriberForm': subscriber_form }
    return render(request, 'home.html', context)

def event(request):
    try:
        subscriber_form = SubscriberForm()
        context = {
            'media_url': settings.MEDIA_URL,
            'upcomingevents': Event.objects.filter(status=True),
            'pastevents': Event.objects.filter(status=False),
            'SubscriberForm': subscriber_form 
        }
        return render(request, 'events.html', context)
    except:
        return redirect('http://127.0.0.1:8000/')

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
                return HttpResponseRedirect('http://127.0.0.1:8000/ThankYou')
            else:
                raise Exception
        else:
            raise Exception        
    except:
        return HttpResponseRedirect('http://127.0.0.1:8000/')

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
                return HttpResponseRedirect('http://127.0.0.1:8000/ThankYou')
            else:
                raise Exception
        else:
            raise Exception
    except:
        return HttpResponseRedirect('http://127.0.0.1:8000/')

def thankYouView(request):
    subscriber_form = SubscriberForm()
    context = {'SubscriberForm': subscriber_form }
    return render(request, 'thanks.html', context)



























# def blog(request):
#     return render(request, 'blog.html')


# def teamFormView(request):
#     if request.method == 'POST':
#         form = TeamForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('http://127.0.0.1:8000/')
#     else:
#         form = TeamForm()
#     return render(request, 'upload.html', {
#         'form': form
#     })

# def eventFormView(request):
#     if request.method == 'POST':
#         form = EventForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('http://127.0.0.1:8000/')
#     else:
#         form = EventForm()
#     return render(request, 'upload.html', {
#         'form': form
#     })

# def testimonialFormView(request):
#     if request.method == 'POST':
#         form = TestimonialForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('http://127.0.0.1:8000/')
#     else:
#         form = TestimonialForm()
#     return render(request, 'upload.html', {
#         'form': form
#     })

# def team(request):
#     data = Team.objects.all()
#     media = settings.MEDIA_URL
#     context = {
#         'media': media,
#         'data': data,
#     }
#     return render(request, 'Team.html', context)
