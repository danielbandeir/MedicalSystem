from django.db import models

class paciente(models.Model):
    Nome = models.CharField(max_length=300)
    endereco = models.CharField(max_length=300)
    email = models.EmailField()

    def __str__(self):
        return self.Nome
    