from django.shortcuts import render
from rest_framework import viewsets
from escola.models import Curso, Aula, Inscricao
from escola.serializer import CursoSerializer

# class AlunosViewSet(viewsets.ModelViewSet):
#     """Exibindo todos os alunos e alunas"""
#     queryset = Aluno.objects.all()
#     serializer_class = AlunoSerializer
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAuthenticated]

class CursosViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    