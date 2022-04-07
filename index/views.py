from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from .forms import NuestroUserForm


def index(request):
    return render(request, 'index/index.html', {})

def plantilla(request):
    datos = {
        'lista': ['primero', 'segundo', 'tercero'],
        'nombre': 'Gael',
        'apellido': 'Fort'
    }
    return render(request, 'index/plantilla.html', datos)

def mi_login (request):
    
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
        
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request,user)
                return redirect ('index')
            else:
                return render(request, 'index/login.html', {'login_form': login_form, 'msj': 'El usuario no se pudo autenticar'})
        else:
           return render(request, 'index/login.html', {'login_form': login_form, 'msj': 'El formulario no es válido'})
    
    login_form = AuthenticationForm()
    return render(request,'index/login.html', {'login_form': login_form})

def registrarse(request):
    
    if request.method == 'POST':
        form = NuestroUserForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            # return render(request,'index/index.html', {'msj': f'Se creó correctamente el usuario {username}' })
            return redirect ('login')
        else:
            return render (request, 'index/registrarse.html',{'form':form, 'mjs':'El formulario no es válido'})
            
    
    form = NuestroUserForm()
    
    return render (request, 'index/registrarse.html',{'form':form})