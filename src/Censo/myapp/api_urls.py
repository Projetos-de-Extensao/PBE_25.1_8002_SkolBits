from rest_framework import routers
from myapp.api import IndentificacaoDeDomicilioViewSet, InformacoesMoradoresViewSet, CaracteristicasDomicilioViewSet, RegistroCivilViewSet, NupcialidadeViewSet, TrabalhoErendimentoViewSet

router = routers.DefaultRouter()

router.register(r'IndentificacaoDomicilio', IndentificacaoDeDomicilioViewSet)  
router.register(r'InformacoesMoradores', InformacoesMoradoresViewSet)
router.register(r'CaracteristicasDomicilio', CaracteristicasDomicilioViewSet)
router.register(r'RegistroCivil', RegistroCivilViewSet)
router.register(r'Nupcialidade', NupcialidadeViewSet)
router.register(r'TrabalhoErendimento', TrabalhoErendimentoViewSet)

urlpatterns = router.urls