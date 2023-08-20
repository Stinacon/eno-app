from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
MEDIUM_CHOICES = (
    ('clay', 'ceramics'),
    ('wood', 'wood'),
    ('paint', 'paint'),
    ('drawing', 'drawing'),
    ('textile', 'textile'),
)


class User(AbstractUser):
    pass


class Participant(models.Model):
    business_name = models.CharField(max_length=150)
    contact_name = models.CharField(max_length=250)
    email = models.EmailField()
    phone = PhoneNumberField(region='US')
    address_street = models.CharField(max_length=300)
    address_city = models.CharField(max_length=300)
    address_state = models.CharField(max_length=2)
    address_zip = models.IntegerField()
    bio = models.TextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    booth_number = models.IntegerField()


class Craft(Participant):
    medium = models.CharField(choices=MEDIUM_CHOICES)

    def __str__(self):
        return self.business_name
