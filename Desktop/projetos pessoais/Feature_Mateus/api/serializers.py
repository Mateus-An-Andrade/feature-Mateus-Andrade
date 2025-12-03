from rest_framework import serializers
from .models import Categoria, Produto

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'



class ProdutoSerializer(serializers.ModelSerializer):
    categoria_nome = serializers.StringRelatedField(source='categoria', read_only=True)
    categoria = serializers.PrimaryKeyRelatedField(
        queryset=Categoria.objects.all()
    )

    class Meta:
        model = Produto
        fields = ['id', 'nome', 'descricao', 'preco', 'categoria', 'categoria_nome']