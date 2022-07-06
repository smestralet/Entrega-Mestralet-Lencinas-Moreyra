
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth.models import User
from .forms import Editar_perfil
from django.contrib.auth.decorators import login_required

from libreria.forms import User_Register_Form

def login_view(request):
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username = username, password = password)
            if user is not None: 
                login(request, user)
                context = {'message': f'Bienvenido {username}' }
                return render(request, 'index.html', context = context)
            else:
                context = {'error': 'El usuario ingresado no existe.'}
                form = AuthenticationForm()
                return render(request, 'auth/login.html', context = context)
        else:
            errors = form.errors
            form = AuthenticationForm()
            context = {'errors': errors, 'form': form}
            return render(request, 'auth/login.html', context = context)

    else:
        form = AuthenticationForm()
        context = {'form': form}
        return render (request, 'auth/login.html', context = context)

def logout_view(request):
    logout(request)
    return redirect('inicio')

def inicio(request):
    return render(request, 'index.html')

def register_view(request):
    if request.method == 'POST':
        form = User_Register_Form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            context = {'message': f'El usuario {username} fué creado con éxito.'}
            return render(request, 'index.html', context = context)
        else:
            errors = form.errors
            form = User_Register_Form()
            context = {'errors': errors, 'form': form}
            return render(request, 'auth/register.html', context = context)
    else:
        form = User_Register_Form()
        context = {'form': form}
        return render(request, 'auth/register.html', context = context)

@login_required  
def perfil(request):
    current_user = request.user
    user_id = current_user.id

    user_info = User.objects.get(id=user_id)
    context = {
        "user_info": user_info,
    }
    return render(request, 'perfil.html', context=context)

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = Editar_perfil(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect ('perfil')
    else:
        form = Editar_perfil(instance=request.user)
        args = {'form':form}
        return render(request, 'editar_perfil.html', args)
