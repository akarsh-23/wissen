from django.shortcuts import redirect, render
from django.conf import settings
from .forms import *


def home(request):
    if request.method == "GET" and request.GET.get('Event'):
        event = Event.objects.get(event=request.GET.get('Event'))
        if event:
            print(event.status)
            if event.status:
                registrationForm = RegistrationForm({'event': request.GET.get('Event')})
                context = {
                    'media_url' : settings.MEDIA_URL,
                    'RegistrationForm' : registrationForm,
                    'image' : event.image,
                }
                return render(request, 'registration/registrations.html', context=context)

    elif request.method == "POST":
        registrationForm = RegistrationForm(request.POST)
        if registrationForm.is_valid():
            newresponse = registrationForm.save()
            newresponse.save()
            return redirect('http://127.0.0.1:8000/ThankYou')
    return redirect('http://127.0.0.1:8000')
