from rest_framework import routers
from .api import ProjectViewSet

router = routers.DefaultRouter()

router.register('api/apiapp', ProjectViewSet, 'apiapp')

urlpatterns = router.urls