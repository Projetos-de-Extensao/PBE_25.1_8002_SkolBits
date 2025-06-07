from rest_framework import routers
from myapp.api import DomicilioViewSet

router = routers.DefaultRouter()
router.register(r'Domicílio', DomicilioViewSet)
# router.register(r'Inforamações de moradores', InformacoesMoradoresViewSet)
# router.register(r'Características do domicílio', CaracteristicasDomicilioViewSet)
# router.register(r'Características adicionais dos moradores', CaracteristicasAdicionaisMoradoresViewSet)


urlpatterns = router.urls