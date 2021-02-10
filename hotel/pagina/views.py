from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from quartos.models import Quarto

def index(request):
    #template = loader.get_template('pagina/index.html')
    #return HttpResponse(template.render())
    return render(request, 'pagina/index.html')

