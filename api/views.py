import requests
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Course, Teacher, PortfolioItem, InfoBlock, ContactMessage, SocialMedia, SectionTitle
from .serializers import CourseSerializer, TeacherSerializer, PortfolioSerializer, InfoSerializer, ContactSerializer, SocialMediaSerializer, SectionTitleSerializer
from .permissions import IsSuperAdminOrReadOnly
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.decorators import action

TELEGRAM_BOT_TOKEN = 'your_bot_token'
TELEGRAM_CHAT_ID = 'your_chat_id'

# CourseViewSet
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsSuperAdminOrReadOnly]
    http_method_names = ['get']
    

# TeacherViewSet
class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsSuperAdminOrReadOnly]
    http_method_names = ['get']
    

# PortfolioViewSet
class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = PortfolioItem.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = [IsSuperAdminOrReadOnly]
    http_method_names = ['get']
    

# InfoViewSet
class InfoViewSet(viewsets.ModelViewSet):
    queryset = InfoBlock.objects.all()
    serializer_class = InfoSerializer
    permission_classes = [IsSuperAdminOrReadOnly]
    http_method_names = ['get']
    

# ContactViewSet
class ContactViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [IsSuperAdminOrReadOnly]

    # Faonly GET va POST metodlariga ruxsat berish
    http_method_names = ['get', 'post']

    @swagger_auto_schema(operation_description="Retrieve all contact messages.")
    def list(self, request, *args, **kwargs):
        """
        Faqat GET metodini faqat ruxsat berish.
        """
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(operation_description="Create a new contact message.")
    def create(self, request, *args, **kwargs):
        """
        Faqat POST metodini ruxsat etish.
        """
        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        instance = serializer.save()
        text = (
            f"📩 Yangi ariza:\n"
            f"👤 {instance.first_name} {instance.last_name}\n"
            f"📞 Telefon: {instance.phone or '—'}\n"
            f"💬 Telegram: {instance.telegram or '—'}\n"
            f"📝 Xabar: {instance.message or '—'}"
        )
        # Telegramga yuborish
        requests.post(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage", data={
            'chat_id': TELEGRAM_CHAT_ID,
            'text': text
        })

# SocialMediaViewSet
class SocialMediaViewSet(viewsets.ModelViewSet):
    queryset = SocialMedia.objects.filter(is_active=True)
    serializer_class = SocialMediaSerializer
    permission_classes = [IsSuperAdminOrReadOnly]
    http_method_names = ['get']
    

# SectionTitleViewSet
class SectionTitleViewSet(viewsets.ModelViewSet):
    queryset = SectionTitle.objects.all()
    serializer_class = SectionTitleSerializer
    permission_classes = [IsSuperAdminOrReadOnly]
    http_method_names = ['get']
    
    @action(detail=False, url_path='by-key/(?P<key>[^/.]+)', methods=['get'])
    def retrieve_by_key(self, request, key=None):
        try:
            section = SectionTitle.objects.get(key=key)
            serializer = self.get_serializer(section)
            return Response(serializer.data)
        except SectionTitle.DoesNotExist:
            return Response({'error': 'Not found'}, status=404)