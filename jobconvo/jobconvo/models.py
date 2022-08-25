from django.db import models

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

class vagaDeEmprego(models.Model):
    FAIXA_SALARIAL = [
    ('R$1.000', 'R$1.000 a R$2.000'),
    ('R$2.000 a R$3.000', 'Acima de R$3.000'),
    ]
    ESCOLARIDADE = [ ('Ensino fundamental', 'Ensino médio', 'Tecnólogo'),
    ('Ensino Superior', 'Pós/MBA/Mestrado', 'Doutorado'),
    ]

class vagaDeEmprego(models.Model):
    nameJob = models.CharField(max_length=100)
    cbFaixaSalarial = models.CharField(max_length=4)
    cbEscolaridade = models.CharField(max_length=4)

def __str__(self):
    return self.nameJob