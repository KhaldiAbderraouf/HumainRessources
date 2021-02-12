from rest_framework import routers

from .views import AbonnementViewSet

router = routers.DefaultRouter()
router.register('abonnement', AbonnementViewSet, 'abonnement')

urlpatterns = router.urls