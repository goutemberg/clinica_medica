from django.db import models

class cadastroEmpresa(models.Model):
    nomeEmp = models.CharField(max_length=260)
    razaoSocialEmp = models.CharField(max_length=260)
    cnpjEmp = models.CharField(max_length=260)
    inscEstEmp = models.CharField(max_length=260)
    cepEmp = models.CharField(max_length=9)
    lougradouroEmp = models.CharField(max_length=260)
    numeroEmp = models.CharField(max_length=5)
    bairroEmp = models.CharField(max_length=260)
    cidadeEmp = models.CharField(max_length=100)
    estadoEmp = models.CharField(max_length=4)
    telefoneEmp = models.CharField(max_length=16)
    celularEmp = models.CharField(max_length=16)
    pessoaContEmp = models.CharField(max_length=50)
    emailEmp = models.CharField(max_length=50)
    isentoTribEmp = models.CharField(max_length=5)
    taxaAdmEmp = models.CharField(max_length=5)

class valorPlantao(models.Model):
    valorPlantao_12 = models.CharField(max_length=10)
    valorPlantaoHora = models.CharField(max_length=10)
    valorPlantaoSemana = models.CharField(max_length=10)
    valorPlantaoSabDom = models.CharField(max_length=10)


class cadastroMedico(models.Model):
   nome = models.CharField(max_length=260)
   especialidade = models.CharField(max_length=100)
   crm = models.CharField(max_length=10)
   telefone = models.CharField(max_length=12)

class plantao(models.Model):
    data = models.DateField()
    medico = models.CharField(max_length=260)
    hora = models.TimeField()
    valor = models.CharField(max_length=12)
