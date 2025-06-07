from rest_framework import serializers
from myapp.models import Domicilio, Morador, IndentificacaoDeDomicilio, InformacoesMoradores

class DomicilioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domicilio
        fields = '__all__'

class MoradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Morador
        fields = '__all__'
class IndentificacaoDeDomicilioSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndentificacaoDeDomicilio
        fields = '__all__'
class InformacoesMoradoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformacoesMoradores
        fields = '__all__'
