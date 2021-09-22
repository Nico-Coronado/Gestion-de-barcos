from django.shortcuts import redirect, render
import datetime
from django.views.generic.edit import DeleteView, UpdateView

from . models import *
from . forms import *

def gestionBarco(request):
    barco = Barco.objects.all()
    form = CrearBarcoForm()
    fecha = ""

    if request.method == 'POST':
        form = CrearBarcoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            embarque = form.cleaned_data['embarque']
            fecha = embarque + datetime.timedelta(days=20)
            barco = Barco(
                nombre = nombre,
                embarque = embarque,
                desembarque = fecha
            )
            barco.save()
            return redirect('gestion-barco')
    context = {'title': 'Gestion del barco - ServiciosSOS', 'listaBarco': barco, 'form': form}
    return render(request, 'gestion_barco.html', context)

def gestionTripulantes(request):
    form = CrearTriulanteForm()
    barco = Barco.objects.all()
    listaTripulante = Tripulante.objects.all()

    if request.method == 'POST':
        form = CrearTriulanteForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'title': 'Gestion de tripulantes - ServiciosSOS',
                'form': form, 'lista': listaTripulante, 'barco': barco}
    return render(request, 'gestion_tripulantes.html', context)

def barcoDetail(request, nombreBarco):
    barco = Barco.objects.get(nombre=nombreBarco)
    lista1 = Tripulante.objects.filter(barco=barco, grupo="1")
    lista2 = Tripulante.objects.filter(barco=barco, grupo="2")
    form = CrearTriulanteInBarcoForm()
    if request.method == 'POST':
        form = CrearTriulanteInBarcoForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            cargo = form.cleaned_data['cargo']
            grupo = form.cleaned_data['grupo']

            tripu = Tripulante(
                nombre = nombre,
                cargo = cargo, 
                grupo = grupo,
                barco = barco
            )
            tripu.save()
            
    context = {'title': f'{nombreBarco} - ServiciosSOS',
                'barco': barco, 'lista1': lista1,'lista2': lista2, 'form': form}
    return render(request, 'barco_detail.html', context)


class BarcoDeleteView(DeleteView):
    model = Barco
    template_name = "crud/delete_barco.html"
    success_url = '/'

class TripulanteDeleteView(DeleteView):
    model = Tripulante
    template_name = "crud/delete_tripulante.html"
    success_url = '/gestion-tripulantes/'

class TripulanteUpdateView(UpdateView):
    model = Tripulante
    form_class = CrearTriulanteForm
    template_name = "crud/update_tripulante.html"
    success_url = "/gestion-tripulantes/"




    

