from django.forms import ModelForm
from .models import *
from django import forms
class RegistrationForm(ModelForm):
    class Meta:
        model = Registration
        fields = ['event','name', 'email', 'phone', 'registrationNo', 'college', 'course']
        widgets = {
            'event': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Event*', 'type':'hidden'}),
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Name*'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Email*'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Phone*', 'type':'tel'}),
            'registrationNo': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Registration No.'}),
            'college': forms.TextInput(attrs={'class': 'form-control','placeholder': 'College*'}),
            'course': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Course*'}),
        }

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['event','status', 'image']
        widgets = {
            'event': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Event*'}),
            'status': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Status*'}),
            'image': forms.FileInput(attrs={'class': 'form-control','placeholder': 'Poster*'}),
        }