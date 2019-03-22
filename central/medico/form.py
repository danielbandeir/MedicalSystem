from django.forms import ModelForm
from .models import medico

class medicoForm(ModelForm):
    class Meta:
        model = medico
        fields = '__all__'