from rest_framework import serializers
from myapp.models import Domicilio, Morador, IndentificacaoDeDomicilio

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

