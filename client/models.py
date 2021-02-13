from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Client(models.Model):
    name = models.CharField(_('name'), max_length=255, primary_key=True)
    email = models.EmailField(_('email address'), blank=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    number = models.CharField(_('number'), max_length=255)
