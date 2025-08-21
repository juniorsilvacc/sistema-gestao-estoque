# 📦 Sistema de Gestão de Estoque

Um sistema completo para controle e gerenciamento de estoque, com funcionalidades de usuários, relatórios, comunicação em tempo real e integração com IA simulada.

---

## 🚀 Funcionalidades

### ✅ Gestão de Estoque
- Cadastro e edição de **produtos**, **categorias**, **marcas** e **fornecedores**.
- Registro de **entradas e saídas** com atualização automática do estoque.
- **Alertas de estoque crítico** (produtos abaixo do nível mínimo).
- Dashboard com **gráficos e métricas**:
  - Top produtos
  - Status do estoque
  - Movimentações recentes
- Exportação de relatórios em **CSV**.

### ✅ Gerenciamento de Usuários
- Cadastro de usuários com **papéis/cargos definidos** (Admin, Operador, etc).
- Controle de acesso por **setor**, exibindo apenas as áreas autorizadas.
- **Autenticação** com login/logout e controle de permissões.

### ✅ Comunicação em Tempo Real
- **API intermediadora de eventos** para capturar saídas de produtos.
- Sempre que há uma saída no sistema, é feito um **request para a API de eventos**, que processa e executa ações como:
  - Envio de SMS
  - Envio de WhatsApp
  - Envio de E-mail
- Arquitetura baseada em eventos, permitindo **escalabilidade** e **integração** com aplicações externas.

### ✅ Painel com IA (Simulada)
- Integração com modelo de **Inteligência Artificial (simulada)**.
- Geração de insights automáticos no dashboard:
  - Produtos com alta rotatividade
  - Previsões simples de reposição
  - Alertas preventivos baseados em comportamento dos dados

### ✅ Extras
- **Filtros e busca inteligentes**.
- Tratamento de erros personalizados (**páginas 404 e 500**).
- Estrutura modular com base em **boas práticas de desenvolvimento**.

## 📸 Screenshot
<img width="1528" height="1313" alt="Image" src="https://github.com/user-attachments/assets/94719d11-84a0-409f-bb6d-ab24ec6352d7" />
<img width="1543" height="1271" alt="Image" src="https://github.com/user-attachments/assets/322b0ac3-6e33-40c4-862b-12786e5c1133" />
<img width="1543" height="1271" alt="Image" src="https://github.com/user-attachments/assets/6138ae4a-d296-4fc4-bbe7-6db672d97f05" />
<img width="1543" height="1271" alt="Image" src="https://github.com/user-attachments/assets/0663ac50-b2f0-40c4-8e48-25c0b8a1f1ab" />
<img width="1543" height="1271" alt="Image" src="https://github.com/user-attachments/assets/4657f59b-36c9-4453-8428-8447b2331813" />
<img width="1543" height="1271" alt="Image" src="https://github.com/user-attachments/assets/1720dadd-7c11-47ab-a8d9-350d8effed60" />
<img width="1543" height="1271" alt="Image" src="https://github.com/user-attachments/assets/43721576-09e1-498b-8ef5-5656b24cc2c3" />
<img width="1543" height="1271" alt="Image" src="https://github.com/user-attachments/assets/e9c42783-96ba-4992-900d-0148739e461f" />
<img width="1543" height="1271" alt="Image" src="https://github.com/user-attachments/assets/f5c9c3ee-18df-4577-a32d-6f2535ea09c8" />
<img width="1543" height="1271" alt="Image" src="https://github.com/user-attachments/assets/52c16370-5140-4f66-b11a-52a3188206c1" />

## 🛠️ Tecnologias Utilizadas
- **Backend:** Django / Django REST Framework  
- **Banco de Dados:** PostgreSQL  
- **Frontend:** HTML5, CCS3, Boostrap, Javascrip, Ajax
- **Comunicação em Tempo Real:** API de eventos + integrações externas  
- **Integração com IA:** Simulação de modelo de Machine Learning
- **Infraestrutura**: Docker

## ▶️ Como Executar

### 1. Clone o repositório
```bash
git clone [https://github.com/seu-usuario/sistema-gestao-estoque.git](https://github.com/juniorsilvacc/sistema-gestao-estoque.git)
cd sistema-gestao-estoque
```

### 2. Crie o ambiente virtual e ative
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Instale as dependências
```bash
pip install -r requirements.txt
```

### 4. Configure o banco de dados
```bash
python manage.py migrate
```

### 4. Configure o banco de dados
```bash
python manage.py migrate
```

### 6. Inicie o servidor
```bash
python manage.py runserver
```

Acessar a aplicação http://localhost:8000
