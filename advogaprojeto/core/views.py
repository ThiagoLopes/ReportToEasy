from django.shortcuts import render, redirect
from django.contrib.auth.forms import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_page # edit for name def login
from django.contrib.auth.decorators import login_required

from core.forms import RegistrarUsuarioForm, LogarForm
from core.models import Usuario

# Create your views here.

@login_required
def index(request):
    usuarios = Usuario.objects.all()
    usuario = Usuario.objects.get(id=request.user.id)
    return render(request, 'index.html',{"usuario" : usuario ,"usuarios" : usuarios})

def login(request):
    if request.method == 'POST':
        form = LogarForm(request.POST)
        dados_form = form.data
        user = authenticate(username = dados_form['username'].lower(), password = dados_form['password'])

        if user is not None:
            login_page(request, user )
            usuario = Usuario.objects.get(id=user.id)
            return redirect('index')

    return render(request, 'login.html')

def log_out(request):
    logout(request)
    return redirect('index')

def registrar(request):

    if request.method =='POST':
        form = RegistrarUsuarioForm(request.POST)
        if form.is_valid():

            dados_form = form.data

            # todo o processo de salvar no bd e criar user
            # criar user
            criar_user = User.objects.create_user(dados_form['nome'].lower(), dados_form['email'].lower(), dados_form['senha'])
            #criar Usuario
            usuario = Usuario(nome=dados_form['nome'].lower(),email=dados_form['email'].lower(), telefone=dados_form['telefone'],user=criar_user)
            #salvar
            usuario.save()
            return redirect('login')
        else:
            return render(request, 'registrar.html', {"form":form})

    return render(request, 'registrar.html')
