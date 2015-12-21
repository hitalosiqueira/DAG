# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Despesa(models.Model):
    codigo = models.AutoField(primary_key=True)
    codigomunicipio = models.ForeignKey('Municipio', db_column='codigomunicipio', blank=True, null=True)
    codigouf = models.ForeignKey('Uf', db_column='codigouf', blank=True, null=True)
    codigopais = models.IntegerField(blank=True, null=True)
    codigoorgao = models.ForeignKey('Orgao', db_column='codigoorgao', blank=True, null=True)
    codigoprograma = models.ForeignKey('Programa', db_column='codigoprograma', blank=True, null=True)
    codigotipodespesa = models.ForeignKey('Tipodespesa', db_column='codigotipodespesa', blank=True, null=True)
    codigodominio = models.ForeignKey('Dominio', db_column='codigodominio', blank=True, null=True)
    codigosubdominio = models.ForeignKey('Subdominio', db_column='codigosubdominio', blank=True, null=True)
    codigofonte = models.ForeignKey('Fonte', db_column='codigofonte', blank=True, null=True)
    codigonatureza = models.ForeignKey('Natureza', db_column='codigonatureza', blank=True, null=True)
    codigotipolicitacao = models.ForeignKey('Tipolicitacao', db_column='codigotipolicitacao', blank=True, null=True)
    dataano = models.IntegerField(blank=True, null=True)
    datames = models.IntegerField(blank=True, null=True)
    datadia = models.IntegerField(blank=True, null=True)
    quantidadeparcelas = models.IntegerField(blank=True, null=True)
    valor = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    descricaoorgao = models.CharField(max_length=255, blank=True, null=True)
    cpfcnpjcredor = models.CharField(max_length=255, blank=True, null=True)
    descricaoprograma = models.CharField(max_length=255, blank=True, null=True)
    descricaodominio = models.CharField(max_length=255, blank=True, null=True)
    descricaosubdominio = models.CharField(max_length=255, blank=True, null=True)
    descricaofonte = models.CharField(max_length=255, blank=True, null=True)
    descricaonatureza = models.CharField(max_length=255, blank=True, null=True)
    descricaotipolicitacao = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'despesa'


class Dominio(models.Model):
    codigo = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dominio'


class Fonte(models.Model):
    codigo = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fonte'


class Municipio(models.Model):
    codigo = models.AutoField(primary_key=True)
    codigouf = models.ForeignKey('Uf', db_column='codigouf', blank=True, null=True)
    descricao = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'municipio'


class Natureza(models.Model):
    codigo = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'natureza'


class Orgao(models.Model):
    codigo = models.AutoField(primary_key=True)
    descricaointernamunicipio = models.CharField(max_length=255, blank=True, null=True)
    descricao = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orgao'


class Pais(models.Model):
    codigo = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100, blank=True, null=True)
    sigla = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pais'


class Programa(models.Model):
    codigo = models.AutoField(primary_key=True)
    descricaointernamunicipio = models.CharField(max_length=100, blank=True, null=True)
    descricao = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'programa'


class Subdominio(models.Model):
    codigo = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subdominio'


class Tipodespesa(models.Model):
    codigo = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100, blank=True, null=True)
    codigodominio = models.ForeignKey(Dominio, db_column='codigodominio', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipodespesa'


class Tipolicitacao(models.Model):
    codigo = models.AutoField(primary_key=True)
    descricao = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipolicitacao'


class Uf(models.Model):
    codigo = models.AutoField(primary_key=True)
    codigopais = models.ForeignKey(Pais, db_column='codigopais', blank=True, null=True)
    descricao = models.CharField(max_length=100, blank=True, null=True)
    sigla = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'uf'
