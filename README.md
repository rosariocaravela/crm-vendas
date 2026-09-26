# ⚡ CRM Vendas

Um CRM profissional para gestão de vendas construído com **Python/Django**.

![Python](https://img.shields.io/badge/Python-3.12+-blue?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.0-green?logo=django&logoColor=white)
![TailwindCSS](https://img.shields.io/badge/TailwindCSS-3.0-blue?logo=tailwindcss&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🚀 Funcionalidades

- 🔐 **Autenticação** — Login, registro e perfil de utilizador
- 👥 **Gestão de Clientes** — CRUD completo com busca, filtros e histórico de interações
- 🔄 **Pipeline de Vendas** — Board Kanban com drag & drop (Prospecto → Fechado)
- 📊 **Dashboard** — Métricas em tempo real com gráficos interativos (Chart.js)
- 📄 **Relatórios** — Exportação para PDF e Excel

## 🛠 Stack Tecnológica

| Componente | Tecnologia |
|---|---|
| Backend | Python 3.12+ / Django 5 |
| Frontend | TailwindCSS + Chart.js + SortableJS |
| Banco de Dados | SQLite (dev) / PostgreSQL (prod) |
| Relatórios | ReportLab (PDF) + openpyxl (Excel) |

## 📦 Instalação

```bash
# Clonar o repositório
git clone https://github.com/SEU_USUARIO/crm-vendas.git
cd crm-vendas

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instalar dependências
pip install -r requirements.txt

# Aplicar migrações
python manage.py migrate

# Criar etapas do pipeline
python manage.py create_default_stages

# Criar superusuário
python manage.py createsuperuser

# Iniciar o servidor
python manage.py runserver
```

## 📸 Screenshots

### Dashboard
> Painel com métricas de vendas, gráficos e atividades recentes

### Pipeline Kanban
> Board interativo com drag & drop para gerir oportunidades

### Gestão de Clientes
> Lista de clientes com busca, filtros e histórico de interações

## 📁 Estrutura do Projeto

```
crm_vendas/
├── accounts/          # Autenticação e perfil
├── clients/           # Gestão de clientes
├── pipeline/          # Pipeline de vendas (Kanban)
├── dashboard/         # Dashboard com métricas
├── reports/           # Relatórios e exportação
├── templates/         # Templates base
├── static/            # CSS, JS, imagens
└── crm_vendas/        # Configurações Django
```

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## 📝 Licença

Este projeto está sob a licença MIT.
