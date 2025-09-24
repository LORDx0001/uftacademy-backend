from rest_framework import serializers
from .models import Course, Teacher, PortfolioItem, InfoBlock, ContactMessage, SectionTitle, SocialMedia

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioItem
        fields = '__all__'

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoBlock
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'

    def validate(self, data):
        if not data.get('phone') and not data.get('telegram'):
            raise serializers.ValidationError("Укажите хотя бы номер телефона или Telegram.")
        return data


class SectionTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionTitle
        fields = '__all__'

class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = '__all__'

