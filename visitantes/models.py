from pickle import FALSE
from statistics import mode
from django.db import models

# Create your models here.

class Visitante(models.Model):
    nome_completo = models.CharField(
        verbose_name="Nome completo",
        max_length=194
    )

    cpf = models.CharField(
        verbose_name="CPF",
        max_length=11
    )

    data_nascimento = models.DateField(
        verbose_name="Data de nascimento",
        auto_now=False,
        auto_now_add=False
    )

    numero_casa = models.PositiveSmallIntegerField(
        verbose_name="Numero da casa"
    )

    placa_veiculo = models.CharField(
        verbose_name="Placa de veiculo",
        max_length=7,
        blank=True,
        null=True
    )

    horario_chegada = models.DateTimeField(
        verbose_name="Horario de chegada na portaria",
        auto_now_add=True
    )

    horario_saida = models.DateTimeField(
        verbose_name="Horario de saida do condominio",
        auto_now=False,
        blank=True,
        null=True
    )

    horario_autorizacao = models.DateTimeField(
        verbose_name="Horario da autorizacao de entrada",
        auto_now=False,
        blank=True,
        null=True
    )

    morador_repsonsavel = models.CharField(
        verbose_name="Morador responsavel pela entrada do visitante",
        max_length=194,
        blank=True
    )

    registrado_por = models.ForeignKey(
        "porteiros.Porteiro",
        verbose_name="Porteiro responsavel pelo registro",
        on_delete=models.PROTECT
    )

    class Meta:
        verbose_name = "Visitante"
        verbose_name_plural = "Visitantes"
        db_table = "visitante"

    def __str__(self):
        return self.nome_completo
