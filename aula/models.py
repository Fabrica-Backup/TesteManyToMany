from django.db import models
import datetime



class Ingrediente (models.Model):
    id_ingrediente = models.AutoField(primary_key = True)
    nome_ingrediente = models.CharField(max_length = 200)
    quantidade_calorica_ingrediente = models.DecimalField(max_digits = 6, decimal_places = 1)
    aproveitamento_ingrediente = models.DecimalField(max_digits = 4, decimal_places = 1)
    quantidade_estoque_ingrediente = models.DecimalField(max_digits = 12, decimal_places = 2, default = 0)
    quantidade_reservada_ingrediente = models.DecimalField(max_digits = 12, decimal_places = 2, default = 0)
    valor_ingrediente = models.DecimalField(max_digits = 12, decimal_places = 2, default = 0) 
    motivo_retirada_estoque = models.CharField(max_length = 200 , null = True)
    
    
    

class Aula (models.Model):
    id_aula = models.AutoField(primary_key = True)
    data_aula = models.DateField(default='01 de janeiro de 2000', null = True)
    descricao_aula = models.CharField(max_length = 200)
    aula_agendada = models.BooleanField(default= True)
    aula_concluida = models.BooleanField(default= True)
    periodo_aula = models.CharField(max_length = 100, null=True)
    ingredientes = models.ManyToManyField('Ingrediente', through='AulaIngrediente')
    #receitas = models.ManyToManyField(Receita, blank = True, related_name="AulaReceita", through="AulaIngrediente")


class AulaIngrediente (models.Model):
    id_aula_ingrediente = models.AutoField(primary_key = True)
    id_aula = models.ForeignKey('Aula')
    id_ingrediente = models.ForeignKey('Ingrediente')
    quantidade_projetada_aula = models.DecimalField(max_digits = 12, decimal_places = 2, default = 0) 
    quantidade_utilizada_aula = models.DecimalField(max_digits = 12, decimal_places = 2, default = 0) 

