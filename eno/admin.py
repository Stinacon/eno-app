from django.contrib import admin
from .models import User, Participant, Craft
# Register your models here.
admin.site.register(User)
admin.site.register(Participant)
admin.site.register(Craft)
