from rest_framework import serializers
from myapp.models import  IndentificacaoDeDomicilio, InformacoesMoradores, CaracteristicasDomicilio, RegistroCivil, Nupcialidade, TrabalhoErendimento, Taxa_mortalidade


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

class RegistroCivilSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroCivil
        fields = '__all__'

class NupcialidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nupcialidade
        fields = '__all__'
class TrabalhoErendimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrabalhoErendimento
        fields = '__all__'
class Taxa_mortalidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Taxa_mortalidade
        fields = '__all__'