"""
Componentes de Gráficos para o Dashboard
"""

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from typing import Tuple

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


def create_daily_sales_chart(data: pd.DataFrame) -> go.Figure:
    """
    Cria gráfico de linha com vendas por dia
    
    Args:
        data: DataFrame com colunas 'data' e 'vendas'
    
    Returns:
        go.Figure: Gráfico Plotly
    """
    daily_sales = data.groupby('data')['vendas'].sum().reset_index()
    
    fig = px.line(
        daily_sales,
        x='data',
        y='vendas',
        title='📈 Vendas por Dia',
        labels={'data': 'Data', 'vendas': 'Vendas (R$)'},
        template='plotly_white'
    )
    
    fig.update_traces(
        line=dict(color=COLORS['primary'], width=3),
        hovertemplate='<b>%{x|%d/%m/%Y}</b><br>R$ %{y:,.2f}<extra></extra>'
    )
    
    fig.update_layout(
        hovermode='x unified',
        margin=dict(l=0, r=0, t=30, b=0),
        paper_bgcolor=COLORS['card_bg'],
        plot_bgcolor='rgba(0,0,0,0)'
    )
    
    return fig


def create_regional_sales_chart(data: pd.DataFrame) -> go.Figure:
    """
    Cria gráfico de barras horizontal com vendas por região
    
    Args:
        data: DataFrame com colunas 'regiao' e 'vendas'
    
    Returns:
        go.Figure: Gráfico Plotly
    """
    regional_sales = data.groupby('regiao')['vendas'].sum().sort_values(ascending=True)
    
    fig = px.barh(
        regional_sales,
        title='🗺️ Vendas por Região',
        labels={'value': 'Vendas (R$)', 'regiao': 'Região'},
        template='plotly_white'
    )
    
    fig.update_traces(
        marker=dict(color=COLORS['primary']),
        hovertemplate='<b>%{y}</b><br>R$ %{x:,.2f}<extra></extra>'
    )
    
    fig.update_layout(
        margin=dict(l=0, r=0, t=30, b=0),
        paper_bgcolor=COLORS['card_bg'],
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis_title='Vendas (R$)',
        yaxis_title=''
    )
    
    return fig


def create_category_sales_chart(data: pd.DataFrame) -> go.Figure:
    """
    Cria gráfico de barras com vendas por categoria
    
    Args:
        data: DataFrame com colunas 'categoria' e 'vendas'
    
    Returns:
        go.Figure: Gráfico Plotly
    """
    category_sales = data.groupby('categoria')['vendas'].sum().sort_values(ascending=False)
    
    fig = px.bar(
        category_sales,
        title='📦 Vendas por Categoria',
        labels={'value': 'Vendas (R$)', 'categoria': 'Categoria'},
        template='plotly_white'
    )
    
    fig.update_traces(
        marker=dict(color=COLORS['success']),
        hovertemplate='<b>%{x}</b><br>R$ %{y:,.2f}<extra></extra>'
    )
    
    fig.update_layout(
        margin=dict(l=0, r=0, t=30, b=0),
        paper_bgcolor=COLORS['card_bg'],
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis_title='',
        yaxis_title='Vendas (R$)',
        showlegend=False
    )
    
    return fig


def create_distribution_chart(data: pd.DataFrame) -> go.Figure:
    """
    Cria gráfico de pizza com distribuição de vendas por região
    
    Args:
        data: DataFrame com colunas 'regiao' e 'vendas'
    
    Returns:
        go.Figure: Gráfico Plotly
    """
    fig = px.pie(
        data,
        names='regiao',
        values='vendas',
        title='🎯 Distribuição de Vendas por Região',
        template='plotly_white',
        hole=0  # 0 para pie, 0.3+ para donut
    )
    
    fig.update_traces(
        hovertemplate='<b>%{label}</b><br>R$ %{value:,.2f}<br>%{percent}<extra></extra>',
        textposition='inside',
        textinfo='label+percent'
    )
    
    fig.update_layout(
        margin=dict(l=0, r=0, t=30, b=0),
        paper_bgcolor=COLORS['card_bg'],
    )
    
    return fig


def create_quantity_by_category_chart(data: pd.DataFrame) -> go.Figure:
    """
    Cria gráfico com quantidade de vendas por categoria
    
    Args:
        data: DataFrame com colunas 'categoria' e 'quantidade'
    
    Returns:
        go.Figure: Gráfico Plotly
    """
    qty_data = data.groupby('categoria')['quantidade'].sum().sort_values(ascending=False)
    
    fig = px.bar(
        qty_data,
        title='📊 Quantidade de Vendas por Categoria',
        labels={'value': 'Quantidade', 'categoria': 'Categoria'},
        template='plotly_white'
    )
    
    fig.update_traces(
        marker=dict(color=COLORS['warning']),
        hovertemplate='<b>%{x}</b><br>Quantidade: %{y}<extra></extra>'
    )
    
    fig.update_layout(
        margin=dict(l=0, r=0, t=30, b=0),
        paper_bgcolor=COLORS['card_bg'],
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis_title='',
        yaxis_title='Quantidade',
        showlegend=False
    )
    
    return fig


def create_trend_chart(data: pd.DataFrame) -> go.Figure:
    """
    Cria gráfico de tendência com área
    
    Args:
        data: DataFrame com colunas 'data' e 'vendas'
    
    Returns:
        go.Figure: Gráfico Plotly
    """
    daily_sales = data.groupby('data')['vendas'].sum().reset_index()
    daily_sales['media_movel'] = daily_sales['vendas'].rolling(window=7, min_periods=1).mean()
    
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=daily_sales['data'],
        y=daily_sales['vendas'],
        fill='tozeroy',
        name='Vendas',
        line=dict(color=COLORS['primary'], width=1),
        fillcolor='rgba(0, 102, 204, 0.1)',
        hovertemplate='<b>%{x|%d/%m/%Y}</b><br>R$ %{y:,.2f}<extra></extra>'
    ))
    
    fig.add_trace(go.Scatter(
        x=daily_sales['data'],
        y=daily_sales['media_movel'],
        name='Tendência (7 dias)',
        line=dict(color=COLORS['danger'], width=2, dash='dash'),
        hovertemplate='<b>%{x|%d/%m/%Y}</b><br>R$ %{y:,.2f}<extra></extra>'
    ))
    
    fig.update_layout(
        title='📉 Tendência de Vendas',
        template='plotly_white',
        margin=dict(l=0, r=0, t=30, b=0),
        paper_bgcolor=COLORS['card_bg'],
        plot_bgcolor='rgba(0,0,0,0)',
        hovermode='x unified',
        xaxis_title='Data',
        yaxis_title='Vendas (R$)'
    )
    
    return fig
