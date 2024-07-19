from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator, EmailValidator

from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator, EmailValidator

class CadastroEmpresa(models.Model):
    nome = models.CharField(max_length=255)
    razao_social = models.CharField(max_length=255)
    cnpj = models.CharField(
        max_length=14, 
        primary_key=True,
        validators=[
            RegexValidator(regex='^\d{14}$', message='CNPJ deve conter 14 dígitos numéricos')
        ]
    )
    inscricao_estadual = models.CharField(max_length=255)
    cep = models.CharField(max_length=9, validators=[
        RegexValidator(regex='^\d{5}-?\d{3}$', message='CEP deve estar no formato XXXXX-XXX')
    ])
    logradouro = models.CharField(max_length=255)
    numero = models.CharField(max_length=5)
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    telefone = models.CharField(max_length=16, validators=[
        RegexValidator(regex='^\(?\d{2}\)?[\s-]?\d{4,5}-?\d{4}$', message='Telefone deve estar no formato (XX) XXXX-XXXX ou (XX) XXXXX-XXXX')
    ])
    celular = models.CharField(max_length=16, default='00000000000', validators=[
        RegexValidator(regex='^\(?\d{2}\)?[\s-]?\d{4,5}-?\d{4}$', message='Celular deve estar no formato (XX) XXXXX-XXXX')
    ])  # Adicionado valor padrão
    pessoa_contato = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, validators=[EmailValidator(message='Email inválido')])
    isento_tributacao = models.BooleanField(default=False)
    taxa_administrativa = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    valor_imposto = models.CharField(max_length=5)
    valor_12h = models.DecimalField(max_digits=10, decimal_places=2, default=00)
    valor_por_hora = models.DecimalField(max_digits=10, decimal_places=2, default=00)
    valor_semana = models.DecimalField(max_digits=10, decimal_places=2, default=00)
    valor_fim_semana = models.DecimalField(max_digits=10, decimal_places=2, default=00)



# class ValorPlantao(models.Model):
#     valor_12h = models.DecimalField(max_digits=10, decimal_places=2)
#     valor_por_hora = models.DecimalField(max_digits=10, decimal_places=2)
#     valor_semana = models.DecimalField(max_digits=10, decimal_places=2)
#     valor_fim_semana = models.DecimalField(max_digits=10, decimal_places=2)

class InformacoesBancarias(models.Model):
    banco = models.CharField(max_length=50)
    agencia = models.CharField(max_length=10, validators=[
        RegexValidator(regex='^\d{4,10}$', message='Agência deve conter de 4 a 10 dígitos numéricos')
    ])
    conta = models.CharField(max_length=10, validators=[
        RegexValidator(regex='^\d{5,10}$', message='Conta deve conter de 5 a 10 dígitos numéricos')
    ])
    titular_conta = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.titular_conta} - {self.banco}'

class CadastroMedico(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14, primary_key=True, validators=[
        RegexValidator(regex='^\d{11}$', message='CPF deve conter 11 dígitos numéricos')
    ])
    especialidade = models.CharField(max_length=100)
    crm = models.CharField(max_length=20)
    celular = models.CharField(max_length=16, validators=[
        RegexValidator(regex='^\(?\d{2}\)?[\s-]?\d{4,5}-?\d{4}$', message='Celular deve estar no formato (XX) XXXXX-XXXX')
    ])
    logradouro = models.CharField(max_length=255)
    numero = models.CharField(max_length=5)
    complemento = models.CharField(max_length=255, blank=True, null=True)
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=2)
    telefone1 = models.CharField(max_length=16, validators=[
        RegexValidator(regex='^\(?\d{2}\)?[\s-]?\d{4,5}-?\d{4}$', message='Telefone deve estar no formato (XX) XXXX-XXXX ou (XX) XXXXX-XXXX')
    ])
    telefone2 = models.CharField(max_length=16, blank=True, null=True, validators=[
        RegexValidator(regex='^\(?\d{2}\)?[\s-]?\d{4,5}-?\d{4}$', message='Telefone deve estar no formato (XX) XXXX-XXXX ou (XX) XXXXX-XXXX')
    ])
    email = models.EmailField(max_length=100, validators=[EmailValidator(message='Email inválido')])
    informacoes_bancarias = models.OneToOneField(InformacoesBancarias, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Atendente(models.Model):
    nome = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nome

class InformacoesClinica(models.Model):
    nome = models.CharField(max_length=255)
    atendentes = models.ManyToManyField(Atendente, related_name='clinicas')
    telefone = models.CharField(max_length=16, validators=[
        RegexValidator(regex='^\(?\d{2}\)?[\s-]?\d{4,5}-?\d{4}$', message='Telefone deve estar no formato (XX) XXXX-XXXX ou (XX) XXXXX-XXXX')
    ])

    def __str__(self):
        return self.nome

class Plantao(models.Model):
    data_inicio = models.DateField(default=timezone.now)
    hora_inicio = models.TimeField(default=timezone.now)
    data_termino = models.DateField(default=timezone.now)
    hora_termino = models.TimeField(default=timezone.now)
    medico_responsavel = models.ForeignKey(CadastroMedico, on_delete=models.CASCADE)
    especialidade = models.CharField(max_length=255)
    tipo_plantao = models.CharField(max_length=20)
    quantidade_horas = models.DecimalField(max_digits=5, decimal_places=2)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=12)
    contato_emergencia = models.CharField(max_length=255)
    equipamentos_necessarios = models.TextField()
    cargos_auxiliares = models.TextField()
    substituto = models.CharField(max_length=255)
    observacoes = models.TextField(max_length=255)

    def __str__(self):
        return f'Plantão {self.tipo_plantao} de {self.medico_responsavel}'
    