from django.shortcuts import render
from rest_framework import viewsets
from .models import Categoria, Produto
from .serializers import CategoriaSerializer, ProdutoSerializer
# Create your views here.


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer