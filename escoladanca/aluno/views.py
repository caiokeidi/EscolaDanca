from django.shortcuts import render
from aluno.serializer import AlunoSerializer
from rest_framework import viewsets
from aluno.models import Aluno
from escola.models import Inscricao

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


