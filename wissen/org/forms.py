from django.forms import ModelForm
from .models import Contact, Subscriber, Team, Event, Testimonial
from django import forms
class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Email'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Phone'}),
            'subject': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Message'}),
        }

class SubscriberForm(ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder': 'example@email.com'}),
        }

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'email', 'phone', 'description', 'designation', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Email'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Phome'}),
            'designation': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Name'}),
            'description': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Name'}),
            'image': forms.FileInput(attrs={'class': 'form-control','placeholder': 'Email'}),
        }

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Name'}),
            'description': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Name'}),
            'image': forms.FileInput(attrs={'class': 'form-control','placeholder': 'Email'}),
        }

class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'email', 'phone', 'designation', 'description', 'image']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Email'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Phome'}),
            'designation': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Name'}),
            'description': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Name'}),
            'image': forms.FileInput(attrs={'class': 'form-control','placeholder': 'Email'}),
        }