from django.db import models

class Quarto(models.Model):
    id_quarto = models.CharField(max_length=10, primary_key=True)
    andar = models.IntegerField()
    numero = models.IntegerField()
    tipo_quarto = [
        ('1','Apartamento'),
        ('2','Suíte'),
        ('3','Normal'),
        ('4','Pernoite')
    ]
    tipo = models.CharField(max_length=15, choices=tipo_quarto)
    descrição= models.TextField(max_length=200)
    n_pessoas = models.CharField(max_length=50)
    custo = models.FloatField()
