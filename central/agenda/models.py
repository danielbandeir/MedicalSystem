from django.db import models
from paciente.models import paciente
from medico.models import medico, especializacao
import datetime

class agenda(models.Model):
    nomeMedico = models.ForeignKey(medico, blank=True, null=True, on_delete=models.SET_NULL)
    nomePaciente = models.ForeignKey(paciente, on_delete=models.CASCADE)
    especializacao = models.ForeignKey(especializacao, null=True, blank=True, on_delete=models.CASCADE)
    data = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return "{} - {} - {}".format(self.nomePaciente, self.nomeMedico, self.especializacao)