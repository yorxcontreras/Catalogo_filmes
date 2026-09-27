from django.db import models

class Diretor(models.Model):
    nome = models.CharField(max_length=100)
    nacionalidade = models.CharField(max_length=50, blank=True, null=True)
    data_nascimento = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Diretores"


class Filme(models.Model):
    GENEROS = [
        ('ACAO', 'Ação'),
        ('COMEDIA', 'Comédia'),
        ('DRAMA', 'Drama'),
        ('FICCAO', 'Ficção Científica'),
        ('TERROR', 'Terror'),
    ]

    titulo = models.CharField(max_length=150)
    sinopse = models.TextField(blank=True, null=True)
    ano_lancamento = models.IntegerField()
    genero = models.CharField(max_length=20, choices=GENEROS, default='DRAMA')
    
    # Relacionamento 1:N com a entidade Diretor
    diretor = models.ForeignKey(
        Diretor, 
        on_delete=models.CASCADE, 
        related_name='filmes'
    )

    def __str__(self):
        return self.titulo