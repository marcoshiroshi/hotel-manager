from django.db import models

class Quarto(models.Model):
    id = models.AutoField(primary_key=True)
    andar = models.IntegerField()
    numero = models.IntegerField()
    tipo_quarto = [
        ('Apartamento','Apartamento'),
        ('Suíte','Suíte'),
        ('Normal','Normal'),
        ('Pernoite','Pernoite')
    ]
    tipo = models.CharField(max_length=15, choices=tipo_quarto)
    descrição= models.TextField(max_length=200)
    quantidade_pessoas = models.IntegerField()
    custo = models.FloatField()
