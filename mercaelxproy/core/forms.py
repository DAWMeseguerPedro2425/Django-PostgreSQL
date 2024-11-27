from django import forms
from .models import *


#----UD7.3.a-----
# Creacion de forms de provincia ,ciudad y distrito
class ProvinciaForm(forms.ModelForm):
    class Meta:
        model = Provincia
        fields = '__all__'

class CiudadForm(forms.ModelForm):
    class Meta:
        model = Ciudad
        fields = '__all__'

class DistritoForm(forms.ModelForm):
    class Meta:
        model = Distrito
        fields = '__all__'