from django.urls import path
from .views import editoriales, libros, buscar_libros, crear_libros, locales

urlpatterns = [
    path('libros/', libros, name = 'libros'),
    path('editoriales/', editoriales, name = 'editoriales'),
    path('locales/', locales, name = 'locales'),
    path('buscar-libros/', buscar_libros, name = 'buscar-libros'),
    path('crear-libros/', crear_libros, name = 'create-libros'),
    
]