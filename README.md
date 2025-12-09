📌 Autenticação + CRUD de Usuários (Flask + MySQL + Docker)

Este projeto é um CRUD completo de usuários com autenticação, desenvolvido em Python utilizando Flask, SQLAlchemy, Flask-Login e MySQL, com ambiente totalmente configurado via Docker Compose.

🚀 Tecnologias utilizadas

Flask

Flask-Login

Flask-SQLAlchemy

MySQL

Docker & Docker Compose

PyMySQL

🔐 Funcionalidades

✔ Cadastro de usuários
✔ Login e Logout
✔ Criptografia de senha
✔ Proteção de rotas
✔ Consulta de usuários
✔ Atualização e deleção
✔ Persistência de dados em container MySQL

🐳 Como rodar o projeto
1. Subir o banco de dados (Docker)
docker compose up -d

2. Instalar dependências
pip install -r requirements.txt

3. Rodar a aplicação
flask run

📁 Estrutura do projeto
/models
  user.py
/database
  __init__.py
app.py
docker-compose.yml
requirements.txt

📝 Endpoints

POST /login

GET /logout

POST /user

GET /user/<id>

PUT /user/<id>

DELETE /user/<id>

🎯 Objetivo do projeto

Praticar conceitos essenciais de backend:

CRUD real com banco SQL

Autenticação baseada em sessão

ORM com SQLAlchemy

Containers com Docker

Organização de API com Flask
