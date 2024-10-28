from django import forms
from django.db import models
from django.forms import ModelForm
from django.utils import timezone
from django.utils.timezone import now
from django.core.validators import RegexValidator, EmailValidator

from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator, EmailValidator

class CadastroEmpresa(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    razao_social = models.CharField(max_length=255)
    cnpj = models.CharField(
        max_length=18,
        unique=True,
        validators=[
            RegexValidator(regex=r'^\d{2}\.\d{3}\.\d{3}/\d{4}-\d{2}$', message='CNPJ deve estar no formato 00.000.000/0000-00')
        ]
    )
    inscricao_estadual = models.CharField(max_length=255, blank=True, null=True)
    cep = models.CharField(max_length=9, validators=[
        RegexValidator(regex=r'^\d{5}-?\d{3}$', message='CEP deve estar no formato XXXXX-XXX')
    ])
    logradouro = models.CharField(max_length=255)
    numero = models.CharField(max_length=5)
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    telefone = models.CharField(max_length=16, validators=[
        RegexValidator(regex=r'^\(?\d{2}\)?[\s-]?\d{4,5}-?\d{4}$', message='Telefone deve estar no formato (XX) XXXX-XXXX ou (XX) XXXXX-XXXX')
    ])
    celular = models.CharField(max_length=16, blank=True, null=True, validators=[
        RegexValidator(regex=r'^\(?\d{2}\)?[\s-]?\d{4,5}-?\d{4}$', message='Celular deve estar no formato (XX) XXXXX-XXXX')
    ])
    email = models.EmailField(max_length=50, validators=[EmailValidator(message='Email inválido')])
    isento_tributacao = models.BooleanField(default=False)
    pessoa_contato = models.CharField(max_length=50, default='N/A')
    valor_12h = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    valor_por_hora = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    valor_semana = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    valor_fim_semana = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    taxa_administrativa = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    valor_contrato = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.nome



class BancoEmpresa(models.Model):
    empresa = models.ForeignKey(CadastroEmpresa, on_delete=models.CASCADE, related_name='bancos')
    banco = models.CharField(max_length=50)
    agencia = models.CharField(max_length=10)
    conta = models.CharField(max_length=10)
    titular_conta = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.banco} - {self.agencia}/{self.conta}'

class CadastroMedico(models.Model):
    doctorCpf = models.CharField(max_length=11, unique=True,default='N/A')  
    doctorName = models.CharField(max_length=100,default='N/A')  
    birthdate = models.DateField(default=now)  
    email = models.EmailField(default='N/A')  
    phone = models.CharField(max_length=15,blank=True, null=True)  
    cep = models.CharField(max_length=9,blank=True, null=True)  
    address = models.CharField(max_length=255,blank=True, null=True)  
    number = models.CharField(max_length=10,blank=True, null=True)  
    complement = models.CharField(max_length=255, blank=True, null=True) 
    bairro = models.CharField(max_length=100,blank=True, null=True)  
    city = models.CharField(max_length=100,blank=True, null=True) 
    state = models.CharField(max_length=2,blank=True, null=True) 
    professionalType = models.CharField(max_length=50,blank=True, null=True)  
    doctorSpecialty = models.CharField(max_length=100,blank=True, null=True)  
    registerType = models.CharField(max_length=50,blank=True, null=True)  
    doctorCrm = models.CharField(max_length=15, unique=True,default='N/A')  
    academicDegree = models.CharField(max_length=100,blank=True, null=True)  
    institutionName = models.CharField(max_length=255,default='N/A')  
    graduationYear = models.IntegerField(default=2000)  
    certifications = models.TextField(blank=True, null=True)  
    clinicAffiliation = models.CharField(max_length=255, blank=True, null=True)  
    otherInfo = models.TextField(blank=True, null=True)  

    def __str__(self):
        return f"{self.doctorName} - {self.doctorCpf}"
    
class Plantao(models.Model):
    id = models.AutoField(primary_key=True)
    data_inicio = models.DateField(default=timezone.now)
    hora_inicio = models.TimeField(default=timezone.now)
    data_termino = models.DateField(default=timezone.now)
    hora_termino = models.TimeField(default=timezone.now)
    medico_responsavel = models.ForeignKey(CadastroMedico, on_delete=models.SET_NULL, related_name='plantoes',
    blank=True, null=True)
    especialidade = models.CharField(max_length=255)
    tipo_plantao = models.CharField(max_length=20)
    quantidade_horas = models.DecimalField(max_digits=5, decimal_places=2)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=12)
    contato_emergencia = models.CharField(max_length=255)
    equipamentos_necessarios = models.TextField(blank=True, null=True)
    cargos_auxiliares = models.TextField(blank=True, null=True)
    substituto = models.CharField(max_length=255, blank=True, null=True)
    observacoes = models.TextField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f'Plantão {self.tipo_plantao} de {self.medico_responsavel}'
    

class DoctorSelect(ModelForm):
     class Meta:
          model = CadastroMedico
          fields = '__all__'
doctor = forms.ModelChoiceField(
         queryset=CadastroMedico.objects.all(),
    )

class PrintPlantao(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14)  # Formato: XXX.XXX.XXX-XX
    especialidade = models.CharField(max_length=100)
    valor_plantao = models.CharField(max_length=100)
    horas = models.CharField(max_length=100)
    valor_horas = models.CharField(max_length=100)
    subtotal = models.CharField(max_length=100)
    valor_imposto = models.CharField(max_length=100)
    valor_a_receber = models.CharField(max_length=100)
    medico = models.ForeignKey(CadastroMedico, on_delete=models.CASCADE, null=True)
    data = models.DateField(default=timezone.now)

    def __str__(self) -> str:
        return self.nome
    
     
    



    