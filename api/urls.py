from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('courses', CourseViewSet)
router.register('teachers', TeacherViewSet)
router.register('portfolio', PortfolioViewSet)
router.register('info', InfoViewSet)
router.register('contact', ContactViewSet)
router.register('social-media', SocialMediaViewSet)
router.register('section-titles', SectionTitleViewSet, basename='section-title')
router.register('header-section', HeaderSectionViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
