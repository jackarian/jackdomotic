from django.urls import path
from django.views.generic import TemplateView

from .views import Prenotazioni, GestionePrenotazione, GestioneRisorse

urlpatterns = [
    path('gestione-prenotazione/', GestionePrenotazione.as_view(), name="prenota"),
    path('gestione-risorse/', GestioneRisorse.as_view(), name="gestione-risorse"),
]
