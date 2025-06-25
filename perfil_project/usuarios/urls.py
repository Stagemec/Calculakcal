from django.urls import path
from . import views

urlpatterns = [
    path('', views.perfil_detalhe, name='perfil_detalhe'),
    path('criar/', views.criar_perfil, name='criar_perfil'),
    path('atualizar/<int:pk>/', views.atualizar_peso, name='atualizar_peso'),
    path('meta/<int:pk>/', views.calcular_meta, name='calcular_meta'),
    path('grafico/<int:pk>/', views.grafico_peso, name='grafico_peso'),
    path('excluir/<int:pk>/', views.excluir_perfil, name='excluir_perfil'),
    path('perfil/<int:pk>/', views.perfil_detalhe, name='perfil_detalhe'),
    path('perfil/<int:pk>/', views.perfil_detalhe, name='perfil_detalhe'),
]