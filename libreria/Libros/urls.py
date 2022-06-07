from django.urls import path
from .views import editoriales, libros, buscar_libros, Crear_libro, locales, Crear_local

urlpatterns = [
    path('libros/', libros, name = 'libros'),
    path('editoriales/', editoriales, name = 'editoriales'),
    path('locales/', locales, name = 'locales'),
    path('buscar-libros/', buscar_libros, name = 'buscar-libros'),
    path('crear-libros/', Crear_libro.as_view(), name = 'create-libros'),
    path('crear-locales/', Crear_local.as_view(), name = 'crear-locales'),
]