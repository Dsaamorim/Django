from django.db import models
import requests

#class vagasDeEmprego(models.Model):

#    nameJob = models.CharField(
#    max_length=255,
#    null=False,
#    blank=False
#  )
#    cbFaixaSalarial = models.CharField(
#    max_length=255,
#    null=False,
#    blank=False
#  )
#    cbEscolaridade = models.CharField(
#    max_length=255,
#    null=False,
#    blank=False
#  )

#objetos = models.Manager()

#class vagaDeEmprego(models.Model):
    #cbFaixaSalarial = [
    #('R$1.000', 'R$1.000 a R$2.000'),
    #('R$2.000 a R$3.000', 'Acima de R$3.000'),
    #]
    #cbEscolaridade = [ 
    #('Ensino fundamental', 'Ensino médio', 'Tecnólogo'),
    #('Ensino Superior', 'Pós/MBA/Mestrado', 'Doutorado'),
    #]

class vagaDeEmprego(models.Model):
    nameJob = models.CharField(max_length=200)
    cbFaixaSalarial = models.CharField(max_length=200)
    cbEscolaridade = models.CharField(max_length=200)

def __str__(self):
    return self.nameJob 



