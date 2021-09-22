from django.forms import widgets
from gestionBarco.models import Barco
from django import forms
from . models import Barco, Tripulante

class CrearBarcoForm(forms.ModelForm):
    
    class Meta:
        model = Barco
        fields = "__all__"
        exclude = ['desembarque']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'embarque': forms.TextInput(attrs={'class': 'form-control'})
        }

class CrearTriulanteForm(forms.ModelForm):
    class Meta:
        model = Tripulante
        fields = "__all__"
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'cargo': forms.TextInput(attrs={'class': 'form-control'}),
            'grupo': forms.Select(attrs={'class': 'form-control'}),
            'barco': forms.Select(attrs={'class': 'form-control'})
        }

class CrearTriulanteInBarcoForm(forms.ModelForm):
    class Meta:
        model = Tripulante
        fields = "__all__"
        exclude = ['barco']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'cargo': forms.TextInput(attrs={'class': 'form-control'}),
            'grupo': forms.Select(attrs={'class': 'form-control'}),
        }