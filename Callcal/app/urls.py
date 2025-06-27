from django.urls import path
from . import views

urlpatterns = [
    path('', views.boas_vindas, name='boas_vindas'),
    path('perfis/', views.lista_perfis, name='lista_perfis'),
    path('cadastrar/', views.cadastro_perfil, name='cadastro_perfil'),
    path('perfil/<int:perfil_id>/', views.detalhes_perfil, name='detalhes_perfil'),
    path('perfil/<int:perfil_id>/atualizar/', views.registrar_atualizacao, name='registrar_atualizacao'),
]
