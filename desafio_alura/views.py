from rest_framework import viewsets, filters
from desafio_alura.serializers import DespesasSerializer, ReceitaSerializer
from desafio_alura.models import Receitas
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


class ReceitasViewSet(viewsets.ModelViewSet):
    queryset = Receitas.objects.all()
    serializer_class = ReceitaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['nome']
    filterset_fields = ['descricao']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
      
   

class DespesasViewSet(viewsets.ModelViewSet):
    queryset = Receitas.objects.all()
    serializer_class = DespesasSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['nome']
    filterset_fields = ['descricao']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
