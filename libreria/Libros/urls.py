from django.urls import path
from .views import editoriales, libros, buscar_libros, Crear_libro, locales, Crear_local, Crear_editorial, detalle_libro, eliminar_libro, Editar_libro, about
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('libros/', libros, name = 'libros'),
    path('editoriales/', editoriales, name = 'editoriales'),
    path('locales/', locales, name = 'locales'),
    path('buscar-libros/', buscar_libros, name = 'buscar-libros'),
    path('detalle-libro/<int:pk>/', detalle_libro, name = 'detalle-libro'),
    path('eliminar-libro/<int:pk>/', eliminar_libro, name = 'eliminar-libro'),
    path('editar-libro/<int:pk>/', Editar_libro.as_view(), name = 'editar-libro'),
    path('crear-libros/', Crear_libro.as_view(), name = 'create-libros'),
    path('crear-locales/', Crear_local.as_view(), name = 'crear-locales'),
    path('crear-editoriales/', Crear_editorial.as_view(), name = 'crear-editoriales'),
    path('about/', about, name = 'about'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)