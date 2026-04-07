from django.urls import path
from myproject.urls import schema_view

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

#Aqui está a interface gráfica interativa do Swagger, onde você pode testar as rotas da API diretamente do navegador.
