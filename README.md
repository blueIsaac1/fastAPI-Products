# Projeto de Gerenciamento de Produtos com FastAPI

Este projeto é uma API simples para gerenciar produtos utilizando FastAPI e Pydantic. Os dados dos produtos são armazenados em um arquivo JSON.

## Estrutura do Projeto

- `json_indb.py`: Contém a classe `JsonDB` que gerencia a leitura e escrita de dados em um arquivo JSON.
- `main.py`: O ponto de entrada da aplicação FastAPI, que define as rotas para obter e criar produtos.
- `product.py`: Define o modelo de dados `Product` utilizando Pydantic.
- `indb.py`: Contém uma função (comentada) para gerar produtos de exemplo.

## Dependências

Certifique-se de ter as seguintes dependências instaladas:

- FastAPI
- Pydantic

Você pode instalar as dependências necessárias usando o seguinte comando:

```bash
pip install fastapi pydantic
```

## Como Usar

1. **Inicie o Servidor**: Execute o arquivo `main.py` para iniciar o servidor FastAPI.

   ```bash
   uvicorn main:app --reload
   ```

2. **Endpoints**:
   - **GET /products**: Retorna a lista de produtos armazenados no arquivo JSON.
   - **POST /products**: Adiciona um novo produto ao arquivo JSON. O corpo da requisição deve ser um JSON com os campos `name` e `price`.

   Exemplo de requisição para criar um produto:

   ```json
   {
       "name": "Produto Exemplo",
       "price": 10.0
   }
   ```

## Estrutura do Arquivo JSON

O arquivo JSON deve ter a seguinte estrutura:

```json
{
    "products": []
}
```

## Contribuições

Sinta-se à vontade para contribuir com melhorias ou correções. Para isso, faça um fork do repositório e envie um pull request.

## Licença

Este projeto está licenciado sob a MIT License.
