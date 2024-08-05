from django.urls import path
from home.views import index
from . import views

app_name = "plantao_pro"

urlpatterns = [
    path('', index, name='index'),
    path('cadastrarempresa/', views.cadastroEmpresa, name='cadastraempresa'),
    path('cadastrarempresa/cadastroEmpBanco/', views.cadastroEmpBanco, name='cadastrarempBanco'),

    path('cadastrarplantao/', views.cadastroPlantao, name='cadastrarplantao'),
    path('cadastrarplantao/cadastroPlantao/', views.cadastroPlantaoBanco, name='cadastroPlantaoBanco'), 

    path('cadastrarmedico/', views.cadastrarMedico, name='cadastrarmedico'),
    path('cadastrarmedico/cadastroMedBanco/', views.cadastroMedBanco, name='cadastroMedBanco'), 
]
