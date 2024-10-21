

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from .models import CadastroEmpresa, CadastroMedico, ValorPlantao, ContatoEmpresa, Plantao, PrintPlantao
from django.views.decorators.http import require_POST
from django.db.models import Q
from datetime import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json



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

@require_POST
def cadastroMedBanco(request):
    
    DoctorCpf = request.POST['doctorCpf']
    DoctorName = request.POST['doctorName']
    Birthdate = request.POST['birthdate']
    Email = request.POST['email']
    Phone = request.POST['phone']
    Cep = request.POST['cep']
    Address = request.POST['address']
    Number = request.POST['number']
    Complement = request.POST['complement']
    Bairro = request.POST['bairro']
    City = request.POST['city']
    State = request.POST['state']
    ProfessionalType = request.POST['professionalType']
    DoctorSpecialty = request.POST['doctorSpecialty']
    RegisterType = request.POST['registerType']
    DoctorCrm = request.POST['doctorCrm']
    AcademicDegree = request.POST['academicDegree']
    InstitutionName = request.POST['institutionName']
    GraduationYear = request.POST['graduationYear']
    Certifications = request.POST['certifications']
    ClinicAffiliation = request.POST['clinicAffiliation']
    OtherInfo = request.POST['otherInfo']
    
    # Cria e salva o novo médico
    novoCadastroMed = CadastroMedico(
        doctorCpf=DoctorCpf,doctorName=DoctorName,birthdate=Birthdate,email=Email,phone=Phone,
        cep=Cep,address=Address,number=Number,complement=Complement,bairro=Bairro,city=City,
        state=State,professionalType=ProfessionalType,
        doctorSpecialty=DoctorSpecialty,registerType=RegisterType,doctorCrm=DoctorCrm,academicDegree=AcademicDegree,
        institutionName=InstitutionName,graduationYear=GraduationYear,certifications=Certifications,
        clinicAffiliation=ClinicAffiliation,otherInfo=OtherInfo
    )
    novoCadastroMed.save()

    # Cria e salva o novo banco associado ao médico criado
    #novoBankDoctor = BancoMedico(
    #    medico=novoCadastroMed,  # Aqui, relacionamos com o novo médico criado
    #    banco=BankName, agencia=BankAgency, conta=BankAccount, titular_conta=BankHolder
    #)
    #novoBankDoctor.save()

    exibeMedBanco = {
         'medicos': CadastroMedico.objects.all()
         
    }

    return redirect('cadastroMedBanco')


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

def resultList(request):
    template_name = "plantaopro/pages/print.html"

    # Buscando médicos para o filtro
    medicos = CadastroMedico.objects.all()

    # Pegando os parâmetros de filtro
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    medico_nome = request.GET.get('medico')

    # Pegando todos os registros inicialmente
    records = PrintPlantao.objects.all()

    # Aplicando filtros de data
    if start_date and end_date:
        records = records.filter(data__range=[start_date, end_date])

    # Aplicando o filtro de médico pelo nome
    if medico_nome:
        records = records.filter(medico__nome=medico_nome)

    return render(
        request,
        template_name,
        {
            "record": records,
            "medicos": medicos,  # Passar médicos para o template
        },
    )
def buscar_cpf(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        cpf = data.get('cpf')
        print(f"CPF recebido: {cpf}")
        
        try:
            medico = CadastroMedico.objects.get(doctorCpf=cpf)
            response = {
                'exists': True,
                'nome': medico.doctorName,
                'data_nascimento': medico.birthdate,
                'email': medico.email,
                'telefone': medico.phone,
                'cep': medico.cep,
                'endereco': medico.address,
                'numero': medico.number,
                'complemento': medico.complement,
                'bairro': medico.bairro,
                'cidade': medico.city,
                'estado': medico.state,
                'tipo_profissional': medico.professionalType,
                'especialidade': medico.doctorSpecialty,
                'tipo_registro': medico.registerType,
                'crm': medico.doctorCrm,
                'grau_academico': medico.academicDegree,
                'instituicao': medico.institutionName,
                'ano_graduacao': medico.graduationYear,
                'certificacoes': medico.certifications,
                'clinica_afiliada': medico.clinicAffiliation,
                'outras_infos': medico.otherInfo
            }
        except CadastroMedico.DoesNotExist:
            print(f"CPF {cpf} não encontrado")
            response = {'exists': False}

        return JsonResponse(response)



@csrf_exempt
def alterar_cadastro(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        cpf = data.get('doctorCpf')
        nome = data.get('doctorName')
        

        try:
            # Buscar o médico pelo CPF
            medico = CadastroMedico.objects.get(doctorCpf=cpf)
            medico.doctorName = nome
            medico.save()

            return JsonResponse({'success': True})
        except CadastroMedico.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Médico não encontrado.'})
    


