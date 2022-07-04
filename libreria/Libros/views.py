from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Editorial, Libros, Locales
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth.decorators import login_required

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

def detalle_libro(request, pk):
    try:
        libro = Libros.objects.get(id=pk)
        context = {'libro':libro}
        return render(request, 'libro_detalle.html', context=context)
    except:
        context={'error':'El libro no existe'}
        return render(request,'libros.html', context=context)

@login_required
def eliminar_libro(request, pk):
    try:
        if request.method == 'GET':
            libro = Libros.objects.get(id=pk)
            context = {'libro':libro}
        else:
            libro = Libros.objects.get(id=pk)
            libro.delete()
            context = {'message':'Libro eliminado correctamente'}
        return render(request, 'eliminar_libro.html', context=context)
    except:
        context={'error':'El libro no existe'}
        return render(request,'eliminar_libro.html', context=context)

class Crear_libro(LoginRequiredMixin, CreateView):   #LoginRequiredMixin lo dejé acá no más. FALTA REVISAR CON EL SERVER CORRIENDO, si es necesario en las otras class.
    model = Libros
    template_name = 'crear_libros.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse('libros')

class Editar_libro(UpdateView):
    model = Libros
    template_name =  'editar_libro.html'
    fields = ['precio','stock']

    def get_success_url(self):
        return reverse('detalle-libro', kwargs = {'pk':self.object.pk})

class Crear_local(CreateView):
    model = Locales
    template_name = 'crear_locales.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse ('locales')

class Crear_editorial(CreateView):
    model = Editorial
    template_name = 'crear_editoriales.html'
    fields = '__all__'

    def get_success_url(self, request):          #acá, probando la REESTRICCIÓN MANUAL. Le agregué el request en los parámetros y le identé una sangría adentro
        if request.user.is_authenticated and request.user.is_superuser:       #al RETURN.
            return reverse ('editoriales')
        else:
            return redirect('login')