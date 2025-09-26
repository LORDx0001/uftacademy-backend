from rest_framework.routers import DefaultRouter
from .views import TitleViewSet

router = DefaultRouter()
router.register(r'titles', TitleViewSet, basename='titles')

urlpatterns = router.urls
