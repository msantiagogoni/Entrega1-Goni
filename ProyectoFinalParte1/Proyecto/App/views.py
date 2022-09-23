from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from AppPrimerMVT.models import Familiares

class ListaFamiliares(ListView):
    model = Familiares
    
    def get_context_data(self, **kwargs):
        context = super(ListaFamiliares, self).get_context_data(**kwargs)
        lista_familiares = Familiares.objects.all()
        context['lista_familiares'] = lista_familiares
        return context
