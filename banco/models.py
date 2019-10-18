from django.db import models

from cadastro.models import Cadastro


class BancoHoras(models.Model):
    militar = models.ForeignKey(Cadastro, on_delete=models.CASCADE)
    horas_adicionadas = models.IntegerField(default=0)
    horas_usadas = models.IntegerField(default=0)
    descricao = models.CharField(max_length=150, default="Nao informado")
    aprovado = models.BooleanField(default=False)

    def __str__(self):
        return self.militar.user.username

    class Meta:
        verbose_name_plural = "Banco De Horas"
