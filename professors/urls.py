from rest_framework.routers import DefaultRouter
from .views import ProfessorViewSet

router = DefaultRouter()
router.register(r'professors', ProfessorViewSet, basename='professors')

urlpatterns = router.urls
