from django.shortcuts import redirect, render

from .models import Cerrajero
from .forms import CerrajeroFormulario, CerrajeroBusqueda
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


def crear_cerrajero(request):
    
    if request.method == 'POST':
        form = CerrajeroFormulario(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            cerrajero = Cerrajero(nombre=data['nombre'], apellido=data['apellido'], desempleado=data['desempleado'])
            cerrajero.save()
            # return render(request, "index/plantilla.html", {})
            # return redirect('plantilla')
            return redirect('index')
    
    form = CerrajeroFormulario()
    return render(request, "profesionales/crear_cerrajero.html", {'form': form})

def lista_cerrajeros(request):
    
    nombre_a_buscar = request.GET.get('nombre', None)
    
    if nombre_a_buscar is not None:
        cerrajeros = Cerrajero.objects.filter(nombre__icontains=nombre_a_buscar)
    else:
        cerrajeros = Cerrajero.objects.all()
        
    form = CerrajeroBusqueda()
    return render(request, "profesionales/lista_cerrajeros.html", {'form': form, 'cerrajeros': cerrajeros})

class DetalleCerrajero(DetailView):
    model = Cerrajero
    template_name = "profesionales/detalle_cerrajero.html"


class EditarCerrajero(UpdateView):
    model = Cerrajero
    success_url = '/profesionales/cerrajeros/'
    fields = ['nombre', 'apellido', 'desempleado']

class BorrarCerrajero(DeleteView):
    model = Cerrajero
    success_url = '/profesionales/cerrajeros/'