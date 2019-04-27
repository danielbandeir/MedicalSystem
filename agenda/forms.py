from django.forms import ModelForm, DateInput, TimeInput,DateField
from .models import agenda
from paciente.models import paciente
from medico.models import medico

class agendaForm(ModelForm):
    class Meta:
        model = agenda
        fields = '__all__'
        widgets = {
            'data': DateInput(attrs={'class': 'datepicker'}),
            'hora': TimeInput(attrs={'type': 'time'})
        }