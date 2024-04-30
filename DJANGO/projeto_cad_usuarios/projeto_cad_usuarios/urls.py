from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    #rota, view responsável, nome de referência
    path('', views.home, name='chamados'),

    path('cadastro_usuarios/', views.cadastro_usuarios, name='cadastro_usuarios'),

    path('usuarios/', views.usuarios, name='listagem_usuarios'),
    ]
