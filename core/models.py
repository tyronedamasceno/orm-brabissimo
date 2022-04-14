from django.db import models

class Viagem(models.Model):
    data_partida = models.DateTimeField()
    duracao = models.DurationField()
    origem = models.CharField(max_length=100)
    destino = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    onibus = models.ForeignKey("core.Onibus", on_delete=models.SET_NULL, null=True)


    def __str__(self) -> str:
        return f'{self.origem}-{self.destino} em {self.data_partida} / R${self.preco}'


class Onibus(models.Model):
    placa = models.CharField(max_length=7)
    marca = models.CharField(max_length=100)
    ano = models.IntegerField()
    empresa = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.placa


class Classe(models.Model):
    class TipoAssento(models.TextChoices):
        EXECUTIVO = 'EXECUTIVO'
        SEMI_LEITO = 'SEMI_LEITO'
        LEITO = 'LEITO'
        CAMA = 'CAMA'
        CAMA_PREMIUM = 'CAMA_PREMIUM'

    tipo = models.CharField(max_length=50, choices=TipoAssento.choices)
    vagas = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    viagem = models.ForeignKey("core.Viagem", on_delete=models.SET_NULL, null=True)
