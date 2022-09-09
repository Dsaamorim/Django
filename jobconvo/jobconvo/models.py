from django.db import models
from django import forms
from .models import models

FAIXA_SALARIAL_CHOICE = (
    (('faixa1', 'R$1.000')),
    (('faixa2','R$1.000 a R$2.000')),
    (('faixa3','R$2.000 a R$3.000')),
    (('faixa4','Acima de R$3.000')),
    )

class vagaDeEmprego(models.Model):
    nameJob = models.CharField(max_length=200)
    cbFaixaSalarial = models.CharField(max_length=25, choices=FAIXA_SALARIAL_CHOICE)

