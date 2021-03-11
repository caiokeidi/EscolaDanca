from django.contrib import admin
from aluno.models import Aluno


class Alunos(admin.ModelAdmin):
    list_display = ('id', 'primeiroNome', 'sobrenome', 'ativo')
    list_display_links = ('id', 'primeiroNome', 'sobrenome',)
    search_fields = ('primeiroNome',)
    list_per_page = 20

admin.site.register(Aluno, Alunos)
