"""
Configurações do Dashboard
"""

import os
from datetime import datetime

# ==================== AMBIENTE ====================

DEBUG = True
ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')

# ==================== SERVIDOR ====================

HOST = '0.0.0.0'
PORT = 8050

# ==================== CORES ====================

COLORS = {
    'background': '#f8f9fa',
    'card_bg': '#ffffff',
    'primary': '#0066cc',
    'success': '#28a745',
    'danger': '#dc3545',
    'warning': '#ffc107',
    'text': '#333333',
    'gray': '#6c757d',
    'light': '#e9ecef',
    'dark': '#212529'
}

# ==================== DADOS ====================

DATA_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'data',
    'vendas.csv'
)

DEFAULT_DAYS = 90
SAMPLE_DATA_DAYS = 90

# ==================== GRÁFICOS ====================

CHART_TEMPLATE = 'plotly_white'
CHART_HEIGHT = 450

GRAPH_MARGIN = dict(l=0, r=0, t=30, b=0)

# ==================== ATUALIZAÇÃO ====================

INTERVAL_UPDATE = 5000  # em milissegundos

# ==================== FORMATAÇÃO ====================

DATE_FORMAT = '%d/%m/%Y'
DATETIME_FORMAT = '%d/%m/%Y às %H:%M:%S'
CURRENCY_SYMBOL = 'R$'

# ==================== DADOS PADRÃO ====================

DEFAULT_REGIONS = ['Norte', 'Nordeste', 'Centro-Oeste', 'Sudeste', 'Sul']
DEFAULT_CATEGORIES = ['Eletrônicos', 'Roupas', 'Alimentos', 'Livros', 'Esportes']

# ==================== KPI ====================

KPI_CONFIG = {
    'total_vendas': {
        'label': 'Total de Vendas',
        'icon': '💰',
        'color': COLORS['primary'],
        'format': 'currency'
    },
    'ticket_medio': {
        'label': 'Ticket Médio',
        'icon': '🎯',
        'color': COLORS['success'],
        'format': 'currency'
    },
    'quantidade': {
        'label': 'Quantidade',
        'icon': '📦',
        'color': COLORS['warning'],
        'format': 'number'
    },
    'variacao': {
        'label': 'Variação',
        'icon': '📈',
        'color': COLORS['success'],
        'format': 'percentage'
    }
}

# ==================== CACHE ====================

CACHE_TIMEOUT = 3600  # 1 hora em segundos

# ==================== LOGGING ====================

LOG_FORMAT = '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
LOG_LEVEL = 'INFO'

# ==================== LIMITES ====================

MAX_RECORDS = 100000
MIN_DATE_RANGE = 1  # dias
MAX_DATE_RANGE = 365  # dias

# ==================== MENSAGENS ====================

MESSAGES = {
    'data_loaded': '✅ Dados carregados com sucesso',
    'data_error': '❌ Erro ao carregar dados',
    'server_started': '🚀 Servidor iniciado',
    'no_data': 'Nenhum dado disponível para o período selecionado'
}
