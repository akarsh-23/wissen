from django.contrib import admin
from .models import *

# Register your models here.
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ['event','name','email','phone','registrationNo','college','course']

admin.site.register(Registration, RegistrationAdmin)

