"""
Componentes reutilizáveis do Dashboard
"""

from .cards import create_kpi_card, create_kpi_row, create_stat_card, COLORS
from .charts import (
    create_daily_sales_chart,
    create_regional_sales_chart,
    create_category_sales_chart,
    create_distribution_chart,
    create_quantity_by_category_chart,
    create_trend_chart
)

__all__ = [
    'create_kpi_card',
    'create_kpi_row',
    'create_stat_card',
    'create_daily_sales_chart',
    'create_regional_sales_chart',
    'create_category_sales_chart',
    'create_distribution_chart',
    'create_quantity_by_category_chart',
    'create_trend_chart',
    'COLORS'
]
