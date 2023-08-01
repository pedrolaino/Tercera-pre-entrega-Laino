from django.shortcuts import render, redirect
from .forms import LibroForm, AutorForm, EditorialForm, BusquedaForm
from .models import Libro

def listar_libros(request):
    libros = Libro.objects.all()
    return render(request, 'listar_libros.html', {'libros': libros})

def crear_libro(request):
    if request.method == 'POST':
        form = LibroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_libro')  
    else:
        form = LibroForm()
    return render(request, 'crear_libro.html', {'form': form})

def crear_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_autor')  
    else:
        form = AutorForm()
    return render(request, 'crear_autor.html', {'form': form})

def crear_editorial(request):
    if request.method == 'POST':
        form = EditorialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crear_editorial')  
    else:
        form = EditorialForm()
    return render(request, 'crear_editorial.html', {'form': form})

def buscar_libros(request):
    resultados = []  

    if request.method == 'POST':
        form = BusquedaForm(request.POST)
        if form.is_valid():
            termino_busqueda = form.cleaned_data['termino_busqueda']
            resultados = Libro.objects.filter(titulo__icontains=termino_busqueda)

    else:
        form = BusquedaForm()

    return render(request, 'buscar_libros.html', {'form': form, 'resultados': resultados})
def inicio(request):
    return render(request, 'base.html')