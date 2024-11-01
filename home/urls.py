from django.urls import path
from home.views import index, resultList  
from . import views
from .views import buscar_cpf, alterar_cadastro, buscar_cnpj_banco, alterar_cadastro_empresa, cadastroEmpBanco, cadastro_empresa

urlpatterns = [
    path('', index, name='index'),
    path('clinica/', cadastro_empresa, name='clinica'),
    path('clinica/cadastrar_clinica/', cadastroEmpBanco, name='cadastrar_clinica'),

    path('plantao/', views.cadastro_plantao, name='plantao'),
    path('cadastro_plantao/cadastro_plantao/', views.cadastroPlantaoBanco, name='cadastrar_plantao'), 

    path('medico/', views.cadastrar_medico, name='medico'),
    path('medico/cadastrar_medico/', views.cadastroMedBanco, name='cadastrar_medico'),

    path('impressao/',resultList, name='impressao'),

    path('buscar_cpf/', buscar_cpf, name='buscar_cpf'),

    path('buscar_cnpj_banco/', buscar_cnpj_banco, name='buscar_cnpj_banco'),

    path('alterar-cadastro/', alterar_cadastro, name='alterar_cadastro'),

     path('alterar_cadastro_empresa/', alterar_cadastro_empresa, name='alterar_cadastro_empresa'),

    
]