from rest_framework.viewsets import ModelViewSet
from .models import Portfolio
from .serializers import PortfolioSerializer


class PortfolioViewSet(ModelViewSet):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
