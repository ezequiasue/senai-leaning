task_manager/
│
├── task_manager/             # Diretório principal do projeto
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py           # Configurações principais
│   ├── urls.py               # URLs globais
│   └── wsgi.py
│
├── tasks/                    # App para gerenciar tarefas e recursos associados
│   ├── __init__.py
│   ├── admin.py              # Configurações do admin
│   ├── apps.py               # Configuração do app
│   ├── forms.py              # Formulários
│   ├── migrations/           # Migrações do banco de dados
│   ├── models.py             # Modelos do app
│   ├── tests.py              # Testes do app
│   ├── views.py              # Views do app
│   ├── urls.py               # Rotas específicas do app
│   └── templates/            # Templates HTML do app
│       ├── base.html
│       ├── task_list.html
│       ├── task_form.html
│       ├── task_confirm_delete.html
│       ├── project_list.html
│       └── category_list.html
│
├── static/                   # Arquivos estáticos (CSS, JS, imagens)
│   ├── css/
│   │   └── styles.css        # Estilos personalizados
│   ├── js/
│   │   └── script.js         # Scripts JS personalizados
│   └── img/                  # Imagens (se necessário)
│
├── media/                    # Arquivos de mídia (uploads)
│   └── attachments/          # Anexos de tarefas
│
├── db.sqlite3                # Banco de dados SQLite
│
└── manage.py                 # Script de gerenciamento do Django
