# ⚡ Quick Start - Dashboard Plotly Dash

## 🚀 Começar em 5 Minutos

### 1️⃣ Preparar Ambiente

```bash
# Entrar na pasta
cd dashboard-plotly-dash

# Criar ambiente virtual
python -m venv venv

# Ativar ambiente
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 2️⃣ Instalar Dependências

```bash
pip install -r requirements.txt
```

### 3️⃣ Executar

```bash
python app.py
```

### 4️⃣ Acessar

Abra no navegador:
```
http://localhost:8050
```

---

## 📊 O Que Você Vê

```
┌─────────────────────────────────────────┐
│  📊 Dashboard de Vendas                 │
│  Análise de Vendas em Tempo Real   14:30│
├─────────────────────────────────────────┤
│ 📅 Período | 🗺️ Região | 📦 Categoria  │
├─────────────────────────────────────────┤
│  💰 Total    🎯 Ticket   📦 Qtd  📈 Var │
│  R$ 50.5K    R$ 234     1.8K    +12.5%  │
├─────────────────────────────────────────┤
│  Vendas/Dia       Vendas/Região        │
│  [Gráfico Linha] [Gráfico Barras H]   │
├─────────────────────────────────────────┤
│  Vendas/Categ    Distribuição/Região  │
│  [Gráfico Bar]   [Gráfico Pizza]      │
├─────────────────────────────────────────┤
│  Quantidade      Tendência             │
│  [Gráfico Bar]   [Gráfico Área]       │
└─────────────────────────────────────────┘
```

---

## 🎮 Como Usar

### Filtrar Dados

1. **Por Data**: Use o calendário para selecionar período
2. **Por Região**: Escolha no dropdown (ou "Todas")
3. **Por Categoria**: Escolha no dropdown (ou "Todas")

Os gráficos **atualizam automaticamente** quando você muda os filtros.

### Interagir com Gráficos

- **Hover**: Passe o mouse para ver valores
- **Click**: Clique na legenda para mostrar/ocultar séries
- **Zoom**: Use o zoom box (icon no canto superior)
- **Reset**: Use o reset zoom (icon no canto superior)
- **Download**: Download como PNG (icon no canto superior)

---

## 📁 Estrutura Rápida

```
dashboard-plotly-dash/
├── app.py              ← Comece por aqui
├── data/vendas.csv     ← Seus dados
├── components/         ← Gráficos e Cards
├── callbacks/          ← Lógica interativa
├── assets/styles.css   ← Estilos
└── README.md           ← Documentação completa
```

---

## 🔧 Customizações Rápidas

### Mudar Cores

Edite em `config.py`:

```python
COLORS = {
    'primary': '#0066cc',   # ← Azul principal
    'success': '#28a745',   # ← Verde
    'danger': '#dc3545',    # ← Vermelho
}
```

### Adicionar Seus Dados

Substitua `data/vendas.csv` mantendo as colunas:
- data (YYYY-MM-DD)
- regiao
- categoria
- vendas
- quantidade

### Mudar Intervalo de Atualização

Em `app.py`, procure:
```python
dcc.Interval(id='interval-component', interval=5000)
```

Mude `5000` para o valor em **milissegundos**:
- 1000 = 1 segundo
- 5000 = 5 segundos (padrão)
- 10000 = 10 segundos

---

## 🆘 Problemas Comuns

### ❌ "ModuleNotFoundError: No module named 'dash'"

```bash
pip install -r requirements.txt
```

### ❌ "Address already in use"

Mude a porta em `config.py`:
```python
PORT = 8051  # ou outro número
```

### ❌ Gráficos não aparecem

1. Verifique se o arquivo `data/vendas.csv` existe
2. Confirme as colunas do CSV
3. Atualize a página (F5)

### ❌ Filtros não funcionam

Verifique o console do navegador (F12) para erros

---

## 📊 Dados de Exemplo

O arquivo `data/vendas.csv` contém:

- **90 dias** de dados históricos
- **5 regiões**: Norte, Nordeste, Centro-Oeste, Sudeste, Sul
- **5 categorias**: Eletrônicos, Roupas, Alimentos, Livros, Esportes
- **1.800 registros** totais

---

## 🚢 Deploy Rápido

### Heroku (Grátis)

```bash
# 1. Instale Heroku CLI
# 2. Login
heroku login

# 3. Crie app
heroku create seu-app-name

# 4. Deploy
git push heroku main
```

### Docker

```bash
docker build -t dashboard .
docker run -p 8050:8050 dashboard
```

---

## 📚 Próximos Passos

1. **Ler** `README.md` para documentação completa
2. **Explorar** `DEVELOPMENT.md` para arquitetura
3. **Customizar** com seus dados e cores
4. **Deploy** em produção

---

## 💬 Dúvidas?

- Verifique `README.md` → Seção FAQ
- Leia `DEVELOPMENT.md` para detalhes técnicos
- Abra uma issue no repositório

---

## ✅ Checklist de Início

- [ ] Clonar/extrair o projeto
- [ ] Criar virtual env
- [ ] Instalar dependências
- [ ] Executar `python app.py`
- [ ] Acessar `http://localhost:8050`
- [ ] Testar filtros
- [ ] Testar interação com gráficos
- [ ] Celebrar! 🎉

---

**Bom desenvolvimento!** 🚀

Última atualização: Dezembro 2024
