from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from locais.models import Locais


class Cadastro(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    postoGraduacao = models.CharField(blank=True,null=True,max_length=12)
    nome = models.CharField(blank=True,null=True,max_length=90)
    oficial = models.BooleanField(blank=True,null=True)
    nomeGuerra = models.CharField(blank=True,null=True,max_length=30)
    numeroFuncional = models.CharField(blank=True,null=True,max_length=10)
    cpf = models.CharField(blank=True,null=True,max_length=15)
    localQdi = models.CharField(max_length=150,blank=True,null=True)
    localQo = models.CharField(max_length=150,blank=True,null=True)

    #local = models.ForeignKey(Locais, blank=True,null=True,on_delete=models.CASCADE)


@receiver(post_save, sender=User)
def create_or_update_user_cadastro(sender, instance, created, **kwargs):
    if created:
        Cadastro.objects.create(user=instance)
    instance.cadastro.save()
