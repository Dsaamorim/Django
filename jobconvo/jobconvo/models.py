from django.db import models

class vagasDeEmprego(models.Model):

    nameJob = models.CharField(
    max_length=255,
    null=False,
    blank=False
  )
    cbFaixaSalarial = models.CharField(
    max_length=255,
    null=False,
    blank=False
  )
    cbEscolaridade = models.CharField(
    max_length=255,
    null=False,
    blank=False
  )

objetos = models.Manager()