from django.contrib import admin

from .models import Libros, Editorial, Locales

# Register your models here.

admin.site.register(Libros)
@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ['nombre']

@admin.site.register(Locales)
class LibrosAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.site.register(Locales)
class LocalesAdmin(admin.ModelAdmin):
    list_display = ['nombre']



