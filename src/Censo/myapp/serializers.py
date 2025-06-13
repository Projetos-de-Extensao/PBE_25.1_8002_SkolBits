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