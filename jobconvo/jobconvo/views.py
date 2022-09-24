from multiprocessing import context
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .forms import createFaixaSalarialChoice, createNivelEscolarChoice, createVagaForm
from .models import vagaDeEmprego
from django.template import RequestContext
from django.core.paginator import Paginator

def home(request):
    return render(request, 'home.html')
    
def create(request):
    return render(request, 'create.html')

def store(request):
    data = {}
    if(request.POST['password'] != request.POST['password-conf']):
        data['msg'] = 'Senha e confirmação de senha diferente!'
        data['class'] = 'alert-danger'
    else:
        user = User.objects.create_user(request.POST['name'], request.POST['email'], request.POST['password'])
        user.first_name = request.POST['name']
        user.save()
        user.user_permissions.add(18)
        data['msg'] = 'Usuário cadastrado com sucesso!'
        data['class'] = 'alert-success'
    return render(request, 'create.html',data)

def painel(request):
    return render(request, 'painel.html')

def dologin(request):
    data = {}
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('/createVaga/')
    else:
        data['msg'] = 'Usuário ou Senha inválidos!'
        data['class'] = 'alert-danger'
        return render(request, 'painel.html',data)

def dashboard(request):
    return render(request, 'dashboard/home.html')

def logouts(request):
    logout(request)
    return redirect('/painel/')

def changePassword(request):
    user = User.objects.get(email=request.user.email)
    user.set_password(request.POST['password'])
    user.save()
    logout(request)
    return redirect('/painel/')

def createVaga(request):
    data = {}    
    if request.method == 'GET':
        form = createVagaForm() 
    else:
        form = createVagaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/lista_vagas/')
    data['form'] = form
    return render(request, "createVaga.html", data)

def createVagaSalarial(request):
    data = {}
    cbFaixaSalarial = createFaixaSalarialChoice()
    data['cbFaixaSalarial'] = cbFaixaSalarial
    if request.GET:
        temp = request.GET['cbFaixaSalarial']
    return render(request, "home.html", data)

def createNivelEscolar(request):
    data = {}
    cbEscolaridade = createNivelEscolarChoice()
    data['cbEscolaridade'] = cbEscolaridade
    if request.GET:
        temp = request.GET['cbEscolaridade']
    return render(request, "home.html", data)

def lista_vagas(request):
    data = {}
    all = vagaDeEmprego.objects.all()
    paginator = Paginator(all, 2)
    pages = request.GET.get('page')
    data['vagas'] = paginator.get_page(pages)
    #search = request.GET.get('search')
    #if search:
    #    data['vagas'] = vagaDeEmprego.objects.filter(nameJob__icontains=search)
    #else:
    #    data['vagas'] = vagaDeEmprego.objects.all()
    return render(request, "lista_vagas.html", data)

def detalhe_vaga(request, pk):
    data = {}
    data['vagas'] = vagaDeEmprego.objects.get(pk=pk)
    return render(request, "detalhe_vaga.html", data)

def edit(request, pk):
    data = {}
    data['vagas'] = vagaDeEmprego.objects.get(pk=pk)
    data['form'] = createVagaForm(instance=data['vagas'])
    return render(request, "createVaga.html", data)

def update(request, pk):
    data = {}
    data['vagas'] = vagaDeEmprego.objects.get(pk=pk)
    form = createVagaForm(request.POST or None, instance=data['vagas'])
    if form.is_valid():
        form.save()
        return redirect('/lista_vagas/')

def delete(request, pk):
    vagas = vagaDeEmprego.objects.get(pk=pk)
    vagas.delete()
    return redirect('lista_vagas')

        
            
