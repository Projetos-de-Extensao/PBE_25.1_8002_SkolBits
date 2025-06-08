from rest_framework import routers
from myapp.api import IndentificacaoDeDomicilioViewSet, InformacoesMoradoresViewSet, CaracteristicasDomicilioViewSet, TrabalhoErendimentoViewSet, RegistroCivilViewSet, NupcialidadeViewSet, Taxa_mortalidadeViewSet, PessoaComDeficienciaViewSet, EducacaoViewSet, DeslocamentoParaTrabalhoViewSet, religiaoCultoViewSet, AutismoViewSet
router = routers.DefaultRouter()

router.register(r'01.IndentificacaoDomicilio', IndentificacaoDeDomicilioViewSet)  
router.register(r'02.InformacoesMoradores', InformacoesMoradoresViewSet)
router.register(r'03.CaracteristicasDomicilio', CaracteristicasDomicilioViewSet)
router.register(r'04.RegistroCivil', RegistroCivilViewSet)
router.register(r'05.Nupcialidade', NupcialidadeViewSet)
router.register(r'06.TrabalhoErendimento', TrabalhoErendimentoViewSet)
router.register(r'07.TaxaMortalidade', Taxa_mortalidadeViewSet)
router.register(r'08.PessoaComDeficiencia', PessoaComDeficienciaViewSet)
router.register(r'09.Educacao', EducacaoViewSet)
router.register(r'10.DeslocamentoParaTrabalho', DeslocamentoParaTrabalhoViewSet)
router.register(r'11.ReligiaoCulto', religiaoCultoViewSet)
router.register(r'12.Autismo', AutismoViewSet) 


urlpatterns = router.urls