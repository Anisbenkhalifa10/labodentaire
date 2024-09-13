from django.shortcuts import render
from .models import Client, Patient, Commande
from datetime import date, timedelta 
from django.shortcuts import render
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommandeForm
from .forms import ClientForm
from .forms import PatientForm
def dashbord(request):
    # Obtenez les données nécessaires pour le tableau de bord
    commandes_aujourd_hui = Commande.objects.filter(date_commande=date.today()).count()
    commandes_demain = Commande.objects.filter(date_commande=date.today() + timedelta(days=1)).count()
    
    # Ajoutez les autres données dont vous avez besoin ici
    total_commandes = Commande.objects.count()  # Exemple
    total_clients = Client.objects.count()      # Assurez-vous d'importer le modèle Client
    total_patients = Patient.objects.count()    # Assurez-vous d'importer le modèle Patient
    
    commandes_statut = {
        'en_attente': Commande.objects.filter(statut='en_attente').count(),
        'en_cours': Commande.objects.filter(statut='en_cours').count(),
        'complete': Commande.objects.filter(statut='complete').count(),
        'refusee': Commande.objects.filter(statut='refuse').count(),
    }

    # Passez les données au template
    context = {
        'commandes_aujourd_hui': commandes_aujourd_hui,
        'commandes_demain': commandes_demain,
        'total_commandes': total_commandes,
        'total_clients': total_clients,
        'total_patients': total_patients,
        'commandes_statut': commandes_statut,
        'commandes_recentes': Commande.objects.order_by('-date_commande')[:10]  # Les 10 commandes récentes
    }
    
    return render(request, 'dashbord.html', context)
def liste_commandes(request):
    # Récupérer les paramètres de recherche et de filtre depuis la requête GET
    search_query = request.GET.get('search', '')
    status_filter = request.GET.get('status', '')

    # Filtrer les commandes en fonction des critères de recherche et de filtre
    commandes = Commande.objects.all()

    if search_query:
        commandes = commandes.filter(
            Q(id__icontains=search_query) |
            Q(client__nom__icontains=search_query) |
            Q(patient__nom__icontains=search_query) |  # Recherche par nom du patient
            Q(patient__prenom__icontains=search_query)  # Recherche par prénom du patient (optionnel)
        )

    if status_filter:
        commandes = commandes.filter(statut=status_filter)

    # Passer les commandes au template
    context = {
        'commandes': commandes,
        'search_query': search_query,
        'status_filter': status_filter,
    }
    return render(request, 'liste_commandes.html', context)

def liste_clients(request):
    clients = Client.objects.all()
    return render(request, 'liste_clients.html', {'clients': clients})

def liste_patients(request):
    patients = Patient.objects.all()
    return render(request, 'liste_patients.html', {'patients': patients})
def modifier_commande(request, id):
    commande = get_object_or_404(Commande, id=id)
    
    if request.method == 'POST':
        form = CommandeForm(request.POST, instance=commande)
        if form.is_valid():
            form.save()
            return redirect('liste_commandes')
    else:
        form = CommandeForm(instance=commande)
    
    return render(request, 'modifier_commande.html', {'form': form, 'commande': commande})
def ajouter_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_clients')
    else:
        form = ClientForm()
    return render(request, 'client_form.html', {'form': form, 'title': 'Ajouter un Client'})

def modifier_client(request, id):
    client = get_object_or_404(Client, id=id)
    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('liste_clients')
    else:
        form = ClientForm(instance=client)
    return render(request, 'client_form.html', {'form': form, 'title': 'Modifier le Client'})

def supprimer_client(request, id):
    client = get_object_or_404(Client, id=id)
    if request.method == 'POST':
        client.delete()
        return redirect('liste_clients')
    return render(request, 'confirm_delete.html', {'client': client})
from django.shortcuts import render, get_object_or_404, redirect
from .models import Client

def confirm_delete(request, id):
    # Récupérer le client à supprimer
    client = get_object_or_404(Client, id=id)
    
    # Si la méthode de la requête est POST, supprimer le client
    if request.method == 'POST':
        client.delete()
        return redirect('liste_clients')  # Rediriger vers la liste des clients après suppression
    
    # Sinon, afficher la page de confirmation
    return render(request, 'confirm_delete.html', {'client': client})
def ajouter_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_patients')
    else:
        form = PatientForm()
    return render(request, 'ajouter_patient.html', {'form': form})

# Modifier un patient existant
def modifier_patient(request, id):
    patient = get_object_or_404(Patient, id=id)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect('liste_patients')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'modifier_patient.html', {'form': form})

# Supprimer un patient
def supprimer_patient(request, id):
    patient = get_object_or_404(Patient, id=id)
    if request.method == 'POST':
        patient.delete()
        return redirect('liste_patients')
    return render(request, 'supprimer_patient.html', {'patient': patient})
def home_client(request):
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_commandes')
    else:
        form = CommandeForm()
    return render(request, 'home_client.html', {'form': form})
def commander_view(request):
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_client')  # Redirige vers la page après l'ajout
    else:
        form = CommandeForm()
    
    clients = Client.objects.all()
    patients = Patient.objects.all()
    
    context = {
        'form': form,
        'clients': clients,
        'patients': patients
    }
    return render(request, 'commander.html', context)