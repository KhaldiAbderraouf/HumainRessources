from django.contrib import admin

# Register your models here.
from .models import Service, Abonnement

admin.site.register(Service)
admin.site.register(Abonnement)