from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import CadastroEmpresa

def index(request):
    cadastroEmpresa = CadastroEmpresa.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'cadastroEmpresa':cadastroEmpresa
    }
    return HttpResponse(template.render(context,request))



def cadastrarEmpresa(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))

def cadastroEmpBanco(request):
    CompanyName = request.POST['companyName']
    CompanyLegalName = request.POST ['companyLegalName']
    novoCadastroEmp = CadastroEmpresa(nome=CompanyName,razao_social=CompanyLegalName)
    novoCadastroEmp.save()
    return HttpResponseRedirect(reverse('index'))