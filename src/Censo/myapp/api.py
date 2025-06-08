from rest_framework import viewsets
from myapp.models import  IndentificacaoDeDomicilio, InformacoesMoradores, CaracteristicasDomicilio, RegistroCivil, Nupcialidade, TrabalhoErendimento, Taxa_mortalidade, PessoaComDeficiencia, Educacao
from myapp.serializers import  IndentificacaoDeDomicilioSerializer, IndentificacaoDeDomicilio, InformacoesMoradoresSerializer,  CaracteristicasDomicilioSerializer, RegistroCivilSerializer, NupcialidadeSerializer, TrabalhoErendimentoSerializer, Taxa_mortalidadeSerializer, pessoaComDeficienciaSerializer, EducacaoSerializer


class IndentificacaoDeDomicilioViewSet(viewsets.ModelViewSet):
    queryset = IndentificacaoDeDomicilio.objects.all()
    serializer_class = IndentificacaoDeDomicilioSerializer

class InformacoesMoradoresViewSet(viewsets.ModelViewSet):
    queryset = InformacoesMoradores.objects.all()
    serializer_class = InformacoesMoradoresSerializer

class CaracteristicasDomicilioViewSet(viewsets.ModelViewSet):
    queryset = CaracteristicasDomicilio.objects.all()
    serializer_class = CaracteristicasDomicilioSerializer

class RegistroCivilViewSet(viewsets.ModelViewSet):
    queryset = RegistroCivil.objects.all()
    serializer_class = RegistroCivilSerializer

class NupcialidadeViewSet(viewsets.ModelViewSet):
    queryset = Nupcialidade.objects.all()
    serializer_class = NupcialidadeSerializer

class TrabalhoErendimentoViewSet(viewsets.ModelViewSet):
    queryset = TrabalhoErendimento.objects.all()
    serializer_class = TrabalhoErendimentoSerializer

class Taxa_mortalidadeViewSet(viewsets.ModelViewSet):
    queryset = Taxa_mortalidade.objects.all()
    serializer_class = Taxa_mortalidadeSerializer
class PessoaComDeficienciaViewSet(viewsets.ModelViewSet):
    queryset = PessoaComDeficiencia.objects.all()
    serializer_class = pessoaComDeficienciaSerializer
class EducacaoViewSet(viewsets.ModelViewSet):
    queryset = Educacao.objects.all()
    serializer_class = EducacaoSerializer  