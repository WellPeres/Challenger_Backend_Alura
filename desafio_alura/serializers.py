from rest_framework import serializers
from desafio_alura.models import Despesas, Receitas


class ReceitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receitas
        fields = ['id', 'descricao', 'valor', 'data',]

class DespesasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despesas
        fields = ['id', 'descricao', 'valor', 'data',]
