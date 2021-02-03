from django.db import models
import datetime
from quartos.models import Quarto

class Pessoa(models.Model):
    cpf = models.CharField(max_length=14, primary_key=True)
    nome = models.CharField(max_length=100)
    tipo_genero = [
        ('H','Homem'),
        ('M','Mulher'),
        ('O','Outro'),
    ]
    genero = models.CharField(max_length=15, choices=tipo_genero)
    dt_nasc = models.DateField()
    numero = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    tipo_funcao = [
        ('1','Gerente'),
        ('2','Recepcionista'),
        ('3','cozinheiro'),
        ('4','faxineiro'),
        ('5','cliente'),
    ]
    funcao = models.CharField(max_length=10, choices=tipo_funcao)
    quarto = models.ForeignKey(Quarto, on_delete=models.CASCADE)
    salario = models.FloatField(default=0)
    dt_chegada = models.DateTimeField()
    dt_saida = models.DateTimeField()


