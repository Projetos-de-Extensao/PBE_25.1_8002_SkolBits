from rest_framework import serializers
from myapp.models import  IndentificacaoDeDomicilio, InformacoesMoradores, CaracteristicasDomicilio


class IndentificacaoDeDomicilioSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndentificacaoDeDomicilio
        fields = '__all__'
class InformacoesMoradoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformacoesMoradores
        fields = '__all__'
class CaracteristicasDomicilioSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaracteristicasDomicilio
        fields = '__all__'