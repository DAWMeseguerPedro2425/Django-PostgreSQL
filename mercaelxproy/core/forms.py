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
        #Disposición de Ciudad según la tabla 2: código (3 columnas), nombre (9 columnas) en la misma fila
        #y provincia en otra fila ocupando todo el ancho
        self.helper.layout = Layout(
            Div(
                Div(Field('codigo'), css_class="col-3"),
                Div(Field('nombre'), css_class="col-9"),
                css_class="row mb-3"
            ),
            Div(
                Div(Field('provincia'), css_class="col-12"),
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
        #Disposición de Distrito según la tabla 2: nombre (6 columnas)
        self.helper.layout = Layout(
            Div(
                Div(Field('nombre'), css_class="col-6"),
                css_class="row mb-3"
            )
        )