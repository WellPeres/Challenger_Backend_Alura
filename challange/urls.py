from atexit import register
from django.contrib import admin
from django.db import router
from django.urls import path, include
from rest_framework import routers
from desafio_alura.views import ReceitasViewSet, DespesasViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Challenge Alura Backend",
      default_version='v1',
      description="Api Construida para o Desafio alura de Backend Controle de Receitas/Despesas",
      terms_of_service="#",
      contact=openapi.Contact(email="email@ficticio.com.br"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)



router = routers.DefaultRouter()
router.register('receitas', ReceitasViewSet, basename='receitas')
router.register('despesas', DespesasViewSet, basename='despesas')

urlpatterns = [
    path('nao-tem-admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
