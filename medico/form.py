from django.forms import ModelForm
from .models import medico, especializacao

class medicoForm(ModelForm):
    class Meta:
        model = medico
        fields = '__all__'

class especializacaoForm(ModelForm):
    class Meta:
        model = especializacao
        fields = '__all__'