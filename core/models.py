from django.db import models

class Test(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.IntegerField()
    estoque= models.IntegerField()

    def __str__(self):
        return self.nome