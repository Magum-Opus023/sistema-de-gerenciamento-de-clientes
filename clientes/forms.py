from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):
    aniversario = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'DD/MM'}),
        help_text="Informe apenas o dia e o mês (ex: 03/04)"
    )
    class Meta:
        model = Cliente
        fields = '__all__'