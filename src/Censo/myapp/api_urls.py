from rest_framework import routers
from myapp.api import DomicilioViewSet
from myapp.api import MoradorViewSet

router = routers.DefaultRouter()
router.register(r'informacoesdomicilio', DomicilioViewSet)
router.register(r'informacoesmorador', MoradorViewSet)
# router.register(r'Características do domicílio', CaracteristicasDomicilioViewSet)
# router.register(r'Características adicionais dos moradores', CaracteristicasAdicionaisMoradoresViewSet)


urlpatterns = router.urls