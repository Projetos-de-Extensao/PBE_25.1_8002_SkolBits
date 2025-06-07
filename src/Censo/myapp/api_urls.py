from rest_framework import routers
from myapp.api import DomicilioViewSet
from myapp.api import MoradorViewSet

router = routers.DefaultRouter()
router.register(r'Informações do domicílio', DomicilioViewSet)
router.register(r'Informações de morador', MoradorViewSet)
# router.register(r'Características do domicílio', CaracteristicasDomicilioViewSet)
# router.register(r'Características adicionais dos moradores', CaracteristicasAdicionaisMoradoresViewSet)


urlpatterns = router.urls