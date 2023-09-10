from django.db import models

class Categoria(models.Model):
    categoria = models.CharField(max_length=50)
    essencial = models.BooleanField(default=False)
    valor_planejamento = models.FloatField(default=0)

    def __str__(self):
        return self.categoria
# Criar os models aqui.

class Conta(models.Model):
    banco_choices = (
       ('PAN', 'PanAmericano'),
       ('CE', 'Caixa Economica') 
    )

    tipo_choices = (
        ('pf', 'Pessoa Física'),
        ('pj', 'Pessoa Jurídica')
    )

    apelido= models.CharField(max_length=50)
    banco = models.CharField(max_length=3, choices=banco_choices)
    tipo = models.CharField(max_length=2, choices=tipo_choices)
    valor = models.FloatField()
    icone = models.ImageField(upload_to="icones")

    def __str__(self):
        return self.apelido
