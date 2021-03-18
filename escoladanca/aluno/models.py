from django.db import models
from django.contrib.auth.models import User



class Aluno(models.Model):
    objects = models.Manager()

    primeiroNome = models.CharField(max_length=20)
    sobrenome = models.CharField(max_length=80)
    dataNascimento = models.DateField()
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=11)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.primeiroNome

class AlunoSite(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    alunoSite = models.ForeignKey(User, on_delete=models.CASCADE)

    


