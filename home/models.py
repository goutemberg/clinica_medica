from django.db import models

class CadastroClinica(models.Model):
    nome = models.CharField(max_length=260)
    razaoSocial = models.CharField(max_length=260)
    cep = models.CharField(max_length=9)
    rua = models.CharField(max_length=260)
    numero = models.CharField(max_length=5)
    bairro = models.CharField(max_length=260)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)

class CadastroMedico(models.Model):
   nome = models.CharField(max_length=260)
   especialidade = models.CharField(max_length=100)
   crm = models.CharField(max_length=10)
   telefone = models.CharField(max_length=12)

class Plantao(models.Model):
    data = models.DateField()
    medico = models.CharField(max_length=260)
    hora = models.TimeField()
    valor = models.CharField()
