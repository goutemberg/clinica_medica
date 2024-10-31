from django.urls import path
from home.views import index, resultList  
from . import views
from .views import buscar_cpf, alterar_cadastro, buscar_cnpj_banco, alterar_cadastro_empresa, cadastroEmpBanco, cadastro_empresa

urlpatterns = [
    path('', index, name='index'),
    path('cadastro_empresa/', cadastro_empresa, name='cadastro_empresa'),
    path('cadastroempresa/cadastroEmpBanco/', cadastroEmpBanco, name='cadastrarempresa'),

    path('cadastrarplantao/', views.cadastroPlantao, name='cadastroPlantao'),
    path('cadastrarplantao/cadastroPlantao/', views.cadastroPlantaoBanco, name='cadastroPlantaoBanco'), 

    path('cadastrarmedico/', views.cadastrarMedico, name='cadastrarMedico'),
    path('cadastrarmedico/cadastroMedBanco/', views.cadastroMedBanco, name='cadastroMedBanco'),

    path('impressao/',resultList, name='impressao'),

    path('buscar_cpf/', buscar_cpf, name='buscar_cpf'),

    path('buscar_cnpj_banco/', buscar_cnpj_banco, name='buscar_cnpj_banco'),

    path('alterar-cadastro/', alterar_cadastro, name='alterar_cadastro'),

     path('alterar_cadastro_empresa/', alterar_cadastro_empresa, name='alterar_cadastro_empresa'),

    
]