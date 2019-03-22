from django.db import models
from paciente.models import paciente
from medico.models import medico

class agenda(models.Model):
    nomeMedico = models.ForeignKey(medico, on_delete=models.CASCADE)
    nomePaciente = models.ForeignKey(paciente, on_delete=models.CASCADE)
    data = models.DateField()
    hora = models.TimeField()

    def __str__(self):
        return "{} - {}".format(self.nomePaciente, self.nomeMedico)