# votre_application/models.py

from django.db import models

class Client(models.Model):
    nom = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    telephone = models.CharField(max_length=20)
    email = models.EmailField()
    class Meta:
        db_table = 'Client'

class Patient(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    date_naissance = models.DateField()
    class Meta:
        db_table = 'Patient'
  

from django.db import models

class Commande(models.Model):
    STATUT_CHOICES = [
        ('en_attente', 'En attente'),
        ('en_cours', 'En cours'),
        ('complete', 'Complété'),
        ('refuse', 'Refusé'),
    ]
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_commande = models.DateField()
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='en_attente')
    class Meta:
        db_table = 'Commande'  # Assurez-vous que le nom de la table est en minuscules
