from django.contrib import admin
from professor.models import Professor

class Professores(admin.ModelAdmin):
    list_display = ('id', 'apelido',)
    list_display_links = ('id', 'apelido',)
    search_fields = ('apelido',)
    list_per_page = 20

admin.site.register(Professor, Professores)
