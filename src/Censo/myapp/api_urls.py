from rest_framework import routers
from myapp.api import IndentificacaoDeDomicilioViewSet, InformacoesMoradoresViewSet, CaracteristicasDomicilioViewSet, RegistroCivilViewSet, NupcialidadeViewSet

router = routers.DefaultRouter()

router.register(r'IndentificacaoDomicilio', IndentificacaoDeDomicilioViewSet)  
router.register(r'InformacoesMoradores', InformacoesMoradoresViewSet)
router.register(r'CaracteristicasDomicilio', CaracteristicasDomicilioViewSet)
router.register(r'RegistroCivil', RegistroCivilViewSet)
router.register(r'Nupcialidade', NupcialidadeViewSet)

urlpatterns = router.urls