from rest_framework import serializers
from escola.models import Curso, Aula, Inscricao

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['id', 'codigo', 'nome', 'nivel', 'descricao']
