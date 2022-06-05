from django.contrib import admin

from .models import Libros, Editorial, Locales

# Register your models here.

admin.site.register(Libros)
admin.site.register(Editorial)
admin.site.register(Locales)
