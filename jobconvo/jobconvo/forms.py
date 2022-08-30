from dataclasses import fields
from django import forms
from .models import vagaDeEmprego
 
FAIXA_SALARIAL = [
    ('R$1.000', 'R$1.000 a R$2.000'),
    ('R$2.000 a R$3.000', 'Acima de R$3.000'),
]

ESCOLARIDADE = [ ('Ensino fundamental', 'Ensino médio', 'Tecnólogo'),
('Ensino Superior', 'Pós/MBA/Mestrado', 'Doutorado'),
]
 
class createVagaForm(forms.ModelForm):
    class Meta:
        model = vagaDeEmprego
        fields = [
        "nameJob",
        "cbFaixaSalarial",
        "cbEscolaridade",
        #nameJob = forms.CharField(max_length=100)
        #cbFaixaSalarial = forms.ChoiceField(choices=FAIXA_SALARIAL, label='Faixa Salarial: ', widget=forms.RadioSelect(choices=FAIXA_SALARIAL), initial='R$1.000')
        #cbEscolaridade = forms.ChoiceField(choices=ESCOLARIDADE, label='Escolaridade: ', widget=forms.RadioSelect(choices=ESCOLARIDADE), initial='Ensino fundamental')
        ]