from rest_framework.viewsets import ModelViewSet
from .models import Footer
from .serializers import FooterSerializer


class FooterViewSet(ModelViewSet):
    queryset = Footer.objects.all()
    serializer_class = FooterSerializer
    
    http_method_names = ['get']
