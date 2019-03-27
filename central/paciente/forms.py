from django.forms import ModelForm, DateInput, TimeInput
from .models import paciente, adicionarAtendimento

class pacienteForm(ModelForm):
    class Meta:
        model = paciente
        fields = '__all__'

class adicionarAtendimentoForm(ModelForm):
    class Meta:
        model = adicionarAtendimento
        fields = '__all__'
        widgets = {
            'data': DateInput(attrs={'class': 'datepicker'}),
            'hora': TimeInput(attrs={'type': 'time'})
        }