from rest_framework import viewsets
from .models import Diretor, Filme
from .serializers import DiretorSerializer, FilmeSerializer

class DiretorViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite visualizar, criar, editar e deletar diretores.
    """
    queryset = Diretor.objects.all().order_by('nome')
    serializer_class = DiretorSerializer
    filterset_fields = ['nacionalidade']
    search_fields = ['nome']


class FilmeViewSet(viewsets.ModelViewSet):
    """
    API endpoint que permite visualizar, criar, editar e deletar filmes.
    """
    queryset = Filme.objects.all().order_by('-ano_lancamento')
    serializer_class = FilmeSerializer
    filterset_fields = ['genero', 'ano_lancamento', 'diretor']
    search_fields = ['titulo', 'sinopse']