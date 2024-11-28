from django import forms
from .models import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field


#----UD7.3.a-----
# Creacion de forms de provincia ,ciudad y distrito
class ProvinciaForm(forms.ModelForm):
    class Meta:
        model = Provincia
        fields = '__all__'

    #----UD7.4.c----
    # Formulario para provincia con crispy
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        #----UD7.4.d----
        #Disposición de Provincia según la tabla 2: código (3 columnas) y nombre (9 columnas) en la misma fila
        self.helper.layout = Layout(
            Div(
                Div(Field('codigo'), css_class="col-3"),
                Div(Field('nombre'), css_class="col-9"),
                css_class="row mb-3"
            )
        )

class CiudadForm(forms.ModelForm):
    class Meta:
        model = Ciudad
        fields = '__all__'

    #----UD7.4.c----
    # Formulario para ciudad con crispy
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        #----UD7.4.d----
        #Disposición de Ciudad según la tabla 2: provincia en fila completa, código (3 columnas) y nombre (9 columnas) en la misma fila
        self.helper.layout = Layout(
            Div(Field('provincia'), css_class="mb-3"),
            Div(
                Div(Field('codigo'), css_class="col-3"),
                Div(Field('nombre'), css_class="col-9"),
                css_class="row mb-3"
            )
        )

class DistritoForm(forms.ModelForm):
    class Meta:
        model = Distrito
        fields = '__all__'

    #----UD7.4.c----
    # Formulario para distrito con crispy
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        #----UD7.4.d----
        #Disposición de Distrito según la tabla 2: nombre y ciudad (6 columnas cada uno) en la misma fila
        self.helper.layout = Layout(
            Div(
                Div(Field('nombre'), css_class="col-6"),
                Div(Field('ciudad'), css_class="col-6"),
                css_class="row mb-3"
            )
        )