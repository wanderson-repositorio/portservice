"""
Definition of models.
"""

from django.db import models

class Lema(models.Model):
    identificador = models.AutoField('identificador',primary_key=True)
    lema = models.CharField('lema',max_length=200)

    class Meta:
        db_table = "lema"

class Flexao(models.Model):
    identificador = models.AutoField('identificador',primary_key=True)
    flexao = models.CharField('lema',max_length=200)
    id_lema = models.ForeignKey(Lema)
   

    class Meta:
        db_table = "flexao"

class Propriedade(models.Model):
    identificador = models.AutoField('identificador',primary_key=True)
    classe_gramatical = models.CharField('classe_gramatical',max_length=10)
    sub_classe = models.CharField('sub_classe',max_length=10)
    tempo = models.CharField('tempo',max_length=10)
    pessoa = models.CharField('pessoa',max_length=10)
    numero = models.CharField('numero',max_length=10)
    genero = models.CharField('genero',max_length=10)
    modo = models.CharField('modo',max_length=10) 
    tipo = models.CharField('tipo',max_length=10) 

    class Meta:
        db_table = "propriedade"



class Flexao_Propriedade(models.Model):
    id_flexao = models.ForeignKey(Flexao)
    id_propriedade = models.ForeignKey(Propriedade)

    class Meta:
        db_table = "flexao_propriedade"
        unique_together = (("id_flexao", "id_propriedade"),)
