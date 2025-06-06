from rest_framework import serializers
from myapp.models import IdentificacaoDomicilio, InformacoesMoradores, CaracteristicasDomicilio, CaracteristicasAdicionaisMoradores

class IdentificacaoDomicilioSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdentificacaoDomicilio
        fields = '__all__'

class InformacoesMoradoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformacoesMoradores
        fields = '__all__'

class CaracteristicasDomicilioSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaracteristicasDomicilio
        fields = '__all__'
        
class CaracteristicasAdicionaisMoradoresSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaracteristicasAdicionaisMoradores
        fields = '__all__'