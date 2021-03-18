from django.contrib import admin
from .models import Contact, Subscriber, Team, Event, Testimonial 

# Register your models here.
admin.site.register(Contact)
admin.site.register(Subscriber)
admin.site.register(Team)
admin.site.register(Event)
admin.site.register(Testimonial)