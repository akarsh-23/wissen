from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=10)
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=50)

class Subscriber(models.Model):
    email = models.EmailField(max_length=254, primary_key=True)

class Team(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, primary_key=True)
    phone = models.CharField(max_length=10)
    designation = models.CharField(max_length=30)
    description = models.CharField(max_length=255, blank=True)
    image = models.FileField(upload_to='Team/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Event(models.Model):
    name = models.CharField(max_length=30, blank=True)
    description = models.CharField(max_length=255, blank=True)
    image = models.FileField(upload_to='Event/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Testimonial(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254, primary_key=True)
    phone = models.CharField(max_length=10)
    designation = models.CharField(max_length=30)
    description = models.CharField(max_length=255, blank=True)
    image = models.FileField(upload_to='Testimonial/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

# class Content(models.Model):
#     aboutus = models.TextField(max_length=500)
#     whatwedo = models.TextField(max_length=500)
#     technicalevents = models.TextField(max_length=500)
#     culturalevents = models.TextField(max_length=500)
#     socialevents = models.TextField(max_length=500)
#     talkshows = models.TextField(max_length=500)
#     events = models.TextField(max_length=500)
#     meettheteam = models.TextField(max_length=500)