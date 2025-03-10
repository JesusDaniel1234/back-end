# Generated by Django 5.0.3 on 2024-11-30 12:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ClaveConjunto",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("llave", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="TipoRiesgo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="RangoRiesgo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("rango", models.CharField(max_length=200)),
                (
                    "tipo_riesgo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="base.tiporiesgo",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ValorRiesgo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("valor", models.CharField(max_length=200)),
                ("orden", models.PositiveIntegerField()),
                (
                    "tipo_riesgo",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="base.tiporiesgo",
                    ),
                ),
            ],
        ),
    ]
