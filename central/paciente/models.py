from django.db import models
from medico.models import medico

class paciente(models.Model):
    Nome = models.CharField(max_length=300, unique=True)
    rg = models.CharField(max_length=60, unique=True)
    cpf = models.CharField(max_length=80, unique=True)
    celular = models.CharField(max_length=80)
    telefone = models.CharField(max_length=80, blank=True)
    estado = models.CharField(max_length=300)
    cidade = models.CharField(max_length=300)
    sangue = models.CharField(max_length=300, blank=True)
    endereco = models.CharField(max_length=300)
    email = models.EmailField()

    def __str__(self):
        return self.Nome

class adicionarAtendimento(models.Model):
    nomePaciente = models.ForeignKey(paciente, blank=True, on_delete=models.CASCADE)
    nomeMedico = models.ForeignKey(medico, null=True, blank=True, on_delete=models.SET_NULL)
    data = models.DateField()
    hora = models.TimeField()
    descricao = models.TextField()

    def __str__(self):
        return '{} - {}'.format(self.nomePaciente, self.nomeMedico)
