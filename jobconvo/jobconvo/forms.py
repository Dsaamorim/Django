from django.forms import ModelForm
from jobconvo.models import *
from jobconvo.models import vagaDeEmprego
from django import forms

class createVagaForm(ModelForm):
    class Meta:
        model = vagaDeEmprego
        fields = [
        "nameJob",
        "cbFaixaSalarial",
        "cbEscolaridade",
    ]

FAIXA_SALARIAL_CHOICE = (
    (('faixa1', 'R$1.000')),
    (('faixa2','R$1.000 a R$2.000')),
    (('faixa3','R$2.000 a R$3.000')),
    (('faixa4','Acima de R$3.000')),
    )

NIVEL_ESCOLAR_CHOICE = (
    (('faixa5', 'Ensino fundamental')),
    (('faixa6', 'Ensino médio')),
    (('faixa7', 'Tecnólogo')),
    (('faixa8', 'Ensino Superior')),
    (('faixa9', 'Pós/MBA/Mestrado')),
    (('faixa10', 'Doutorado')),
    )

class createFaixaSalarialChoice(ModelForm):
    cbFaixaSalarial = forms.ChoiceField(choices=FAIXA_SALARIAL_CHOICE)

class createNivelEscolarChoice(ModelForm):
    cbEscolaridade = forms.ChoiceField(choices=NIVEL_ESCOLAR_CHOICE)






        



