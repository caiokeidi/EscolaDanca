from django.shortcuts import render
from rest_framework import viewsets, generics
from escola.models import Curso, Aula, Inscricao
from escola.serializer import CursoSerializer, AulaSerializer, InscricaoSerializer, InscricoesDoAlunoSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# class AlunosViewSet(viewsets.ModelViewSet):
#     """Exibindo todos os alunos e alunas"""
#     queryset = Aluno.objects.all()
#     serializer_class = AlunoSerializer
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAuthenticated]

class CursosViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class AulasViewSet(viewsets.ModelViewSet):
    queryset = Aula.objects.all()
    serializer_class = AulaSerializer

class InscricoesViewSet(viewsets.ModelViewSet):
    queryset = Inscricao.objects.all()
    serializer_class = InscricaoSerializer

class InscricoesDoAluno(generics.ListAPIView):
    def get_queryset(self):
        queryset = Inscricao.objects.filter(aluno_id = self.kwargs['pk'])
        return queryset
    serializer_class = InscricoesDoAlunoSerializer