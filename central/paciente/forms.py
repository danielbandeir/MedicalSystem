from django import forms
from .models import paciente

class pacienteForm(forms.Form):
    class Meta:
        model = paciente
        fields =[
            'nome',
            'endereco',
            'email'
        ]
