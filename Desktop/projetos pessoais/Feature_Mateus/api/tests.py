from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Categoria, Produto

# Create your tests here.
class ProdutoAPITests(APITestCase):

    def setUp(self):
        # Criar uma categoria para usar nos produtos
        self.categoria = Categoria.objects.create(nome="games")
        self.produto_url = reverse('produto-list')  
                                                                    # gerar a URL do endpoint de listagem/criação de produtos automaticamente usando o nome do ViewSet, sem precisar digitar a URL manualmente.

    def test_criar_produto(self):
        data = {
            "nome": "GTA VI",
            "descricao": "GAME de lançamento 2026",
            "preco": "1000.89",
            "categoria": self.categoria.id
        }
        response = self.client.post(self.produto_url, data, format='json')
        
        self.assertEqual(response.data['categoria'], self.categoria.id)       # ID usado no POST
        self.assertEqual(response.data['categoria_nome'], "games")      # StringRelatedField


                                                   # O bloco de teste acima verifica se a API de produtos funciona corretamente.

    def test_listar_produtos(self):
        Produto.objects.create(
            nome="Notebook",
            descricao="i7 16GB",
            preco=3999.99,
            categoria=self.categoria
        )
        response = self.client.get(self.produto_url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['nome'], "Notebook")


                                                                                #Esse teste garante que a API consegue listar produtos corretamente e que os dados retornados estão corretos.