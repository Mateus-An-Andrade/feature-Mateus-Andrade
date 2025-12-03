from rest_framework import serializers
from .models import Categoria, Produto

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'



class ProdutoSerializer(serializers.ModelSerializer):
# objetivo: o nome da categoria, não só o ID
    categoria = serializers.StringRelatedField()


    class Meta:
        model = Produto
        fields = '__all__'