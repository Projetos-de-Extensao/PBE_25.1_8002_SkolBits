from rest_framework import viewsets
from myapp.models import Domicilio
from myapp.serializers import DomicilioSerializer

class DomicilioViewSet(viewsets.ModelViewSet):
    queryset = Domicilio.objects.all()
    serializer_class = DomicilioSerializer

# class InformacoesMoradoresViewSet(viewsets.ModelViewSet):
#     queryset = InformacoesMoradores.objects.all()
#     serializer_class = InformacoesMoradoresSerializer
# class CaracteristicasDomicilioViewSet(viewsets.ModelViewSet):
#     queryset = CaracteristicasDomicilio.objects.all()
#     serializer_class = CaracteristicasDomicilioSerializer
# class CaracteristicasAdicionaisMoradoresViewSet(viewsets.ModelViewSet):
#     queryset = CaracteristicasAdicionaisMoradores.objects.all()
#     serializer_class = CaracteristicasAdicionaisMoradoresSerializer