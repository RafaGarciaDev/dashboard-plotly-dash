# 📊 Dashboard Interativo com Plotly Dash

Um dashboard interativo e responsivo construído com Plotly Dash, apresentando análise de vendas em tempo real com múltiplos gráficos, filtros dinâmicos e indicadores KPI.

## ✨ Funcionalidades

- **Dashboard em Tempo Real**: Atualização automática de dados
- **Filtros Dinâmicos**: Filtre por período, região e categoria
- **KPI Indicators**: Indicadores principais de desempenho
- **Gráficos Interativos**: Pie charts, bar charts, line charts com Plotly
- **Design Responsivo**: Layout adaptável para dispositivos móveis
- **Callbacks Interativos**: Sincronização de componentes em tempo real

## 🛠️ Tecnologias Utilizadas

- **Dash**: Framework web para dashboards Python
- **Plotly**: Visualização de dados interativa
- **Pandas**: Manipulação de dados
- **Python 3.8+**

## 📋 Requisitos

```bash
pip install dash plotly pandas numpy
```

## 🚀 Como Executar

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/dashboard-plotly-dash.git
cd dashboard-plotly-dash

# 2. Instale as dependências
pip install -r requirements.txt

# 3. Execute a aplicação
python app.py

# 4. Acesse no navegador
# http://localhost:8050
```

## 📁 Estrutura do Projeto

```
dashboard-plotly-dash/
├── app.py                 # Arquivo principal da aplicação
├── data/
│   └── vendas.csv        # Dados de exemplo
├── callbacks/
│   └── callbacks.py      # Callbacks interativos
├── components/
│   ├── cards.py          # Componentes KPI
│   └── charts.py         # Componentes de gráficos
├── assets/
│   └── styles.css        # Estilos CSS personalizados
├── requirements.txt      # Dependências do projeto
├── .gitignore           # Arquivos a ignorar
└── README.md            # Documentação
```

## 💡 Exemplos de Uso

### Visualizar Dashboard
```python
from dash import Dash, dcc, html, Input, Output
import plotly.express as px

app = Dash(__name__)
# Dashboard com múltiplos gráficos e filtros
```

### Filtros Dinâmicos
Utilize o dropdown para filtrar dados por período, região ou categoria. Os gráficos se atualizam automaticamente.

### KPI Cards
Acompanhe em tempo real:
- Total de Vendas
- Ticket Médio
- Taxa de Crescimento
- Número de Transações

## 🔗 Dependências Principais

| Pacote | Versão | Propósito |
|--------|--------|----------|
| dash | 2.14+ | Framework do dashboard |
| plotly | 5.18+ | Visualizações interativas |
| pandas | 2.0+ | Manipulação de dados |
| numpy | 1.24+ | Computação numérica |

## 📈 Performance

- **Tempo de Carregamento**: < 2 segundos
- **Renderização**: GPU acelerada com Plotly WebGL
- **Escalabilidade**: Otimizado para até 100k registros

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor:

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 👤 Autor

Seu Nome
- GitHub: [@seu-usuario](https://github.com/seu-usuario)
- LinkedIn: [Seu Perfil](https://linkedin.com/in/seu-perfil)

## 📞 Suporte

Para dúvidas ou sugestões, abra uma issue no repositório.

---

⭐ Se este projeto foi útil, deixe uma star!
