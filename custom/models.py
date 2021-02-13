from enum import Enum

from django.db import models

# Create your models here.
from django.utils import timezone

from client.models import Client


secteur_type = [('IMM', 'IMM'),
                ('DCM', 'DCM'),
                ('Rubber', 'Rubber'),
                ('E-BLW', 'E-BLW'),
                ('Inj-BLW', 'Inj-BLW'),
                ('Mould', 'Mould'),
                ('autre', 'autre')]

demande_type = [('fiabilité', 'fiabilité'),
                ('planification budgétaire', 'planification budgétaire'),
                ('devis', 'devis')]


class DemandeChoice(Enum):
    FI = 'fiabilité'
    PB = 'planification budgétaire'
    DV = 'devis'


class CheckList(models.Model):
    entreprise = models.ForeignKey(Client, related_name='client_checklists', on_delete=models.CASCADE)
    contact = models.CharField(max_length=255)
    poste = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    email = models.EmailField(blank=True)
    adresse = models.CharField(max_length=255)
    date = models.DateTimeField(default=timezone.now)
    reference = models.CharField(max_length=255)
    pilote = models.CharField(max_length=255)
    projet = models.CharField(max_length=255)
    secteur = models.CharField(max_length=10, choices=secteur_type)
    secteur_autre = models.CharField(max_length=255, blank=True)
    know_afc_industry = models.BooleanField(default=False)
    know_afc_yizumi = models.BooleanField(default=False)
    know_afc_tongda = models.BooleanField(default=False)
    etat_societe = models.CharField(max_length=255)
    nombre_machine = models.CharField(max_length=255)
    marques = models.CharField(max_length=255)
    type_demande = models.CharField(max_length=100, choices=demande_type)



