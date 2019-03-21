from django.forms import ModelForm
from .models import paciente

class pacienteForm(ModelForm):
    class Meta:
        model = paciente
        fields = '__all__'