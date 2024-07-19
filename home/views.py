from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import CadastroEmpresa, ValorPlantao


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
    CompanyCnpj = request.POST ['companyCnpj']
    CompanyInscricaoEstadual = request.POST['companyInscricaoEstadual']
    CompanyCep = request.POST['companyCep']
    Lougradouro = request.POST ['lougradouro']
    CompanyNumber = request.POST['companyNumber']
    CompanyNeighborhood = request.POST['companyNeighborhood'] 
    CompanyCity= request.POST['companyCity']
    CompanyState = request.POST['companyState']
    CompanyPhone = request.POST['companyPhon']
    CompanyCell = request.POST['companyCell']
    CompanyContactPerson = request.POST['companyContactPerson']
    CompanyEmail = request.POST['companyEmail']
    CompanyTaxaAdministracao = request.POST['companyTaxaAdministracao']
    CompanyIsentoTributacao = request.POST['companyIsentoTributacao']
    novoCadastroEmp = CadastroEmpresa(nome=CompanyName,razao_social=CompanyLegalName,cnpj=CompanyCnpj,inscricao_estadual=CompanyInscricaoEstadual,
    cep=CompanyCep,logradouro=Lougradouro,numero=CompanyNumber,bairro=CompanyNeighborhood,cidade=CompanyCity,estado=CompanyState,telefone=CompanyPhone,
    celular=CompanyCell,pessoa_contato=CompanyContactPerson,email=CompanyEmail,taxa_administrativa=CompanyTaxaAdministracao,isento_tributacao=CompanyIsentoTributacao,
    )
    novoCadastroEmp.save()
    return HttpResponseRedirect(reverse('index'))


def index(request):
    cadValorPlant = ValorPlantao.objects.all().values()
    template = loader.get_template('index.html')
    context = {
        'cadValorPlant':cadValorPlant
    }
    return HttpResponse(template.render(context,request))


def cadastrarValorPlant(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render({}, request))

def cadValorPlant(request):
    CompanyValorPlantao = request.POST['companyValorPlantao']
    CompanyValorPlantaoHora = request.POST['companyValorPlantaoHora']
    CompanyPlantaoSemana = request.POST['companyPlantaoSemana'] 
    CompanyValorPlantaoSabadoDomingo = request.POST['companyValorPlantaoSabadoDomingo']
    novoCadPlant = ValorPlantao(valor_12h=CompanyValorPlantao,valor_por_hora=CompanyValorPlantaoHora,valor_semana=CompanyPlantaoSemana,valor_fim_semana=CompanyValorPlantaoSabadoDomingo)
    novoCadPlant.save()
    return HttpResponseRedirect(reverse('index')) 