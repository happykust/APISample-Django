from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from drf_yasg.views import get_schema_view
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import permissions
from drf_yasg import openapi

# Set settings of API schema
SchemaView = get_schema_view(
    openapi.Info(
      title="APISample API",
      default_version='v1',
      description="Sample of CRUD API using User model",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

# Our API urls
urlpatterns = [
    path('users/', include('users.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('docs/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
    path('docs-schema/', SchemaView.as_view(), name='schema_url')
]