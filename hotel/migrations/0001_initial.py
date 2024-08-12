# Generated by Django 5.1 on 2024-08-10 03:19

import django.db.models.deletion
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="EnderecoHospede",
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
                ("rua", models.CharField(max_length=255)),
                ("numero", models.CharField(max_length=10)),
                ("cidade", models.CharField(max_length=100)),
                ("estado", models.CharField(max_length=2)),
                ("cep", models.CharField(max_length=10)),
                ("anotacoes", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Hospede",
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
                ("nome_hospede", models.CharField(max_length=100)),
                ("data_nascimento_hospede", models.DateTimeField()),
                ("nacionalidade_hospede", models.CharField(max_length=50)),
                (
                    "tipo_documento_identidade_hospede",
                    models.CharField(
                        choices=[
                            ("CPF", "CPF"),
                            ("RG", "RG"),
                            ("Passaporte", "Passaporte"),
                            ("CNH", "CNH"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "numero_documento_identificacao_hospede",
                    models.CharField(max_length=20),
                ),
                (
                    "informacoes_contato",
                    phonenumber_field.modelfields.PhoneNumberField(
                        max_length=128, region=None
                    ),
                ),
                (
                    "endereco_hospede",
                    models.OneToOneField(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="hospede",
                        to="hotel.enderecohospede",
                    ),
                ),
            ],
        ),
    ]
