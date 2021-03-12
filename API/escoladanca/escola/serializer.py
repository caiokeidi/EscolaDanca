from rest_framework import serializers
from escola.models import Curso, Aula, Inscricao

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['id', 'codigo', 'nome', 'nivel', 'descricao']

class AulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aula
        fields = "__all__"

class InscricaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscricao
        fields= "__all__"

class InscricoesDoAlunoSerializer(serializers.ModelSerializer):
    curso_nome = serializers.ReadOnlyField(source='aula.curso.nome')

    class Meta:
        model = Inscricao
        fields = ['curso_nome']