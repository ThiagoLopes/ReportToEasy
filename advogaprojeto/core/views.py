from django.shortcuts import render, redirect
from django.contrib.auth.forms import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_page  # edit for name def login
from django.contrib.auth.decorators import login_required

from django.template import RequestContext

from core.forms import RegistrarUsuarioForm, LogarForm, TemplateForm
from core.models import Usuario, TemplateFile

# Create your views here.


@login_required
def get_user_logado(request):
    usuario = Usuario.objects.get(id=request.user.id)
    return usuario


def home(request):
    if request.user.is_authenticated == True:
        return redirect('index')
    else:
        return render(request, 'home.html')


@login_required
def index(request):
    usuarios = Usuario.objects.all()
    arquivos = TemplateFile.objects.all()
    return render(
        request, 'index.html', {
            "usuario": get_user_logado(request),
            "usuarios": usuarios,
            "arquivos": arquivos}
    )


def login(request):
    if request.method == 'POST':
        form = LogarForm(request.POST)
        dados_form = form.data
        user = authenticate(
            username=dados_form['username'].lower(),
            password=dados_form['password']
        )
        if user is not None:
            login_page(request, user)
            return redirect('index')
    return render(request, 'login.html')


def log_out(request):
    logout(request)
    return redirect('home')


def registrar(request):

    if request.method == 'POST':
        form = RegistrarUsuarioForm(request.POST)
        if form.is_valid():
            dados_form = form.data
            # todo o processo de salvar no bd e criar user
            # criar user
            criar_user = User.objects.create_user(
                dados_form['nome'].lower(),
                dados_form['email'].lower(),
                dados_form['senha']
            )
            # criar Usuario
            usuario = Usuario(
                nome=dados_form['nome'].lower(),
                email=dados_form['email'].lower(),
                telefone=dados_form['telefone'],
                user=criar_user
            )
            # salvar
            usuario.save()
            return redirect('login')
        else:
            return render(request, 'registrar.html', {"form": form})

    return render(request, 'registrar.html')


@login_required
def gerar_documento(request):
    return render(request, 'gerar_documento.html', {"usuario": get_user_logado(request)})


@login_required
def cadastrar_documento(request):
    if request.method == 'POST':
        form = TemplateForm(request.POST, request.FILES)
        if form.is_valid():
            arq = TemplateFile(
                nome=form.data['nome'],
                descricao=form.data['descricao'],
                arquivo=request.FILES['arquivo'],
                user=Usuario.objects.get(id=request.user.id)
            )
            arq.save()
            return redirect('index')
        else:
            return render(request, 'cadastrar_documento.html', {"form": form})
    else:
        arquivos = TemplateFile.objects.all().filter(user=get_user_logado(request))
        return render(request, 'cadastrar_documento.html', {
            "usuario": get_user_logado(request),
            "arquivos_do_user": arquivos}
        )
