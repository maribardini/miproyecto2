from http.client import HTTPResponse
from django.http import HttpResponse, HttpResponseBadRequest
from django.template import loader


# Create your views here.

def index(request):
    return HttpResponse('<h1>Bienvenidos a mi pagina de Django</h1>')

def plantilla(request):
    
    template = loader.get_template('plantilla.html')
    
    plantilla_generada = template.render({})
    
    return HttpResponse(plantilla_generada)