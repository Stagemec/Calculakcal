# 🥗 Calculakcal

**Calculakcal** é uma calculadora de calorias feita com Django que permite criar perfis de usuários para calcular suas necessidades calóricas diárias. A ferramenta considera dados como idade, peso, altura, sexo, nível de atividade física e objetivo de peso (emagrecimento, manutenção ou ganho de massa). Tudo é armazenado localmente em SQLite, sem necessidade de cadastro.

---

## ⚙️ Tecnologias Utilizadas

- **Python 3.8+**
- **Django** (framework web)
- **SQLite3** (banco de dados local)
- **HTML5 & CSS3**
- **Bootstrap** (interface responsiva)
- **JavaScript**

---

## 📋 Funcionalidades

- Criação de perfis de usuários com dados individuais.
- Cálculo da TMB (Taxa Metabólica Basal) com a equação de Harris-Benedict.
- Ajuste da TMB com base no nível de atividade física.
- Aplicação de metas (emagrecer, manter ou ganhar peso).
- Armazenamento local no dispositivo com SQLite.

---

## 🧰 Requisitos Mínimos

- Python 3.8 ou superior
- Pip (gerenciador de pacotes Python)
- Git (opcional)
- Navegador moderno (para uso da interface web)

---

## 🚀 Como Executar o Projeto

### 1. Clonar o repositório

  ```bash
  git clone https://github.com/Stagemec/Calculakcal.git
  cd Calculakca
  ```



### 2. Criar ambiente virtual (opcional, mas recomendado)
```bash
python -m venv venv
```

Ativar o ambiente virtual:

Windows:
```bash
venv\Scripts\activate
```
Linux/MacOS:
```bash
source venv/bin/activate
pip install -r requirements.txt
```
Ou, para instalação mínima:
```bash
pip install django
```
---
4. Aplicar migrações
python manage.py migrate

6. Acessar no navegador

Abra seu navegador e acesse:
```ip
http://127.0.0.1:8000/
```
---
📁 Estrutura do Projet:

```files
Calculakcal/
├── calculadora/           # Aplicação principal
│   ├── migrations/        # Migrações do banco
│   ├── models.py          # Modelos de dados
│   ├── views.py           # Regras de negócio
│   ├── urls.py            # Rotas da aplicação
│   └── templates/         # Páginas HTML (com Bootstrap)
├── db.sqlite3             # Banco de dados local
├── manage.py              # Gerenciador do Django
├── static/                # Arquivos estáticos (CSS, JS, imagens)
└── README.md              # Documentação do projeto
```
---
🌱 Melhorias Futuras

Cadastro de refeições com contagem de macronutrientes.

Dashboard com gráficos de progresso.

Histórico de metas e resultados por perfil.

Exportação de dados em PDF ou CSV.

Autenticação de usuários (login e senha).

Integração com APIs de alimentos.

---
📄 Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo LICENSE para mais detalhes.

---





