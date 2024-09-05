from django import forms
from django.forms import ModelForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from .models import CadastroEmpresa, CadastroMedico, ValorPlantao, ContatoEmpresa, Plantao, BancoMedico
from django.views.decorators.http import require_POST
from .models import DoctorSelect


def companyRegistration(request):
     cadastroEmpresa = CadastroEmpresa.objects.all().values()
     template = loader.get_template('plantaopro/pages/CompanyRegistration.html')
     context = {
         'cadastroEmpresa':cadastroEmpresa
     }
     return HttpResponse(template.render(context,request))

    
def cadastroEmpresa(request):
     template = loader.get_template('plantaopro/pages/CompanyRegistration.html')
     return HttpResponse(template.render({}, request))

@require_POST
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
    CompanyPhone = request.POST['companyPhone']
    CompanyCell = request.POST['companyCell']
    CompanyEmail = request.POST['companyEmail']
    CompanyIsentoTributacao = request.POST['companyIsentoTributacao'] == 'true'

    

    CompanyContactPerson = request.POST['companyContactPerson']

    novoCadastroEmp = CadastroEmpresa(
        nome=CompanyName,razao_social=CompanyLegalName,cnpj=CompanyCnpj,
        inscricao_estadual=CompanyInscricaoEstadual,cep=CompanyCep,logradouro=Lougradouro, 
        numero=CompanyNumber,bairro=CompanyNeighborhood,cidade=CompanyCity,estado=CompanyState, telefone=CompanyPhone, celular=CompanyCell, 
        email=CompanyEmail, isento_tributacao=CompanyIsentoTributacao
    )

    novoCadastroEmp.save()

    CompanyValorPlantao_12 = request.POST['companyValorPlantao_12']
    CompanyValorPlantaoHora = request.POST['companyValorPlantaoHora']
    CompanyPlantaoSemana = request.POST['companyPlantaoSemana']
    CompanyValorPlantaoSabadoDomingo = request.POST['companyValorPlantaoSabadoDomingo']

    novoCadPlantao = ValorPlantao(
        empresa=novoCadastroEmp,
        valor_12h=CompanyValorPlantao_12,
        valor_por_hora=CompanyValorPlantaoHora,
        valor_semana=CompanyPlantaoSemana,
        valor_fim_semana=CompanyValorPlantaoSabadoDomingo,
    )
    novoCadPlantao.save()

    novoPessoaContato = ContatoEmpresa(
        empresa=novoCadastroEmp,
        pessoa_contato=CompanyContactPerson
    )
    
    novoPessoaContato.save()

    # return HttpResponseRedirect(reverse('plantaopro/pages/CompanyRegistration'))
    return redirect('index')

def shiftRegistration(request):
     cadastroPlantao = Plantao.objects.all().values()
     template = loader.get_template('plantaopro/pages/shiftRegistration.html')
     context = {
         'cadastroPlantao':cadastroPlantao
     }
     return HttpResponse(template.render(context,request))

    
def cadastroPlantao(request):
     template = loader.get_template('plantaopro/pages/shiftRegistration.html')
     return HttpResponse(template.render({}, request))

@require_POST
def cadastroPlantaoBanco(request):
    StartDate = request.POST['startDate']
    EndDate = request.POST ['endDate']
    StartTime = request.POST ['startTime']
    EndTime = request.POST['endTime']
    DoctorSelect = request.POST['doctorSelect']
    Specialty = request.POST ['specialty']
    ShiftType = request.POST['shiftType']
    ShiftValue = request.POST['shiftValue'] 
    ShiftHours= request.POST['shiftHours']
    ShiftStatus = request.POST['shiftStatus']
    EmergencyContact = request.POST['emergencyContact']
    Equipment = request.POST['equipment']
    AuxiliaryStaff = request.POST['auxiliaryStaff']
    Substitute = request.POST['substitute']
    Notes = request.POST['notes']
    

    novoCadastroPlan = Plantao(
        data_inicio=StartDate,hora_inicio=StartTime,data_termino=EndDate,hora_termino=EndTime,medico_responsavel=DoctorSelect, especialidade=Specialty,tipo_plantao=ShiftType, 
        quantidade_horas=ShiftHours,valor=ShiftValue,status=ShiftStatus,contato_emergencia=EmergencyContact,equipamentos_necessarios=Equipment, 
        cargos_auxiliares=AuxiliaryStaff,substituto=Substitute,observacoes=Notes 
       
    )

    novoCadastroPlan.save()

    return redirect('plantaopro/pages/shiftRegistration.html')

