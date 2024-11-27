from django import forms
from .models import *
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


#----UD7.3.a-----
# Creacion de forms de Asociacion, Categoria, Subcategoria y Comercio
class AsociacionForm(forms.ModelForm):
    class Meta:
        model = Asociacion
        fields = '__all__'

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

class SubcategoriaForm(forms.ModelForm):
    class Meta:
        model = Subcategoria
        fields = '__all__'

class ComercioForm(forms.ModelForm):
    class Meta:
        model = Comercio
        fields = '__all__'

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