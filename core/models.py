from django.db import models

class Viagem(models.Model):
    data_partida = models.DateTimeField()
    duracao = models.DurationField()
    origem = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f'{self.origem}-{self.destino} em {self.data_partida} / R${self.preco}'