def doctorRegistration(request):
     cadastroMedico = CadastroMedico.objects.all().values()
     template = loader.get_template('plantaopro/pages/doctorRegistration.html')
     context = {
         'cadastroMedico':cadastroMedico
     }
     return HttpResponse(template.render(context,request))

    
def cadastrarMedico(request):
     template = loader.get_template('plantaopro/pages/doctorRegistration.html')
     return HttpResponse(template.render({}, request))

# @require_POST
# def cadastroMedBanco(request):
#     DoctorName = request.POST['doctorName']
#     DoctorCpf = request.POST ['doctorCpf']
#     DoctorSpecialty = request.POST ['doctorSpecialty']
#     DoctorCrm = request.POST['doctorCrm']
#     DoctorPhone = request.POST['doctorPhone']
#     DoctorAddress = request.POST ['doctorAddress']
#     DoctorNumber = request.POST['doctorNumber']
#     DoctorComplement = request.POST['doctorComplement'] 
#     DoctorNeighborhood = request.POST['doctorNeighborhood']
#     DoctorCity = request.POST['doctorCity']
#     DoctorState = request.POST['doctorState']
#     DoctorPhone1 = request.POST['doctorPhone1']
#     DoctorPhone2 = request.POST['doctorPhone2']
#     DoctorEmail = request.POST['doctorEmail']
#     BankName = request.POST['bankName']
#     BankAgency = request.POST['bankAgency']
#     BankAccount = request.POST['bankAccount']
#     BankHolder = request.POST['bankHolder']
    
#     novoCadastroMed = CadastroMedico(
#         nome=DoctorName,cpf=DoctorCpf,especialidade=DoctorSpecialty,crm=DoctorCrm,celular=DoctorPhone,logradouro=DoctorAddress,numero=DoctorNumber,
#         complemento=DoctorComplement,bairro=DoctorNeighborhood,cidade=DoctorCity,estado=DoctorState,telefone1=DoctorPhone1, 
#         telefone2=DoctorPhone2,email=DoctorEmail 
#     )

#     novoCadastroMed.save()

#     novoBankDoctor = BancoMedico (

#     banco=BankName,agencia=BankAgency,conta=BankAccount,titular_conta=BankHolder
#     )
#     novoBankDoctor.save()

@require_POST
def cadastroMedBanco(request):
    DoctorName = request.POST['doctorName']
    DoctorCpf = request.POST['doctorCpf']
    DoctorSpecialty = request.POST['doctorSpecialty']
    DoctorCrm = request.POST['doctorCrm']
    DoctorPhone = request.POST['doctorPhone']
    DoctorAddress = request.POST['doctorAddress']
    DoctorNumber = request.POST['doctorNumber']
    DoctorComplement = request.POST['doctorComplement'] 
    DoctorNeighborhood = request.POST['doctorNeighborhood']
    DoctorCity = request.POST['doctorCity']
    DoctorState = request.POST['doctorState']
    DoctorPhone1 = request.POST['doctorPhone1']
    DoctorPhone2 = request.POST['doctorPhone2']
    DoctorEmail = request.POST['doctorEmail']
    BankName = request.POST['bankName']
    BankAgency = request.POST['bankAgency']
    BankAccount = request.POST['bankAccount']
    BankHolder = request.POST['bankHolder']
    
    # Cria e salva o novo médico
    novoCadastroMed = CadastroMedico(
        nome=DoctorName, cpf=DoctorCpf, especialidade=DoctorSpecialty, crm=DoctorCrm, celular=DoctorPhone, 
        logradouro=DoctorAddress, numero=DoctorNumber, complemento=DoctorComplement, bairro=DoctorNeighborhood, 
        cidade=DoctorCity, estado=DoctorState, telefone1=DoctorPhone1, telefone2=DoctorPhone2, email=DoctorEmail
    )
    novoCadastroMed.save()

    # Cria e salva o novo banco associado ao médico criado
    novoBankDoctor = BancoMedico(
        medico=novoCadastroMed,  # Aqui, relacionamos com o novo médico criado
        banco=BankName, agencia=BankAgency, conta=BankAccount, titular_conta=BankHolder
    )
    novoBankDoctor.save()

    exibeMedBanco = {
         'medicos': CadastroMedico.objects.all()
         
    }

    return redirect('http://127.0.0.1:8000/cadastrarmedico/', exibeMedBanco)


def index(request):
    return render(
        request,
        'plantaopro/pages/index.html'
    )

def imprimirRelatorio(request):
    return render(
        request,
        'plantaopro/pages/print.html'
    )






    


