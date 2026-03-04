# 📖 Guia de Desenvolvimento - Dashboard Plotly Dash

Este documento serve como guia para desenvolvedores que desejam entender e estender o dashboard.

## 🏗️ Arquitetura

O projeto segue uma arquitetura modular e limpa:

```
├── app.py              (Entrada principal, layout)
├── config.py           (Configurações centralizadas)
├── utils.py            (Funções utilitárias)
├── callbacks/          (Lógica de interatividade)
├── components/         (Componentes reutilizáveis)
├── assets/             (Estilos CSS)
└── data/               (Dados)
```

## 🔄 Fluxo de Dados

```
user input (filtros)
        ↓
    callbacks.py (processa filtros)
        ↓
    utils.py (valida e formata dados)
        ↓
    components/ (renderiza componentes)
        ↓
    UI (atualiza dashboard)
```

## 📝 Adicionando uma Nova Funcionalidade

### 1. Novo Gráfico

**Arquivo**: `components/charts.py`

```python
def create_my_chart(data: pd.DataFrame) -> go.Figure:
    """
    Descrição do gráfico
    
    Args:
        data: DataFrame com os dados
    
    Returns:
        go.Figure: Gráfico Plotly
    """
    # Processar dados
    chart_data = data.groupby('coluna')['valor'].sum()
    
    # Criar figura
    fig = px.bar(chart_data, title='Meu Gráfico')
    
    # Customizar
    fig.update_layout(
        template='plotly_white',
        margin=dict(l=0, r=0, t=30, b=0),
        hovermode='x unified'
    )
    
    return fig
```

**Arquivo**: `callbacks/callbacks.py`

```python
# Adicione ao Output do callback
Output('my-chart', 'figure'),

# E à função
fig_my_chart = create_my_chart(filtered_df)

# Retorne
return (..., fig_my_chart)
```

**Arquivo**: `app.py`

```python
dcc.Graph(id='my-chart')
```

### 2. Novo KPI

**Arquivo**: `callbacks/callbacks.py`

```python
# No callback
valor_kpi = alguma_metrica(filtered_df)
kpi_novo = create_kpi_card(
    f"Valor: {valor_kpi}",
    "Label do KPI",
    COLORS['primary'],
    "🎯"
)

Output('kpi-novo', 'children')
```

**Arquivo**: `app.py`

```python
html.Div(id='kpi-novo', style={'flex': '1'})
```

### 3. Novo Filtro

**Arquivo**: `app.py`

```python
html.Div([
    html.Label("Meu Filtro:", style={'fontWeight': 'bold'}),
    dcc.Dropdown(
        id='my-filter',
        options=[
            {'label': 'Opção 1', 'value': 'op1'},
            {'label': 'Opção 2', 'value': 'op2'},
        ],
        value='op1',
    ),
], style={'flex': '1'})
```

**Arquivo**: `callbacks/callbacks.py`

```python
@app.callback(
    [...outputs...],
    [
        ...inputs...,
        Input('my-filter', 'value'),  # Adicione aqui
        ...
    ]
)
def update_dashboard(..., my_filter, ...):
    # Processar filtro
    if my_filter != 'all':
        filtered_df = filtered_df[filtered_df['coluna'] == my_filter]
```

## 🎨 Customizando Estilos

**Arquivo**: `assets/styles.css`

Adicione suas classes CSS. Elas serão aplicadas automaticamente:

```css
.minha-classe {
    background-color: #fff;
    border-radius: 8px;
    padding: 20px;
}
```

Ou inline nos componentes:

```python
html.Div(
    "Conteúdo",
    style={
        'backgroundColor': '#fff',
        'borderRadius': '8px',
        'padding': '20px'
    }
)
```

## 🧪 Testando Localmente

### 1. Modo Debug

```python
app.run_server(debug=True)  # Já configurado
```

Benefícios:
- Hot reload de código
- Error messages detalhadas
- Dash Dev Tools

### 2. Testar Filtros

```python
# Adicione print statements
def update_dashboard(...):
    print(f"Filtro de região: {region}")
    print(f"Dados filtrados: {len(filtered_df)} registros")
```

## 📊 Estrutura de Dados Esperada

O arquivo CSV deve conter:

```csv
data,regiao,categoria,vendas,quantidade
2024-12-05,Sudeste,Eletrônicos,487.23,3
2024-12-05,Nordeste,Roupas,345.67,7
```

Colunas obrigatórias:
- `data`: formato ISO (YYYY-MM-DD)
- `regiao`: string
- `categoria`: string
- `vendas`: float/int
- `quantidade`: int

## 🐛 Debug

### Ativar Logging

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Dash Dev Tools

Acesso automático em desenvolvimento. Abra o navegador e procure o menu de dev tools.

### Inspecionar Callbacks

```python
# Em callbacks.py
print(f"Filtered data shape: {filtered_df.shape}")
print(f"Columns: {filtered_df.columns.tolist()}")
```

## 📈 Performance

### Otimizações

1. **Memoization**:
```python
@functools.lru_cache(maxsize=32)
def expensive_function(param):
    return result
```

2. **Lazy Loading**:
```python
# Carregar dados sob demanda
if len(df) > 50000:
    df = df.sample(n=10000)
```

3. **Agrupar callbacks**:
```python
# Melhor: um callback com múltiplos outputs
@app.callback([Output(...), Output(...)])
def multi_update():
    return value1, value2
```

## 🔐 Segurança

### Validação de Entrada

```python
def validate_date_range(start, end):
    try:
        s = pd.to_datetime(start)
        e = pd.to_datetime(end)
        return s <= e
    except:
        return False
```

### Sanitizar Dados

```python
# Remover valores extremos
df = df[df['vendas'] > 0]
df = df[df['vendas'] < 1000000]
```

## 📚 Referências

- [Dash Documentation](https://dash.plotly.com/)
- [Plotly Express](https://plotly.com/python/plotly-express/)
- [Pandas Documentation](https://pandas.pydata.org/)
- [Python Best Practices](https://pep8.org/)

## 🚀 Deployment Checklist

- [ ] Remover `debug=True`
- [ ] Testar em produção localmente
- [ ] Validar todos os gráficos
- [ ] Verificar performance
- [ ] Configurar logging
- [ ] Backup de dados
- [ ] Documentar mudanças
- [ ] Atualizar README

## 💬 Convenções de Código

### Nomes

```python
# Funções
create_chart()
update_data()
format_value()

# Variáveis
filtered_df
total_sales
chart_data

# Constantes
MAX_RECORDS
DATE_FORMAT
DEFAULT_COLOR
```

### Docstrings

```python
def my_function(param1: str, param2: int) -> dict:
    """
    Breve descrição
    
    Args:
        param1: Descrição do parâmetro
        param2: Descrição do parâmetro
    
    Returns:
        dict: Descrição do retorno
    """
    pass
```

## 🎯 Próximos Passos

1. Explore o código base
2. Execute localmente (`python app.py`)
3. Modifique um componente
4. Commit com mensagem clara
5. Abra um Pull Request

---

**Dúvidas?** Abra uma issue no repositório!
