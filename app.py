"""
Dashboard Interativo com Plotly Dash
Aplicação de análise de vendas em tempo real com filtros dinâmicos
"""

from dash import Dash, dcc, html, Input, Output, State
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

# ==================== CONFIGURAÇÃO ====================

# Inicializar aplicação
app = Dash(__name__)
app.title = "Dashboard de Vendas"

# Cores do tema
COLORS = {
    'background': '#f8f9fa',
    'card_bg': '#ffffff',
    'primary': '#0066cc',
    'success': '#28a745',
    'danger': '#dc3545',
    'warning': '#ffc107',
    'text': '#333333'
}

# ==================== DADOS ====================

def generate_sample_data(days=90):
    """Gera dados de exemplo para o dashboard"""
    np.random.seed(42)
    
    dates = pd.date_range(end=datetime.now(), periods=days, freq='D')
    regions = ['Norte', 'Nordeste', 'Centro-Oeste', 'Sudeste', 'Sul']
    categories = ['Eletrônicos', 'Roupas', 'Alimentos', 'Livros', 'Esportes']
    
    data = {
        'data': np.repeat(dates, 20),
        'regiao': np.tile(np.random.choice(regions, 20), days),
        'categoria': np.tile(np.random.choice(categories, 20), days),
        'vendas': np.tile(np.random.uniform(100, 1000, 20), days),
        'quantidade': np.tile(np.random.randint(1, 10, 20), days),
    }
    
    df = pd.DataFrame(data)
    df['mes'] = df['data'].dt.to_period('M')
    return df

df = generate_sample_data()

# ==================== COMPONENTES ====================

def create_kpi_card(value, label, color, icon):
    """Cria um card KPI"""
    return dcc.Loading(
        id=f"loading-{label}",
        type="default",
        children=html.Div([
            html.Div([
                html.H6(label, style={'color': '#666', 'marginBottom': '10px'}),
                html.H3(value, style={'color': color, 'margin': '0'}),
            ], style={
                'backgroundColor': COLORS['card_bg'],
                'padding': '20px',
                'borderRadius': '8px',
                'boxShadow': '0 2px 4px rgba(0,0,0,0.1)',
                'borderLeft': f'4px solid {color}'
            })
        ])
    )

def create_layout():
    """Cria o layout principal do dashboard"""
    return html.Div(style={'backgroundColor': COLORS['background'], 'minHeight': '100vh'}, children=[
        
        # ========== HEADER ==========
        html.Div([
            html.Div([
                html.H1("📊 Dashboard de Vendas", style={'margin': '0'}),
                html.P("Análise de Vendas em Tempo Real", style={'color': '#666', 'margin': '5px 0 0 0'}),
            ], style={'flex': '1'}),
            html.Div(id='datetime-display', style={'textAlign': 'right', 'fontSize': '14px', 'color': '#666'})
        ], style={
            'backgroundColor': '#ffffff',
            'padding': '20px 30px',
            'boxShadow': '0 2px 8px rgba(0,0,0,0.1)',
            'marginBottom': '20px',
            'display': 'flex',
            'justifyContent': 'space-between',
            'alignItems': 'center'
        }),
        
        # ========== FILTROS ==========
        html.Div([
            html.Div([
                html.Label("Período:", style={'fontWeight': 'bold'}),
                dcc.DatePickerRange(
                    id='date-picker',
                    start_date=df['data'].min(),
                    end_date=df['data'].max(),
                    display_format='DD/MM/YYYY',
                    style={'width': '100%'}
                ),
            ], style={'flex': '1', 'marginRight': '20px'}),
            
            html.Div([
                html.Label("Região:", style={'fontWeight': 'bold'}),
                dcc.Dropdown(
                    id='region-dropdown',
                    options=[{'label': 'Todas', 'value': 'todas'}] + 
                            [{'label': r, 'value': r} for r in sorted(df['regiao'].unique())],
                    value='todas',
                    style={'width': '100%'}
                ),
            ], style={'flex': '1', 'marginRight': '20px'}),
            
            html.Div([
                html.Label("Categoria:", style={'fontWeight': 'bold'}),
                dcc.Dropdown(
                    id='category-dropdown',
                    options=[{'label': 'Todas', 'value': 'todas'}] + 
                            [{'label': c, 'value': c} for c in sorted(df['categoria'].unique())],
                    value='todas',
                    style={'width': '100%'}
                ),
            ], style={'flex': '1'}),
        ], style={
            'backgroundColor': COLORS['card_bg'],
            'padding': '20px 30px',
            'marginBottom': '20px',
            'borderRadius': '8px',
            'boxShadow': '0 2px 4px rgba(0,0,0,0.1)',
            'display': 'flex',
            'gap': '15px'
        }),
        
        # ========== KPI CARDS ==========
        html.Div([
            html.Div(id='kpi-total-vendas', style={'flex': '1', 'marginRight': '15px'}),
            html.Div(id='kpi-ticket-medio', style={'flex': '1', 'marginRight': '15px'}),
            html.Div(id='kpi-quantidade', style={'flex': '1', 'marginRight': '15px'}),
            html.Div(id='kpi-variacao', style={'flex': '1'}),
        ], style={
            'display': 'flex',
            'marginBottom': '20px',
            'gap': '10px',
            'padding': '0 30px'
        }),
        
        # ========== GRÁFICOS ==========
        html.Div([
            # Linha 1
            html.Div([
                html.Div([
                    dcc.Graph(id='vendas-por-dia'),
                ], style={'flex': '2', 'marginRight': '20px'}),
                
                html.Div([
                    dcc.Graph(id='vendas-por-regiao'),
                ], style={'flex': '1'}),
            ], style={'display': 'flex', 'marginBottom': '20px', 'gap': '10px'}),
            
            # Linha 2
            html.Div([
                html.Div([
                    dcc.Graph(id='vendas-por-categoria'),
                ], style={'flex': '1', 'marginRight': '20px'}),
                
                html.Div([
                    dcc.Graph(id='distribuicao-vendas'),
                ], style={'flex': '1'}),
            ], style={'display': 'flex', 'gap': '10px'}),
        ], style={'padding': '0 30px'}),
        
        dcc.Interval(id='interval-component', interval=5000),  # Atualiza a cada 5s
    ])

