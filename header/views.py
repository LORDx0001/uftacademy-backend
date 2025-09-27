from rest_framework.viewsets import ModelViewSet
from .models import Header
from .serializers import HeaderSerializer

class HeaderViewSet(ModelViewSet):
    queryset = Header.objects.all()
    serializer_class = HeaderSerializer

    http_method_names = ['get']
