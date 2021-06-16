from django.http import request
from django.shortcuts import redirect, render
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout


def home_view(request):
    return render(request, 'home.html', {})


def login_view(request):
    error_message = None
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        # print(form.data)
        if form.is_valid():
            username = form.data.get('username')
            password = form.data.get('password')
            user = authenticate(username=username, password=password)    
            if user is not None:
                login(request, user)
                if request.GET.get('next'):
                    return redirect(request.GET.get('next'))
                else:
                    return redirect('home')

            else:
                error_message = 'Error | Datos incorrectos'
    

    return render(request, 'login.html', {'form':form, 'error_message': error_message})


def logout_view(request):
    logout(request)
    return redirect('home')