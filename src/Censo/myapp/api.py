from rest_framework import viewsets
from .models import Domicilio, Morador
from .serializers import DomicilioSerializer, MoradorSerializer

class DomicilioViewSet(viewsets.ModelViewSet):
    queryset = Domicilio.objects.all()
    serializer_class = DomicilioSerializer

class MoradorViewSet(viewsets.ModelViewSet):
    queryset = Morador.objects.all()
    serializer_class = MoradorSerializer

# Ao invés de escrever manualmente como criar, ler, atualizar e deletar dados, o ModelViewSet.
# Essa classe gera automaticamente todas as operações CRUD (Create, Read, Update, Delete).