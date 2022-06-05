from django.shortcuts import render
from .models import Editorial, Libros, Locales

# Create your views here.

def editoriales(request):
    edits = Editorial.objects.all()
    context = {
        'editoriales':edits
    }
    return render(request, 'editoriales.html', context=context)

def buscar_libros(request):
    print(request.GET)
    libros = Libros.objects.filter(name__icontains = request.GET['Search'])
    context = {'libros':libros}
    return render(request, 'buscar_libros.html', context=context)
