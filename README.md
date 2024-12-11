# Case Wise - API de Controle Financeiro

Bem-vindo ao repositório da API para o aplicativo de controle financeiro **Case Wise**! Este projeto visa fornecer uma API RESTful utilizando **Python**, o framework **Django**, e a biblioteca **Django REST Framework**.

Adotamos a arquitetura **Clean Architecture** e princípios de **Domain-Driven Design (DDD)** aprendidos durante um curso, tornando o desenvolvimento desta API uma experiência enriquecedora e desafiadora, especialmente por ser nossa primeira implementação após o estudo. Estamos confiantes de que você também encontrará valor ao explorá-la.

## Instalação

Para facilitar a configuração do projeto, recomendamos o uso do gerenciador de pacotes **UV**. Você pode seguir os passos abaixo para instalá-lo e iniciar o servidor da API:

### Passo 1: Instalar o UV
1. Abra o **PowerShell** no Windows.
2. Execute o seguinte comando para instalar o UV:

   ```powershell
   powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

### Passo 2: Iniciar a API
1. Navegue até a pasta do projeto no terminal:

   ```cmd
   cd infrastructure/api/
   ```

2. Inicie o servidor da API com o comando:

   ```cmd
   uv run manage.py runserver
   ```

Pronto! A sua API está funcionando e pronta para uso.

## Rotas Principais Para Primeira Navegação

### Criação de Usuário
- Endpoint: `users/create/`
- Descrição: Permite criar um novo usuário.

### Login
- Endpoint: `auth/login/`
- Descrição: Realiza o login do usuário, fornecendo acesso aos recursos da aplicação.

Com isso, você tem acesso completo ao poder da nossa aplicação web. 😊

