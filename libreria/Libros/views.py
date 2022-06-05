from django.shortcuts import render
from .models import Editorial

# Create your views here.

def editoriales(request):
    edits = Editorial.objects.all()


