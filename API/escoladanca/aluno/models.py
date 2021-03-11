from django.db import models

class Aluno(models.Model):
    objects = models.Manager()
    
    primeiroNome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=80)
    dataNascimento = models.DateField()
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=11)

    def __str__(self):
        return self.primeiroNome

