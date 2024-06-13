## Projeto de Gerenciamento de Recursos - README

Este projeto implementa um sistema de gerenciamento de recursos utilizando Flask para o backend e React para o frontend. O sistema gerencia produtos, funcionários, empréstimos e certificados, permitindo operações básicas de CRUD (Create, Read, Update, Delete).

### Tecnologias Utilizadas

- **Backend**:
  - Flask: Framework web em Python para construção do servidor backend.
  - SQLAlchemy: Biblioteca ORM para interação com o banco de dados.
  - SQLite: Banco de dados relacional utilizado para armazenamento dos dados.


### Estrutura do Projeto

O projeto está estruturado da seguinte forma:

- **backend/**: Contém o código para o servidor Flask.
  - **app.py**: Arquivo principal que inicializa a aplicação Flask e configura as rotas.
  - **models.py**: Define os modelos de dados usando SQLAlchemy.
  - **routes/**: Contém os arquivos de rotas organizados por entidade (produtos, funcionários, empréstimos, certificados).
  - **templates/**: Poderia conter templates HTML (não necessário se estiver usando React).

- **frontend/**: Contém o código para o cliente React.
  - **public/**: Arquivos estáticos e index.html.
  - **src/**: Código JavaScript/JSX do React.
    - **components/**: Componentes reutilizáveis da interface.
    - **services/**: Funções para realizar requisições HTTP ao backend.

### Configuração e Instalação

Para rodar o projeto localmente, siga os passos abaixo:

1. **Clonar o repositório**:
   ```
   git clone <url_do_seu_repositorio>
   cd <nome_do_seu_projeto>
   ```

2. **Configurar o Backend**:
   - Navegue até o diretório `backend/`:
     ```
     cd backend
     ```
   - Instale as dependências do Python (é recomendável usar um ambiente virtual):
     ```
     pip install -r requirements.txt
     ```
   - Inicie o servidor Flask:
     ```
     flask run
     ```

3. **Configurar o Frontend**:
   - Abra um novo terminal na raiz do projeto (ou no diretório `frontend/`):
     ```
     cd frontend
     ```
   - Instale as dependências do Node.js:
     ```
     npm install
     ```
   - Inicie o servidor de desenvolvimento do React:
     ```
     npm start
     ```
egado e se comunicará com o backend Flask para todas as operações.

### Uso do Sistema

- **Funcionalidades**:
  - **Produtos**: CRUD completo para gerenciar produtos.
  - **Funcionários**: CRUD completo para gerenciar funcionários.
  - **Empréstimos**: CRUD completo para gerenciar empréstimos de recursos.
  - **Certificados**: CRUD completo para gerenciar certificados de funcionários.

- **API Endpoints**:
  - Todos os endpoints estão definidos em `backend/app.py` e organizados em rotas separadas para cada entidade (produtos, funcionários, empréstimos, certificados).

