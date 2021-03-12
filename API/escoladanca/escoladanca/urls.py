
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from escola.views import CursosViewSet, AulasViewSet, InscricoesViewSet

router = routers.DefaultRouter()
router.register('cursos', CursosViewSet, basename='Cursos')
router.register('aulas', AulasViewSet, basename='Aulas')
router.register('inscricoes', InscricoesViewSet, basename='Inscrições')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
