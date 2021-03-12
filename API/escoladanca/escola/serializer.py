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
    curso = serializers.ReadOnlyField(source='aula.curso.nome')
    aula_diaSemana = serializers.SerializerMethodField()
    horario = serializers.ReadOnlyField(source='aula.horario')
    professor = serializers.ReadOnlyField(source='aula.professor.apelido')

    class Meta:
        model = Inscricao
        fields = ['curso','aula_diaSemana', 'horario', 'professor']
    
    def get_aula_diaSemana(self, obj):
        return obj.aula.get_diaSemana_display() 

    


class AlunosMatriculadosEmCursoSerializer(serializers.ModelSerializer):
    aluno_id = serializers.ReadOnlyField(source='aluno.id')
    aluno_nome = serializers.ReadOnlyField(source='aluno.primeiroNome')
    aluno_sobrenome = serializers.ReadOnlyField(source='aluno.sobrenome')

    class Meta:
        model = Inscricao
        fields = ['aluno_nome','aluno_id', 'aluno_sobrenome']