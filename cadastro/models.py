from django.contrib.auth.models import User
from django.db import models

from locais.models import Locais


class Cadastro(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    postoGraduacao = models.CharField(blank=True, null=True, max_length=12, default="nao encontrado")
    nome = models.CharField(blank=True, null=True, max_length=90, default="nao encontrado")
    oficial = models.CharField(max_length=1, blank=True, null=True, default="E")
    nomeGuerra = models.CharField(blank=True, null=True, max_length=30, default="nao encontrado")
    numeroFuncional = models.CharField(blank=True, null=True, max_length=10, default="nao encontrado")
    cpf = models.CharField(blank=True, null=True, max_length=15, default="nao encontrado")
    localQdi = models.CharField(max_length=150, blank=True, null=True, default="nao encontrado")
    localQo = models.CharField(max_length=150, blank=True, null=True, default="nao encontrado")

    def __str__(self):  # __unicode__ for Python 2
        return self.user.username

    class Meta:
        verbose_name_plural = "Cadastro"

    # local = models.ForeignKey(Locais, blank=True,null=True,on_delete=models.CASCADE)
