from django.contrib import admin

from .models import Libros, Editorial, Locales

# Register your models here.

#admin.site.register(Libros)
@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ['nombre']

@admin.register(Libros)
class LibrosAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Locales)
class LocalesAdmin(admin.ModelAdmin):
    list_display = ['nombre']



