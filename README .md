# Projeto de API RESTful com Django Rest Framework

Este é um projeto criado para iniciantes que desejam desenvolver uma API RESTful usando Python e Django Rest Framework. Ele foi projetado para ensinar as principais operações CRUD (Create, Read, Update, Delete) e para demonstrar como criar e gerenciar uma API produtiva de forma prática e orientada a REST.

## 🎓 Sobre o Curso
Este projeto faz parte do curso [**Crie RESTful API com Django Rest Framework para Qualquer Um**](https://www.udemy.com/course/crie-restful-api-com-django-rest-framework-para-qualquer-um/learn/lecture/22902274#overview), que ensina como construir uma API do zero, abordando o ecossistema do Django e seus principais componentes.  

- **Instrutor**: Pedro Impulcetto, Software Engineer @ Nubank
- **Objetivo**: Criar uma API REST com endpoints para cadastro, consulta, edição e exclusão de informações, seguindo os padrões REST.
- **Nível**: Iniciante
- **Duração do Curso**: 30 minutos
- **Plataformas**: iOS, Android

## 🚀 Funcionalidades do Projeto
- **Modelagem de API**: Estruturação de uma API seguindo os conceitos de REST.
- **CRUD Completo**: Endpoints para criação, leitura, atualização e exclusão de registros.
- **Serialização**: Manipulação de dados de entrada e saída com serializers.
- **Upload de Imagens**: Suporte a upload de arquivos e imagens.
- **Pesquisa de Objetos**: Endpoint para busca e filtro de dados.

## 🛠 O que você aprenderá
- Uso do **Django Rest Framework** para criar e gerenciar APIs produtivas e escaláveis.
- Implementação de **viewsets** e **serializers** para manipulação de dados.
- Operações de **CRUD** com métodos HTTP e responses padronizadas.
- Configuração de endpoints e modelagem de dados.
- Práticas de desenvolvimento de APIs para negócios baseados em tecnologia.

## 📋 Pré-requisitos
Para melhor aproveitamento, é recomendado:
- **Conhecimento básico em Python**
- **Entendimento inicial do Django e do Django Rest Framework**

## 📂 Estrutura do Projeto
1. **Instalação**  
   - Clone este repositório
   - Crie um ambiente virtual e ative-o:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - Instale as dependências do projeto:
     ```bash
     pip install -r requirements.txt
     ```
   - Configure o banco de dados (SQLite ou PostgreSQL) e aplique as migrações:
     ```bash
     python manage.py migrate
     ```

2. **Executando o Servidor**
   ```bash
   python manage.py runserver
   ```

3. **Arquitetura do Projeto**
   - `my_project/` - Diretório do projeto Django contendo configurações e urls
   - `api/` - Aplicativo principal com os arquivos de views, serializers e models

## 📝 Exemplos de Uso
Um exemplo simples para criar um novo registro:

```python
import requests

url = "http://localhost:8000/api/itens/"
data = {
    "nome": "Item Exemplo",
    "descricao": "Descrição do item exemplo"
}
response = requests.post(url, json=data)
print(response.json())
```

## 🧑‍🏫 Sobre o Instrutor
**Pedro Impulcetto** trabalha como engenheiro de software no Nubank, com experiência em linguagens como Clojure, JavaScript, Go e Python. Ele possui amplo conhecimento em tecnologias de back-end e escalabilidade, além de vivência em projetos com empresas como Google e Banco do Brasil.

## 📜 Licença
Este projeto está sob a Licença MIT. Consulte o arquivo [LICENSE](LICENSE) para obter mais detalhes.