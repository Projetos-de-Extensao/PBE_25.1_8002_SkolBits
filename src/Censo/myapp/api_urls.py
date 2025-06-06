from rest_framework import routers
from myapp.api import IdentificacaoDomicilioViewSet, InformacoesMoradoresViewSet, CaracteristicasDomicilioViewSet, CaracteristicasAdicionaisMoradoresViewSet

router = routers.DefaultRouter()
router.register(r'Identificação do domicílio', IdentificacaoDomicilioViewSet)
router.register(r'Inforamações de moradores', InformacoesMoradoresViewSet)
router.register(r'Características do domicílio', CaracteristicasDomicilioViewSet)
router.register(r'Características adicionais dos moradores', CaracteristicasAdicionaisMoradoresViewSet)


urlpatterns = router.urls