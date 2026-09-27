from django.contrib import admin
from .models import Diretor, Filme

@admin.register(Diretor)
class DiretorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'nacionalidade', 'data_nascimento')
    search_fields = ('nome',)

@admin.register(Filme)
class FilmeAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'genero', 'ano_lancamento', 'diretor')
    list_filter = ('genero', 'ano_lancamento')
    search_fields = ('titulo', 'sinopse')