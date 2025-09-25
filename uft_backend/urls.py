from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="TalipovPro API",
        default_version='v1',
        description="IT Akademiya Lending sayt API hujjati",
        contact=openapi.Contact(email="support@talipovpro.uz"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('about.urls')),
    path('api/', include('courses.urls')),
    path('api/', include('professors.urls')),
    path('api/', include('portfolio.urls')),
    path('api/', include('contact.urls')),
    path('api/', include('footer.urls')),  # ⬅️ Footer app
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
