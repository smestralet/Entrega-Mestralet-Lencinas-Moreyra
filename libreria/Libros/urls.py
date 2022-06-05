from django.urls import path
from .views import editoriales, buscar_libros

urlpatterns = [
    path('editoriales/', editoriales, name = 'editoriales'),
    path('buscar-libros/', buscar_libros, name = 'buscar-libros'),
]