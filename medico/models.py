from django.db import models


class especializacao(models.Model):
    nome = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.nome
        
class medico(models.Model):
    nome = models.CharField(max_length=300, unique=True)
    crm = models.CharField(max_length=300)
    especializacao = models.ForeignKey(especializacao, blank=True, null=True, on_delete=models.SET_NULL)
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
        return self.nome