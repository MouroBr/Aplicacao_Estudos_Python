from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Definição da tabela para armazenar informações dos hóspedes.

class Hospede(models.Model):
    cpf_hospede = models.CharField(max_length=11, primary_key=True, unique=True)
    nome_hospede = models.CharField(max_length=100, blank=False, null=False)
    data_nascimento_hospede = models.DateTimeField(blank=False, null=False)
    nacionalidade_hospede = models.CharField(max_length=50)
    tipo_documento_identidade_hospede = models.CharField(
        max_length=20,
        choices=[
            ("CPF", "CPF"),
            ("RG", "RG"),
            ("Passaporte", "Passaporte"),
            ("CNH", "CNH"),
        ],
    )
    numero_documento_identificacao_hospede = models.CharField(max_length=20)
    informacoes_contato = PhoneNumberField(blank=False, null=False)

    endereco_hospede = models.ForeignKey(
        "EnderecoHospede",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="hospedes",
    )

    def __str__(self):
        return f"{self.nome_hospede} ({self.cpf_hospede})"


class EnderecoHospede(models.Model):
    rua = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=10)
    anotacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.rua}, {self.numero} - {self.cidade}/{self.estado} - {self.cep}"
