import requests
from rest_framework import viewsets
from .models import Course, Teacher, PortfolioItem, InfoBlock, ContactMessage
from .serializers import *
from rest_framework.permissions import AllowAny

TELEGRAM_BOT_TOKEN = 'your_bot_token'
TELEGRAM_CHAT_ID = 'your_chat_id'

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = PortfolioItem.objects.all()
    serializer_class = PortfolioSerializer

class InfoViewSet(viewsets.ModelViewSet):
    queryset = InfoBlock.objects.all()
    serializer_class = InfoSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        instance = serializer.save()
        text = (
            f"📩 Новая заявка:\n"
            f"👤 {instance.first_name} {instance.last_name}\n"
            f"📞 Телефон: {instance.phone or '—'}\n"
            f"💬 Telegram: {instance.telegram or '—'}\n"
            f"📝 Сообщение: {instance.message or '—'}"
        )
        requests.post(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage", data={
            'chat_id': TELEGRAM_CHAT_ID,
            'text': text
        })

class SocialMediaViewSet(viewsets.ModelViewSet):
    queryset = SocialMedia.objects.filter(is_active=True)
    serializer_class = SocialMediaSerializer
    
class SectionTitleViewSet(viewsets.ModelViewSet):
    queryset = SectionTitle.objects.all()
    serializer_class = SectionTitleSerializer