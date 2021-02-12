from django.db import models

# Create your models here.
from django.contrib.auth.models import User

import datetime
from django.utils import timezone

from accounts.models import BaseUser, Right

now = timezone.now()


# Create your models here.


class Service(models.Model):
    nom = models.CharField(max_length=100, primary_key=True)
    # nom_arabe = models.CharField(max_length=100, default="")
    # nom_francais = models.CharField(max_length=100, default="")
    prix = models.FloatField(default=0)

    def __str__(self):
        return self.nom


class Abonnement(models.Model):
    user = models.ForeignKey(BaseUser, related_name="abonnements", on_delete=models.CASCADE)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    services = models.ManyToManyField(Service)
    rights = models.ManyToManyField(Right)
    est_valide = models.BooleanField(default=False)

    @property
    def est_valide(self):
        now = datetime.datetime.now()
        if self.date_debut.date() < now.date() or \
                (self.date_debut.date() == now.date() and
                 self.date_debut.time() <= now.time()) and \
                now.date() < self.date_fin.date() or \
                (now.date() == self.date_fin.date() and
                 now.time() < self.date_fin.time()):
            return True
        else:
            return False

    def __str__(self):
        return "{} {}".format(str(self.user), str(self.date_debut))
