from django import forms
from .models import *
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field, HTML


#----UD7.3.a-----
# Creacion de forms de Asociacion, Categoria, Subcategoria y Comercio
class AsociacionForm(forms.ModelForm):
    class Meta:
        model = Asociacion
        fields = '__all__'

    #----UD7.4.c-----
    # Formulario para asociacion con crispy
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        #----UD7.4.d----
        #Disposición de Asociación según la tabla 2: nombre, dirección y ciudad en filas completas, correo y teléfono (6 columnas cada uno) en la misma fila
        self.helper.layout = Layout(
            Div(
                Field('nombre'),
                Field('descripcion'),
                css_class="mb-3"
            ),
            HTML('<hr>'),
            Div(
                Div(Field('telefono'), css_class="col-6"),
                Div(Field('correo_electronico'), css_class="col-6"),
                css_class="row mb-3"
            ),
            Div(
                Field('direccion'),
                Field('web'),
                css_class="mb-3"
            )
        )

    #----UD7.3.b-----
    # Clean para telefono y correo electronico
    def clean(self):
        cleaned_data = super().clean()
        telefono = cleaned_data.get('telefono')
        correo_electronico = cleaned_data.get('correo_electronico')

        if telefono and (not telefono.isdigit() or len(telefono) != 9):
            self.add_error('telefono', 'El número de teléfono debe tener 9 dígitos.')
        if correo_electronico:
            try:
                validate_email(correo_electronico) # validate_email importacion que valida un email
            except ValidationError:
                self.add_error('correo_electronico', 'Introduzca un correo electrónico válido.')

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

    #----UD7.4.c-----
    # Formulario para categoria con crispy
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        #----UD7.4.d----
        #Disposición de Categoría según la tabla 2: código (3 columnas) y nombre (9 columnas) en la misma fila
        self.helper.layout = Layout(
            Div(
                Field('nombre'),
                Field('descripcion'),
                css_class="mb-3"
            )
        )

class SubcategoriaForm(forms.ModelForm):
    class Meta:
        model = Subcategoria
        fields = '__all__'

    #----UD7.4.c-----
    # Formulario para subcategoria con crispy
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        #----UD7.4.d----
        #Disposición de Subcategoría según la tabla 2: categoría en fila completa, código (3 columnas) y nombre (9 columnas) en la misma fila
        self.helper.layout = Layout(
            Div(
                Field('categoria'),
                Field('nombre'),
                Field('descripcion'),
                css_class="mb-3"
            )
        )

class ComercioForm(forms.ModelForm):
    class Meta:
        model = Comercio
        fields = '__all__'

    #----UD7.4.c-----
    # Formulario para comercio con crispy
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_tag = False
        #----UD7.4.d----
        #Disposición de Comercio según la tabla 2: nombre y descripción en fila completa, correo y teléfono (6 columnas cada uno), dirección y web (6 columnas cada uno) en la misma fila
        self.helper.layout = Layout(
            Div(
                Field('nombre'),
                Field('descripcion'),
                css_class="mb-3"
            ),
            HTML('<hr>'),
            Div(
                Div(Field('telefono'), css_class="col-6"),
                Div(Field('correo_electronico'), css_class="col-6"),
                css_class="row mb-3"
            ),
            Div(
                Field('direccion'),
                Field('web'),
                css_class="mb-3"
            ),
            HTML('<hr>'),
            Div(
                Div(Field('asociacion'), css_class="col-6"),
                Div(Field('subcategoria'), css_class="col-6"),
                css_class="row mb-3"
            ),
            Div(
                Field('imagen'),
                css_class="mb-3"
            )
        )

    #----UD7.3.b-----
    # Clean para telefono y correo electronico
    def clean(self):
        cleaned_data = super().clean()
        telefono = cleaned_data.get('telefono')
        correo_electronico = cleaned_data.get('correo_electronico')

        if telefono and (not telefono.isdigit() or len(telefono) != 9):
            self.add_error('telefono', 'El número de teléfono debe tener 9 dígitos.')

        if correo_electronico:
            try:
                validate_email(correo_electronico)# validate_email importacion que valida un email
            except ValidationError:
                self.add_error('correo_electronico', 'Introduzca un correo electrónico válido.')