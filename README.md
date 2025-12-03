°README-CANDIDATO: Mateus Andrade

°Instruções para rodar
°Pré-requisitos

°Python 3.13.2

°Django 6.0

°Django REST Framework

°Variáveis de ambiente

°SECRET_KEY →'django-insecure-#aipb5=kqss)xy@(aan-%__%!wkbypikh7o#et5+&a=^wsq^=j';

°DEBUG → True;

°DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


=====================================================================================================================================================================================================================
Dificuldades encontradas:

==>Ajustar a exibição do nome da categoria no serializador de Produto usando StringRelatedField. 
==>Configurar testes unitários para criação e listagem de produtos com APITestCase do DRF.

=====================================================================================================================================================================================================================

O que não teve tempo de fazer:

==>Implementação deploy via Render.
==>Documentação Swagger/OpenAPI.
==>Testes mais completos para cobrir ou previnir duplicidade de produtos ou dados.

=====================================================================================================================================================================================================================

Seção final: Recomendações

==>Adicionar autenticação para a API (JWT/Token).
==>Configurar PostgreSQL para produção.
==>Melhorar validações nos serializadores e criar testes adicionais.
==>Implementar documentação Swagger/OpenAPI para os endpoints.
