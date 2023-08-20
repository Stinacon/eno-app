from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class User(AbstractUser):
    pass


class Participant(models.Model):
    business_name = models.CharField(max_length=150)
    contact_name = models.CharField(max_length=250)
    email = models.EmailField()
    phone = models.models.PhoneNumberField(_(""))
    address_street = models.CharField(max_length=300)
    address_city = models.CharField(max_length=300)
    address_state = models.CharField(max_length=2)
    address_zip = models.IntegerField(max_length=5)
    bio = models.TextField()
    url = models.URLField(blank=True, null=True)
    booth_number = models.IntegerField(max_length=999)


class Craft(Participant):
    pass
