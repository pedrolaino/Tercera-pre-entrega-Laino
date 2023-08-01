"""
URL configuration for miproyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('libros/', views.listar_libros, name='listar_libros'),
    path('crear_libro/', views.crear_libro, name='crear_libro'),
    path('crear_autor/', views.crear_autor, name='crear_autor'),
    path('crear_editorial/', views.crear_editorial, name='crear_editorial'),
    path('buscar_libros/', views.buscar_libros, name='buscar_libros'),
    path('', views.inicio, name='inicio'),
  
]
