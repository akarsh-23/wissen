from django.shortcuts import redirect, render
from django.conf import settings
from .forms import *
from org import models


def home(request):
    try:
        if request.method == "GET" and request.GET.get('Event'):
            event = models.Event.objects.get(name=request.GET.get('Event'))
            if event:
                if event.status:
                    registrationForm = RegistrationForm({'event': request.GET.get('Event')})
                    context = {
                        'media_url' : settings.MEDIA_URL,
                        'RegistrationForm' : registrationForm,
                        'image' : event.image,
                    }
                    return render(request, 'registration/registrations.html', context=context)
                else:
                    registrationForm = RegistrationForm({'event': request.GET.get('Event')})
                    context = {
                        'media_url' : settings.MEDIA_URL,
                        'error' : 'Registration Closed!',
                        'image' : event.image,
                    }
                    return render(request, 'registration/geterror.html', context=context)

        elif request.method == "POST":
            registrationForm = RegistrationForm(request.POST)
            event = models.Event.objects.get(name=request.POST.get('event'))
            if registrationForm.is_valid():
                newresponse = registrationForm.save()
                newresponse.save()
                return redirect('http://127.0.0.1:8000/ThankYou')
            else:
                registrationForm = RegistrationForm(request.POST)
                context = {
                    'media_url' : settings.MEDIA_URL,
                    'RegistrationForm' : registrationForm,
                    'image' : event.image,
                }
                return render(request, 'registration/posterror.html', context=context)
    except:
        return redirect('http://127.0.0.1:8000/Events')
