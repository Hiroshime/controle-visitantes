from django import forms
from visitantes.models import Visitante

class VisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = ("nome_completo","cpf","data_nascimento","numero_casa","placa_veiculo")
        error_messages = {
            "nome_completo":{"required": "O nome completo do visitante é obrigatorio."},
            "cpf":{"required": "O CPF do visitante é obrigatorio."},
            "data_nascimento":{"required": "A data de nascimento do visitante é obrigatoria.","invalid":"por favor informe uma data valida (DD/MM/AAAA)"},
            "numero_casa":{"required": "O numero da casa é obrigatorio."}
        }