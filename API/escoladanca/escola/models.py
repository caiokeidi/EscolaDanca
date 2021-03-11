from django.db import models
from aluno.models import Aluno
from professor.models import Professor

class Curso(models.Model):
    objects = models.Manager()

    NIVEL = (
        ('I1', 'Infantil 1'),
        ('I2', 'Infantil 2'),
        ('B1', 'Básico 1'),
        ('B2', 'Básico 2'),
        ('I1', 'Intermediário 1'),
        ('I2', 'Intermediário 2'),
        ('I3', 'Intermediário 3'),
        ('A1', 'Avançado 1'),
        ('A2', 'Avançado 2'),
        ('A3', 'Avançado 3'),
        ('P', 'Profissional'),
        ('O', 'Outro'),
    )
    codigo = models.CharField(max_length=5)
    nome = models.CharField(max_length=50)
    nivel = models.CharField(max_length=2, choices=NIVEL, blank=False, null=False, default='B1')
    descricao = models.TextField(max_length=300)

    def __str__(self):
        return self.nome

class Classe(models.Model):
    SEMANA = (
        ('SG', 'Segunda-Feira'),
        ('TR', 'Terça-Feira'),
        ('QA', 'Quarta-Feira'),
        ('QI', 'Quinta-Feira'),
        ('SE', 'Sexta-Feira'),
        ('SA', 'Sábado'),
        ('DM', 'Domingo'),
    )
    

    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    diaSemana = models.CharField(max_length=2, choices=SEMANA, blank=False, null=False, default='SG')
    horario = models.TimeField()
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    mensalidade = models.FloatField()
    ativo = models.BooleanField(default=True)
    

    





