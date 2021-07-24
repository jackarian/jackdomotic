from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
# Create your views here.

from django.views import generic
from django.http import Http404, JsonResponse
from django.views.generic import TemplateView
from django.views.generic.list import BaseListView


class Prenotazioni(TemplateView):
    template_name = "control/index.html"


class GestionePrenotazione(TemplateView):
    template_name = "control/gestione_prenotazione.html"


class GestioneRisorse(TemplateView):
    template_name = "control/gestione_risorse.html"
