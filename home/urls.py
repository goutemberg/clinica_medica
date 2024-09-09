from django.urls import path
from home.views import index, imprimirRelatorio, resultList  
from . import views

urlpatterns = [
    path('', index, name='index'),
    path('cadastroempresa/', views.cadastroEmpresa, name='cadastroEmpresa'),
    path('cadastroempresa/cadastroEmpBanco/', views.cadastroEmpBanco, name='cadastrarempresa'),

    path('cadastrarplantao/', views.cadastroPlantao, name='cadastroPlantao'),
    path('cadastrarplantao/cadastroPlantao/', views.cadastroPlantaoBanco, name='cadastroPlantaoBanco'), 

    path('cadastrarmedico/', views.cadastrarMedico, name='cadastrarMedico'),
    path('cadastrarmedico/cadastroMedBanco/', views.cadastroMedBanco, name='cadastroMedBanco'),

    path('impressao/',resultList, name='impressao'),
    
]
