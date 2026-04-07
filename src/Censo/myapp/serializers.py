from rest_framework import serializers
from .models import Domicilio, Morador

class MoradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Morador
        fields = '__all__'

class DomicilioSerializer(serializers.ModelSerializer):
    moradores = MoradorSerializer(many=True, read_only=True)

    class Meta:
        model = Domicilio
        fields = '__all__'

#O ModelSerializer funciona como um tradutor. Ele pega os objetos complexos do seu banco de dados (as instâncias de Domicilio e Morador) e os converte em um formato de texto leve, o JSON, que é o padrão da web. Usar fields = '__all__' garante que todos os campos que você definiu lá no models.py sejam incluídos automaticamente nessa tradução, poupando você de digitar um por um.