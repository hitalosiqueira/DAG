# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Despesa',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('codigopais', models.IntegerField(null=True, blank=True)),
                ('dataano', models.IntegerField(null=True, blank=True)),
                ('datames', models.IntegerField(null=True, blank=True)),
                ('datadia', models.IntegerField(null=True, blank=True)),
                ('quantidadeparcelas', models.IntegerField(null=True, blank=True)),
                ('valor', models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=18)),
                ('descricaoorgao', models.CharField(max_length=255, null=True, blank=True)),
                ('cpfcnpjcredor', models.CharField(max_length=255, null=True, blank=True)),
                ('descricaoprograma', models.CharField(max_length=255, null=True, blank=True)),
                ('descricaodominio', models.CharField(max_length=255, null=True, blank=True)),
                ('descricaosubdominio', models.CharField(max_length=255, null=True, blank=True)),
                ('descricaofonte', models.CharField(max_length=255, null=True, blank=True)),
                ('descricaonatureza', models.CharField(max_length=255, null=True, blank=True)),
                ('descricaotipolicitacao', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'despesa',
            },
        ),
        migrations.CreateModel(
            name='Dominio',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'dominio',
            },
        ),
        migrations.CreateModel(
            name='Fonte',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'fonte',
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'municipio',
            },
        ),
        migrations.CreateModel(
            name='Natureza',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'natureza',
            },
        ),
        migrations.CreateModel(
            name='Orgao',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('descricaointernamunicipio', models.CharField(max_length=255, null=True, blank=True)),
                ('descricao', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'orgao',
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=100, null=True, blank=True)),
                ('sigla', models.CharField(max_length=3, null=True, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'pais',
            },
        ),
        migrations.CreateModel(
            name='Programa',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('descricaointernamunicipio', models.CharField(max_length=100, null=True, blank=True)),
                ('descricao', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'programa',
            },
        ),
        migrations.CreateModel(
            name='Subdominio',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'subdominio',
            },
        ),
        migrations.CreateModel(
            name='Tipodespesa',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'tipodespesa',
            },
        ),
        migrations.CreateModel(
            name='Tipolicitacao',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=100, null=True, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'tipolicitacao',
            },
        ),
        migrations.CreateModel(
            name='Uf',
            fields=[
                ('codigo', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(max_length=100, null=True, blank=True)),
                ('sigla', models.CharField(max_length=2, null=True, blank=True)),
            ],
            options={
                'managed': False,
                'db_table': 'uf',
            },
        ),
    ]
