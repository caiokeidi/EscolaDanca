from django.db import models

class Professor(models.Model):
    objects = models.Manager()
    apelido = models.CharField(max_length=50)
    nomeCompleto = models.CharField(max_length=110)
    descricao = models.TextField(max_length=500)

    def __str__(self):
        return self.apelido