app.layout = create_layout()

# ==================== CALLBACKS ====================

@app.callback(
    [Output('kpi-total-vendas', 'children'),
     Output('kpi-ticket-medio', 'children'),
     Output('kpi-quantidade', 'children'),
     Output('kpi-variacao', 'children'),
     Output('datetime-display', 'children'),
     Output('vendas-por-dia', 'figure'),
     Output('vendas-por-regiao', 'figure'),
     Output('vendas-por-categoria', 'figure'),
     Output('distribuicao-vendas', 'figure')],
    [Input('date-picker', 'start_date'),
     Input('date-picker', 'end_date'),
     Input('region-dropdown', 'value'),
     Input('category-dropdown', 'value'),
     Input('interval-component', 'n_intervals')]
)
def update_dashboard(start_date, end_date, region, category, n_intervals):
    """Atualiza todos os componentes do dashboard"""
    
    # Filtrar dados
    filtered_df = df[(df['data'] >= start_date) & (df['data'] <= end_date)]
    
    if region != 'todas':
        filtered_df = filtered_df[filtered_df['regiao'] == region]
    
    if category != 'todas':
        filtered_df = filtered_df[filtered_df['categoria'] == category]
    
    # KPIs
    total_vendas = filtered_df['vendas'].sum()
    ticket_medio = filtered_df['vendas'].mean()
    quantidade = filtered_df['quantidade'].sum()
    variacao = ((filtered_df['vendas'].iloc[-7:].sum() - filtered_df['vendas'].iloc[-14:-7].sum()) / 
                filtered_df['vendas'].iloc[-14:-7].sum() * 100) if len(filtered_df) > 14 else 0
    
    kpi_total = create_kpi_card(f"R$ {total_vendas:,.2f}", "Total de Vendas", COLORS['primary'], "💰")
    kpi_ticket = create_kpi_card(f"R$ {ticket_medio:,.2f}", "Ticket Médio", COLORS['success'], "🎯")
    kpi_qtd = create_kpi_card(f"{quantidade:,.0f}", "Quantidade", COLORS['warning'], "📦")
    kpi_var = create_kpi_card(f"{variacao:+.1f}%", "Variação", COLORS['success'] if variacao >= 0 else COLORS['danger'], "📈")
    
    # Datetime
    datetime_str = datetime.now().strftime("%d/%m/%Y às %H:%M:%S")
    
    # Gráfico 1: Vendas por Dia
    daily_sales = filtered_df.groupby('data')['vendas'].sum().reset_index()
    fig_daily = px.line(daily_sales, x='data', y='vendas', 
                        title='Vendas por Dia',
                        labels={'data': 'Data', 'vendas': 'Vendas (R$)'},
                        template='plotly_white')
    fig_daily.update_traces(line=dict(color=COLORS['primary'], width=3))
    
    # Gráfico 2: Vendas por Região
    regional_sales = filtered_df.groupby('regiao')['vendas'].sum().sort_values(ascending=True)
    fig_region = px.barh(regional_sales, 
                         title='Vendas por Região',
                         labels={'value': 'Vendas (R$)', 'regiao': 'Região'},
                         template='plotly_white')
    fig_region.update_traces(marker=dict(color=COLORS['primary']))
    
    # Gráfico 3: Vendas por Categoria
    category_sales = filtered_df.groupby('categoria')['vendas'].sum().sort_values(ascending=False)
    fig_category = px.bar(category_sales,
                          title='Vendas por Categoria',
                          labels={'value': 'Vendas (R$)', 'categoria': 'Categoria'},
                          template='plotly_white')
    fig_category.update_traces(marker=dict(color=COLORS['success']))
    
    # Gráfico 4: Distribuição (Pie)
    fig_dist = px.pie(filtered_df, names='regiao', values='vendas',
                      title='Distribuição de Vendas por Região',
                      template='plotly_white')
    
    return kpi_total, kpi_ticket, kpi_qtd, kpi_var, datetime_str, fig_daily, fig_region, fig_category, fig_dist

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8050)
