from django.db import models


class LocalQo(models.Model):
    sigla = models.CharField(max_length=10,blank=True,null=True)
    nome = models.CharField(max_length=150,blank=True,null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Local Qo"


class LocalQdi(models.Model):
    sigla = models.CharField(max_length=10,blank=True,null=True)
    nome = models.CharField(max_length=150,blank=True,null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Local Qdi"


class Locais(models.Model):
    localQo = models.OneToOneField(LocalQo, on_delete=models.CASCADE,blank=True,null=True)
    localQdi = models.OneToOneField(LocalQdi, on_delete=models.CASCADE,blank=True,null=True)
    localAdido = models.CharField(max_length=150,blank=True,null=True)

    class Meta:
        verbose_name_plural = "Locais"
