from django.shortcuts import render
from .models import Editorial, Libros, Locales

def libros(request):
    libros = Libros.objects.all()
    context = {
        'libros' : libros
    }
    return render(request, 'libros.html', context = context)


def editoriales(request):
    edits = Editorial.objects.all()
    context = {
        'editoriales':edits
    }
    return render(request, 'editoriales.html', context=context)


def locales(request):
    locales = Locales.objects.all()
    context = {'locales': locales
    }
    return render (request, 'locales.html', context=context)


def buscar_libros(request):
    print(request.GET)
    libros = Libros.objects.filter(name__icontains = request.GET['Search'])
    context = {'libros':libros}
    return render(request, 'buscar_libros.html', context=context)


def crear_libros(request):
    return render(request, 'crear_libros.html')
