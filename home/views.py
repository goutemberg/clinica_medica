

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
    try:
        # Extrair dados do formulário
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
            doctorCpf=DoctorCpf, doctorName=DoctorName, birthdate=Birthdate, email=Email, phone=Phone,
            cep=Cep, address=Address, number=Number, complement=Complement, bairro=Bairro, city=City,
            state=State, professionalType=ProfessionalType, doctorSpecialty=DoctorSpecialty,
            registerType=RegisterType, doctorCrm=DoctorCrm, academicDegree=AcademicDegree,
            institutionName=InstitutionName, graduationYear=GraduationYear, certifications=Certifications,
            clinicAffiliation=ClinicAffiliation, otherInfo=OtherInfo
        )
        novoCadastroMed.save()

        # Redireciona após o cadastro bem-sucedido
        return redirect('cadastrarMedico')

    except Exception as e:
        # Log ou tratamento de erro
        print(f"Erro ao salvar cadastro: {e}")
        return render(request, 'erro.html', {'mensagem': 'Ocorreu um erro ao tentar cadastrar o médico.'})


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
@require_POST
def buscar_cpf(request):
    import json
    
    # Tente capturar o CPF enviado via JSON
    try:
        data = json.loads(request.body)
        cpf = data.get('doctorCpf')  # O nome da chave deve corresponder ao nome enviado no 'fetch'
        
        if not cpf:
            return JsonResponse({'error': 'CPF não fornecido'}, status=400)
        
        print(f"O Cpf enviado foi {cpf}")

        # Busca o médico no banco de dados
        try:
            medico = CadastroMedico.objects.get(doctorCpf=cpf)
            medico_data = {
                'doctorCpf': medico.doctorCpf,
                'doctorName': medico.doctorName,
                'birthdate': medico.birthdate,
                'email': medico.email,
                'phone': medico.phone,
                'cep': medico.cep,
                'address': medico.address,
                'number': medico.number,
                'complement': medico.complement,
                'bairro': medico.bairro,
                'city': medico.city,
                'state': medico.state,
                'professionalType': medico.professionalType,
                'doctorSpecialty': medico.doctorSpecialty,
                'registerType': medico.registerType,
                'doctorCrm': medico.doctorCrm,
                'academicDegree': medico.academicDegree,
                'institutionName': medico.institutionName,
                'graduationYear': medico.graduationYear,
                'certifications': medico.certifications,
                'clinicAffiliation': medico.clinicAffiliation,
                'otherInfo': medico.otherInfo
            }
            return JsonResponse({'exists': True, 'medico': medico_data})

        except CadastroMedico.DoesNotExist:
            return JsonResponse({'exists': False})

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Erro ao decodificar JSON'}, status=400)
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
    


