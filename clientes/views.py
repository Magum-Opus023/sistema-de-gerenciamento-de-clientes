from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Cliente
from .forms import ClienteForm

# Create your views here.

def cliente_list(request):
    clientes = Cliente.objects.all()
    print("Clientes recuperados:", clientes)  # Adicionando um print para depuração
    return render(request, 'clientes/cliente_list.html', {'clientes': clientes})

def criar_cliente(request):
    if request.method == 'POST':
        print("Dados recebidos no formulário:", request.POST)  # Debugging
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            print("Cliente salvo com sucesso!")  # Verificar se salvou
            return redirect('cliente_list')
        else:
            print("Erro no formulário:", form.errors)  # Se o formulário for inválido, mostre os erros
    else:
        form = ClienteForm()
    return render(request, 'clientes/cliente_form.html', {'form': form})

def atualizar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('cliente_list')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'clientes/cliente_form.html', {'form': form})

def excluir_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('cliente_list')
    return render(request, 'clientes/cliente_confirm_delete.html', {'cliente': cliente})
