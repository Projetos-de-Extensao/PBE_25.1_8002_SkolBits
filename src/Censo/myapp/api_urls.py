from rest_framework import routers
from myapp.api import IdentificacaoDomicilioViewSet, InformacoesMoradoresViewSet, CaracteristicasDomicilioViewSet

router = routers.DefaultRouter()
router.register(r'Identificação do domicílio', IdentificacaoDomicilioViewSet)
router.register(r'Inforamações de moradores', InformacoesMoradoresViewSet)
router.register(r'Características do domicílio', CaracteristicasDomicilioViewSet)


urlpatterns = router.urls