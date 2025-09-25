from rest_framework.routers import DefaultRouter
from .views import HeaderViewSet

router = DefaultRouter()
router.register("header", HeaderViewSet, basename="header")

urlpatterns = router.urls
