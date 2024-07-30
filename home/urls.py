# from django.urls import path
# from . import views


from django.urls import path
from home.views import index, cadastrarempresa, cadastrarmedico, cadastrarplantao, impressao


# urlpatterns = [
#     path('', views.index, name='index'),
#     path('cadastrarEmpresa/', views.cadastrarEmpresa, name='cadastrarEmpresa'),
#     path('cadastroEmpBanco/', views.cadastroEmpBanco, name='cadastroEmpBanco'),
#     path('cadMedBanco/', views.cadMedBanco, name='cadMedBanco'),
#     path('cadPlantaoBanco/', views.cadPlantaoBanco, name='cadPlantaoBanco'),
#     path('relatorioPage/', views.relatorioPage, name='relatorioPage'),
 
# ]
app_name = "plantao_pro"

urlpatterns = [
    path('', index, name='index'),
    path('cadastrarempresa/', cadastrarempresa, name='cadastraempresa'),
    path('cadastrarmedico/', cadastrarmedico, name='cadastrarmedico'),
    path('cadastrarplantao/', cadastrarplantao, name='cadastrarplantao'),
    path('impressao/', impressao, name='impressao'),
    
]
