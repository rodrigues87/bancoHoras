from django.contrib.auth.models import User
from django.db import models


class BancoHoras(models.Model):
    militar = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario_cadastro")
    horas_adicionadas = models.IntegerField(default=0)
    horas_usadas = models.IntegerField(default=0)
    descricao = models.CharField(max_length=150, default="Nao informado")
    aprovado = models.BooleanField(default=False)

    def __str__(self):
        return self.militar.username

    class Meta:
        verbose_name_plural = "Banco De Horas"
