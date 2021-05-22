from django.db import models

# Create your models here.
class Registration(models.Model):
    event = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    email = models.EmailField(primary_key=True)
    phone = models.BigIntegerField()
    registrationNo = models.BigIntegerField(blank=True)
    college = models.CharField(max_length=50)
    course = models.CharField(max_length=50)