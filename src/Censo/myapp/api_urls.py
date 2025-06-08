from rest_framework import routers
from myapp.api import IndentificacaoDeDomicilioViewSet, InformacoesMoradoresViewSet, CaracteristicasDomicilioViewSet, TrabalhoErendimentoViewSet, RegistroCivilViewSet, NupcialidadeViewSet, Taxa_mortalidadeViewSet, PessoaComDeficienciaViewSet, EducacaoViewSet, DeslocamentoParaTrabalhoViewSet, religiaoCultoViewSet, AutismoViewSet
router = routers.DefaultRouter()

router.register(r'IndentificacaoDomicilio', IndentificacaoDeDomicilioViewSet)  
router.register(r'InformacoesMoradores', InformacoesMoradoresViewSet)
router.register(r'CaracteristicasDomicilio', CaracteristicasDomicilioViewSet)
router.register(r'RegistroCivil', RegistroCivilViewSet)
router.register(r'Nupcialidade', NupcialidadeViewSet)
router.register(r'TrabalhoErendimento', TrabalhoErendimentoViewSet)
router.register(r'TaxaMortalidade', Taxa_mortalidadeViewSet)
router.register(r'PessoaComDeficiencia', PessoaComDeficienciaViewSet)
router.register(r'Educacao', EducacaoViewSet)
router.register(r'DeslocamentoParaTrabalho', DeslocamentoParaTrabalhoViewSet)
router.register(r'ReligiaoCulto', religiaoCultoViewSet)
router.register(r'Autismo', AutismoViewSet) 


urlpatterns = router.urls