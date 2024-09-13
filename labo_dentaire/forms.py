from django import forms
from .models import Commande
from .models import Client
from .models import Patient
class CommandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = ['client', 'patient', 'date_commande', 'statut']
        widgets = {
            'date_commande': forms.DateInput(attrs={'type': 'date'}),
            'statut': forms.Select(choices=Commande.STATUT_CHOICES),
        }
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['nom', 'adresse', 'telephone', 'email']
class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['nom', 'prenom', 'date_naissance']