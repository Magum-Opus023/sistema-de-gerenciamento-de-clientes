from django.urls import path
from . import views

urlpatterns = [
    path('', views.cliente_list, name='cliente_list'),
    path('cliente/novo/', views.criar_cliente, name='criar_cliente'),
    path('cliente/editar/<int:pk>/', views.atualizar_cliente, name='atualizar_cliente'),
    path('cliente/excluir/<int:pk>/', views.excluir_cliente, name='excluir_cliente'),
]