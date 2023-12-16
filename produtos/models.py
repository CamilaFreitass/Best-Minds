from django.db import models
from django.contrib.auth.models import User

class Produto(models.Model):
    nome_produto = models.CharField(max_length=50)
    codigo_produto = models.IntegerField()
    descricao_produto = models.TextField()
    preco_produto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return self.nome_produto