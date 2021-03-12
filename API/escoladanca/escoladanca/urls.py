
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from escola.views import CursosViewSet, AulasViewSet, InscricoesViewSet
from professor.views import ProfessoresViewSet
from aluno.views import AlunoViewSet
from escola import urls as escolaURLS


router = routers.DefaultRouter()
router.register('cursos', CursosViewSet, basename='Cursos')
router.register('aulas', AulasViewSet, basename='Aulas')
router.register('inscricoes', InscricoesViewSet, basename='Inscrições')
router.register('professores', ProfessoresViewSet, basename='Professores')
router.register('alunos', AlunoViewSet, basename='Alunos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('escola/', include(escolaURLS))

]
