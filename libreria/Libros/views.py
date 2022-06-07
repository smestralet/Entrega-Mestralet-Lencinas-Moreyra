from django.shortcuts import render
from django.urls import reverse
from .models import Editorial, Libros, Locales
from django.views.generic import CreateView

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


class Crear_libro(CreateView):
    model = Libros
    template_name = 'crear_libros.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('libros')


class Crear_local(CreateView):
    model = Locales
    template_name = 'crear_locales.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse ('locales')