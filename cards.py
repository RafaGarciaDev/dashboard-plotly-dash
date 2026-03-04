"""
Componentes KPI para o Dashboard
"""

from dash import dcc, html
from typing import Dict

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


def create_kpi_card(value: str, label: str, color: str, icon: str) -> html.Div:
    """
    Cria um card KPI estilizado
    
    Args:
        value: Valor a ser exibido (ex: "R$ 1.234,56")
        label: Rótulo do KPI (ex: "Total de Vendas")
        color: Cor do card (ex: "#0066cc")
        icon: Emoji ou ícone (ex: "💰")
    
    Returns:
        html.Div: Componente KPI card
    """
    return dcc.Loading(
        id=f"loading-{label}",
        type="default",
        children=html.Div([
            html.Div([
                html.Div([
                    html.Span(icon, style={
                        'fontSize': '28px',
                        'marginRight': '10px'
                    }),
                    html.H6(label, style={
                        'color': '#666',
                        'marginBottom': '10px',
                        'marginTop': '0',
                        'display': 'inline-block'
                    })
                ], style={'display': 'flex', 'alignItems': 'center'}),
                
                html.H3(value, style={
                    'color': color,
                    'margin': '15px 0 0 0',
                    'fontSize': '28px'
                }),
            ], style={
                'backgroundColor': COLORS['card_bg'],
                'padding': '20px',
                'borderRadius': '8px',
                'boxShadow': '0 2px 8px rgba(0,0,0,0.08)',
                'borderLeft': f'4px solid {color}',
                'transition': 'transform 0.2s, box-shadow 0.2s',
            })
        ]),
        style={
            'height': '100%'
        }
    )


def create_kpi_row(kpi_data: Dict) -> html.Div:
    """
    Cria uma linha com múltiplos KPI cards
    
    Args:
        kpi_data: Dicionário com dados dos KPIs
                  {'label': {'value': '...', 'color': '...', 'icon': '...'}}
    
    Returns:
        html.Div: Linha com cards KPI
    """
    cards = []
    num_cards = len(kpi_data)
    
    for idx, (key, data) in enumerate(kpi_data.items()):
        margin_right = '15px' if idx < num_cards - 1 else '0'
        
        cards.append(
            html.Div(
                create_kpi_card(
                    value=data['value'],
                    label=data['label'],
                    color=data['color'],
                    icon=data['icon']
                ),
                style={
                    'flex': '1',
                    'marginRight': margin_right,
                    'minWidth': '0'
                }
            )
        )
    
    return html.Div(
        cards,
        style={
            'display': 'flex',
            'gap': '10px',
            'marginBottom': '20px',
            'padding': '0 30px'
        }
    )


def create_stat_card(title: str, content: html.Div, color: str = None) -> html.Div:
    """
    Cria um card de estatística genérico
    
    Args:
        title: Título do card
        content: Conteúdo do card (pode ser html.Div, dcc.Graph, etc)
        color: Cor de destaque (opcional)
    
    Returns:
        html.Div: Card de estatística
    """
    border_color = color or COLORS['primary']
    
    return html.Div([
        html.H5(title, style={
            'marginTop': '0',
            'marginBottom': '15px',
            'color': COLORS['text'],
            'borderBottom': f'2px solid {border_color}',
            'paddingBottom': '10px'
        }),
        content
    ], style={
        'backgroundColor': COLORS['card_bg'],
        'padding': '20px',
        'borderRadius': '8px',
        'boxShadow': '0 2px 8px rgba(0,0,0,0.08)',
    })
