"""
Funções Utilitárias para o Dashboard
"""

import pandas as pd
from datetime import datetime, timedelta
import os


def load_data(file_path: str = None) -> pd.DataFrame:
    """
    Carrega dados de vendas do arquivo CSV
    
    Args:
        file_path: Caminho do arquivo CSV (opcional)
    
    Returns:
        pd.DataFrame: DataFrame com dados de vendas
    """
    if file_path is None:
        # Assumir que o arquivo está em data/vendas.csv
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, 'data', 'vendas.csv')
    
    try:
        df = pd.read_csv(file_path)
        df['data'] = pd.to_datetime(df['data'])
        df = df.sort_values('data').reset_index(drop=True)
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")
    except Exception as e:
        raise Exception(f"Erro ao carregar dados: {str(e)}")


def generate_sample_data(days: int = 90) -> pd.DataFrame:
    """
    Gera dados de exemplo para o dashboard
    
    Args:
        days: Número de dias de dados a gerar
    
    Returns:
        pd.DataFrame: DataFrame com dados de exemplo
    """
    import numpy as np
    
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
    return df


def format_currency(value: float) -> str:
    """
    Formata um valor numérico como moeda brasileira
    
    Args:
        value: Valor a formatar
    
    Returns:
        str: Valor formatado (ex: "R$ 1.234,56")
    """
    return f"R$ {value:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')


def format_number(value: float, decimals: int = 0) -> str:
    """
    Formata um número com separador de milhares
    
    Args:
        value: Valor a formatar
        decimals: Número de casas decimais
    
    Returns:
        str: Número formatado (ex: "1.234" ou "1.234,56")
    """
    if decimals == 0:
        return f"{value:,.0f}".replace(',', '.')
    else:
        return f"{value:,.{decimals}f}".replace(',', 'X').replace('.', ',').replace('X', '.')


def get_date_range_options() -> dict:
    """
    Retorna opções predefinidas de intervalo de datas
    
    Returns:
        dict: Dicionário com opções de data
    """
    today = datetime.now().date()
    
    return {
        'Hoje': {
            'start_date': today,
            'end_date': today
        },
        'Últimos 7 dias': {
            'start_date': today - timedelta(days=7),
            'end_date': today
        },
        'Últimos 30 dias': {
            'start_date': today - timedelta(days=30),
            'end_date': today
        },
        'Este mês': {
            'start_date': today.replace(day=1),
            'end_date': today
        },
        'Mês passado': {
            'start_date': (today.replace(day=1) - timedelta(days=1)).replace(day=1),
            'end_date': today.replace(day=1) - timedelta(days=1)
        },
        'Últimos 90 dias': {
            'start_date': today - timedelta(days=90),
            'end_date': today
        }
    }


def calculate_metrics(df: pd.DataFrame) -> dict:
    """
    Calcula métricas gerais do DataFrame
    
    Args:
        df: DataFrame com dados de vendas
    
    Returns:
        dict: Dicionário com métricas
    """
    return {
        'total_vendas': df['vendas'].sum(),
        'ticket_medio': df['vendas'].mean(),
        'quantidade_total': df['quantidade'].sum(),
        'numero_transacoes': len(df),
        'vendas_maxima': df['vendas'].max(),
        'vendas_minima': df['vendas'].min(),
        'desvio_padrao': df['vendas'].std(),
        'data_inicio': df['data'].min(),
        'data_fim': df['data'].max()
    }


def get_top_items(df: pd.DataFrame, column: str, n: int = 5) -> pd.Series:
    """
    Retorna os N itens com maior valor em uma coluna
    
    Args:
        df: DataFrame com dados
        column: Nome da coluna
        n: Número de itens a retornar
    
    Returns:
        pd.Series: Top N itens
    """
    return df.groupby(column)['vendas'].sum().nlargest(n)


def validate_date_range(start_date, end_date) -> bool:
    """
    Valida se o intervalo de datas é válido
    
    Args:
        start_date: Data inicial
        end_date: Data final
    
    Returns:
        bool: True se válido, False caso contrário
    """
    try:
        start = pd.to_datetime(start_date)
        end = pd.to_datetime(end_date)
        return start <= end
    except:
        return False
