from django import forms
from .models import Libro, Autor, Editorial

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'

class EditorialForm(forms.ModelForm):
    class Meta:
        model = Editorial
        fields = '__all__'
        
class BusquedaForm(forms.Form):
    termino_busqueda = forms.CharField(label='Buscar')