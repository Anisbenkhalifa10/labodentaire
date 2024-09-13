"""
URL configuration for labo_dentaire project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .loginviews import admin_login,logout_view
from . import views

urlpatterns = [
    # ... vos autres routes
     path('', views.home_client, name='home_client'),
     path('login/', admin_login, name='login'),
     path('dashbord/', views.dashbord, name='dashbord'),
    path('commandes/', views.liste_commandes, name='liste_commandes'),
    path('clients/', views.liste_clients, name='liste_clients'),
    path('patients/', views.liste_patients, name='liste_patients'),
     path('logout/', logout_view, name='logout'),
       path('commandes/<int:id>/modifier/', views.modifier_commande, name='modifier_commande'),
      path('clients/', views.liste_clients, name='liste_clients'),
    path('clients/ajouter/', views.ajouter_client, name='ajouter_client'),
    path('clients/modifier/<int:id>/', views.modifier_client, name='modifier_client'),
    path('clients/supprimer/<int:id>/', views.supprimer_client, name='supprimer_client'),
     path('clients/<int:id>/confirm_delete/', views.confirm_delete, name='confirm_delete'),
      path('patients/', views.liste_patients, name='liste_patients'),
    path('patients/ajouter/', views.ajouter_patient, name='ajouter_patient'),
    path('patients/<int:id>/modifier/', views.modifier_patient, name='edit_patient'),
    path('patients/<int:id>/supprimer/', views.supprimer_patient, name='delete_patient'),
     path('commander/', views.commander_view, name='commander'),
]