from django.contrib import admin
from escola.models import Curso, Inscricao, Aula


class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'nome', 'nivel')
    list_display_links = ('id', 'codigo', 'nome')
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Curso, Cursos)

class Aulas(admin.ModelAdmin):
    list_display = ('id', 'curso', 'diaSemana', 'horario', 'professor', 'ativo')
    list_display_links = ('id', 'curso',)
    search_fields = ('curso',)
    list_per_page = 20

admin.site.register(Aula, Aulas)

class Inscricoes(admin.ModelAdmin):
    list_display = ('id', 'aluno', 'aula',)
    list_display_links = ('id', 'aluno', 'aula',)
    search_fields = ('aluno',)
    list_per_page = 25

admin.site.register(Inscricao, Inscricoes)