from django.urls import path
from . import views

urlpatterns = [
    path('', views.cliente_list, name='cliente_list'),
    path('cliente/novo/', views.cliente_create, name='cliente_create'),
    path('cliente/editar/<int:pk>/', views.cliente_update, name='cliente_update'),
    path('cliente/excluir/<int:pk>/', views.cliente_delete, name='cliente_delete'),
]