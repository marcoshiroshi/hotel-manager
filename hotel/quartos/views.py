from django.shortcuts import render
from django.http import HttpResponse
from .models import Quarto
from django.template import loader

def quartos(request):
    template = loader.get_template('quartos/quartos.html')

    lista_quartos = {
        'quartos' : Quarto.objects.all()
    }
    return HttpResponse(template.render(lista_quartos, request))