"""
Callbacks Interativos para o Dashboard
"""

from dash import Input, Output
from datetime import datetime
import pandas as pd
from components.cards import create_kpi_card, COLORS
from components.charts import (
    create_daily_sales_chart,
    create_regional_sales_chart,
    create_category_sales_chart,
    create_distribution_chart,
    create_quantity_by_category_chart,
    create_trend_chart
)


def register_callbacks(app, df: pd.DataFrame):
    """
    Registra todos os callbacks do dashboard
    
    Args:
        app: Aplicação Dash
        df: DataFrame com dados de vendas
    """
    
    @app.callback(
        [
            Output('kpi-total-vendas', 'children'),
            Output('kpi-ticket-medio', 'children'),
            Output('kpi-quantidade', 'children'),
            Output('kpi-variacao', 'children'),
            Output('datetime-display', 'children'),
            Output('vendas-por-dia', 'figure'),
            Output('vendas-por-regiao', 'figure'),
            Output('vendas-por-categoria', 'figure'),
            Output('distribuicao-vendas', 'figure'),
            Output('quantidade-por-categoria', 'figure'),
            Output('tendencia-vendas', 'figure'),
        ],
        [
            Input('date-picker', 'start_date'),
            Input('date-picker', 'end_date'),
            Input('region-dropdown', 'value'),
            Input('category-dropdown', 'value'),
            Input('interval-component', 'n_intervals')
        ]
    )
    def update_dashboard(start_date, end_date, region, category, n_intervals):
        """
        Atualiza todos os componentes do dashboard baseado nos filtros
        
        Args:
            start_date: Data inicial do filtro
            end_date: Data final do filtro
            region: Região selecionada
            category: Categoria selecionada
            n_intervals: Contador de intervalos (para atualização periódica)
        
        Returns:
            Tupla com atualizações para todos os outputs
        """
        
        # ========== FILTRAR DADOS ==========
        filtered_df = df[(df['data'] >= start_date) & (df['data'] <= end_date)].copy()
        
        if region != 'todas':
            filtered_df = filtered_df[filtered_df['regiao'] == region]
        
        if category != 'todas':
            filtered_df = filtered_df[filtered_df['categoria'] == category]
        
        # Garantir que temos dados
        if len(filtered_df) == 0:
            filtered_df = df[(df['data'] >= start_date) & (df['data'] <= end_date)].copy()
        
        # ========== CALCULAR KPIS ==========
        total_vendas = filtered_df['vendas'].sum()
        ticket_medio = filtered_df['vendas'].mean()
        quantidade = filtered_df['quantidade'].sum()
        
        # Calcular variação (comparar últimos 7 dias com 7 dias anteriores)
        sorted_df = filtered_df.sort_values('data')
        if len(sorted_df) > 14:
            recent_sales = sorted_df.iloc[-7:]['vendas'].sum()
            previous_sales = sorted_df.iloc[-14:-7]['vendas'].sum()
            variacao = ((recent_sales - previous_sales) / previous_sales * 100) if previous_sales > 0 else 0
        else:
            variacao = 0
        
        # ========== CRIAR KPI CARDS ==========
        kpi_total = create_kpi_card(
            f"R$ {total_vendas:,.2f}",
            "Total de Vendas",
            COLORS['primary'],
            "💰"
        )
        
        kpi_ticket = create_kpi_card(
            f"R$ {ticket_medio:,.2f}",
            "Ticket Médio",
            COLORS['success'],
            "🎯"
        )
        
        kpi_qtd = create_kpi_card(
            f"{quantidade:,.0f}",
            "Quantidade",
            COLORS['warning'],
            "📦"
        )
        
        color_variacao = COLORS['success'] if variacao >= 0 else COLORS['danger']
        kpi_var = create_kpi_card(
            f"{variacao:+.1f}%",
            "Variação",
            color_variacao,
            "📈" if variacao >= 0 else "📉"
        )
        
        # ========== DATETIME ==========
        datetime_str = datetime.now().strftime("%d/%m/%Y às %H:%M:%S")
        
        # ========== CRIAR GRÁFICOS ==========
        fig_daily = create_daily_sales_chart(filtered_df)
        fig_region = create_regional_sales_chart(filtered_df)
        fig_category = create_category_sales_chart(filtered_df)
        fig_dist = create_distribution_chart(filtered_df)
        fig_qty = create_quantity_by_category_chart(filtered_df)
        fig_trend = create_trend_chart(filtered_df)
        
        return (
            kpi_total,
            kpi_ticket,
            kpi_qtd,
            kpi_var,
            datetime_str,
            fig_daily,
            fig_region,
            fig_category,
            fig_dist,
            fig_qty,
            fig_trend
        )
