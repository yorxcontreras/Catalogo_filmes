from rest_framework import serializers
from .models import Diretor, Filme

class FilmeSerializer(serializers.ModelSerializer):
    # Campo apenas para leitura que exibe o nome do diretor no GET do filme
    diretor_nome = serializers.ReadOnlyField(source='diretor.nome')

    class Meta:
        model = Filme
        fields = [
            'id', 
            'titulo', 
            'sinopse', 
            'ano_lancamento', 
            'genero', 
            'diretor', 
            'diretor_nome'
        ]

class DiretorSerializer(serializers.ModelSerializer):
    # Serializador aninhado para leitura dos filmes associados a este diretor
    filmes = FilmeSerializer(many=True, read_only=True)

    class Meta:
        model = Diretor
        fields = ['id', 'nome', 'nacionalidade', 'data_nascimento', 'filmes']