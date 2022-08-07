from django.db import models

class Receitas(models.Model):
    descricao = models.CharField(max_length=30)
    valor = models.FloatField(max_length=15)
    data = models.DateField()
    def __str__(self):
        return self.descricao

class Despesas(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.CharField(max_length=30)
    valor = models.FloatField(max_length=15)
    data = models.DateField()
    def __str__(self):
        return self.descricao

