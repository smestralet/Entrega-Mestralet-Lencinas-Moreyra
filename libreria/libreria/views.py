from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm


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
    return redirect('index')







def inicio(request):
    return render(request, 'index.html')