from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    aniversario = forms.DateField(
        widget=forms.DateInput(format='%d/%m', attrs={'type': 'date'}),
        input_formats=['%d-%m-%y', '%d/%m']
    )
    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone', 'cpf', 'aniversario']