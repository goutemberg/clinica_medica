from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastrarEmpresa/', views.cadastrarEmpresa, name='cadastrarEmpresa'),
    path('cadastroEmpBanco/', views.cadastroEmpBanco, name='cadastroEmpBanco'),
    path('cadMedBanco/', views.cadMedBanco, name='cadMedBanco'),
    path('cadPlantaoBanco/', views.cadPlantaoBanco, name='cadPlantaoBanco'),
    path('relatorioPage/', views.relatorioPage, name='relatorioPage'),
 
]
