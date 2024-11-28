Validar Instalação
1.	Verificar a instalação do Python
2.	Instalar o Visual Studio Code (se ainda não estiver instalado)
3.	Criar uma pasta para o projeto
Ambiente Virtual e Dependências
1.	Criar um ambiente virtual (python -m venv venv)
2.	Ativar o ambiente virtual
3.	Atualizar pip (python -m pip install --upgrade pip)
4.	Instalar o Django (pip install django)
5.	Criar um arquivo requirements.txt (pip freeze > requirements.txt)
Criação do Projeto Django
1.	Executar django-admin startproject nome_do_projeto . para iniciar o projeto
2.	Executar python manage.py startapp nome_do_app para criar o aplicativo
Estrutura de Arquivos
1.	Criar pasta templates para os arquivos HTML
2.	Criar pasta static com subpastas:
•	css para estilos
•	img para imagens
•	js para scripts JavaScript
Configuração do Projeto
1.	Configurar settings.py:
•	Adicionar o nome do app em INSTALLED_APPS
•	Configurar STATIC_URL, STATIC_ROOT e STATICFILES_DIRS
•	Configurar TEMPLATES para incluir o diretório de templates
•	Configurar o banco de dados (SQLite, PostgreSQL ou MySQL)
•	Configurar TIME_ZONE e LANGUAGE_CODE
Configuração de URLs
1.	Configurar urls.py do projeto
2.	Criar e configurar urls.py do aplicativo
Modelos e Banco de Dados
1.	Definir modelos no arquivo models.py
2.	Executar python manage.py makemigrations
3.	Executar python manage.py migrate
Criação de Views e Templates
1.	Criar views no arquivo views.py
2.	Criar templates HTML correspondentes
Configuração do Admin
1.	Registrar modelos no arquivo admin.py
Testes
1.	Escrever testes básicos no arquivo tests.py
Execução do Servidor de Desenvolvimento
1.	Executar python manage.py runserver
Controle de Versão
1.	Inicializar repositório Git (git init)
2.	Criar arquivo .gitignore
3.	Fazer commit inicial
