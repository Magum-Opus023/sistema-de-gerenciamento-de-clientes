from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    endereco = models.TextField()
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return self.nome