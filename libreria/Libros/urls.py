from django.urls import path
from .views import editoriales, libros, buscar_libros, crear_libros

urlpatterns = [
    path('editoriales/', editoriales, name = 'editoriales'),
    path('libros/', libros, name = 'libros'),
    path('buscar-libros/', buscar_libros, name = 'buscar-libros'),
    path('crear-libros/', crear_libros, name = 'create-libros'),
]