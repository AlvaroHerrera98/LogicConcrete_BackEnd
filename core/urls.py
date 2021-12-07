from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from logic_api import views
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
 
urlpatterns = [
   path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
   path('admin/', admin.site.urls),
   path('api/', include('logic_api.urls', namespace='logic_api')),
   path('api/user/', include('users.urls', namespace='users')),
   path('', TemplateView.as_view(template_name="logicconcrete/index.html")),
   path('docs/', include_docs_urls(title='LogicConcreteAPI')),
   path('schema', get_schema_view(
       title="Your Proeject",
       description="API for Logic Concrete",
       version="1.0.0",
        ), name="openapi-schema")
]

