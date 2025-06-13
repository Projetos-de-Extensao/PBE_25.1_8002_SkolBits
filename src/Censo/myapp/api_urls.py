from rest_framework import routers
from .api import DomicilioViewSet, MoradorViewSet

router = routers.DefaultRouter()
router.register(r'domicilios', DomicilioViewSet)
router.register(r'moradores', MoradorViewSet)

urlpatterns = router.urls