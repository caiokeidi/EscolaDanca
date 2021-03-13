from django.urls import path, include
from escola.views import InscricoesDoAluno
urlpatterns = [
    path('matriculas/aluno/<int:pk>', InscricoesDoAluno.as_view(), name='inscricoes_aluno')
]