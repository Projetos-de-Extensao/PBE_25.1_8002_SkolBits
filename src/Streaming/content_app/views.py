from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Bem-vindo à Plataforma de Streaming!</h1><p>Esta é a página inicial.</p>")

# Create your views here.
from rest_framework import viewsets
from .models import Content
from .serializers import ContentSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    #permission_classes = [IsAuthenticatedOrReadOnly]

    #def perform_create(self, serializer):
        #serializer.save(creator=self.request.user)