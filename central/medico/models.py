from django.db import models

class medico(models.Model):
    nome = models.CharField(max_length=300)
    crm = models.CharField(max_length=300)

    def __str__(self):
        return self.nome