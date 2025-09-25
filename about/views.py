from rest_framework.viewsets import ModelViewSet
from .models import About
from .serializers import AboutSerializer


class AboutViewSet(ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
