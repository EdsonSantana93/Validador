import pandas as pd
from typing import Tuple

def ler_dados(arquivo_excel: str, sheet_names: Tuple[str, str]) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Lê os dados das abas especificadas do arquivo Excel."""
    try:
        df1 = pd.read_excel(arquivo_excel, sheet_name=sheet_names[0])
        df2 = pd.read_excel(arquivo_excel, sheet_name=sheet_names[1])
        df1 = df1.fillna("").astype(str)
        df2 = df2.fillna("").astype(str)
        return df1, df2
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo Excel não encontrado: {arquivo_excel}")
    except ValueError as ve:
        raise ValueError(f"Erro ao ler arquivo Excel (Valor inválido): {ve}")
    except KeyError as ke:
        raise KeyError(f"Erro ao ler arquivo Excel (Chave não encontrada): {ke}")
    except Exception as e:
        raise ValueError(f"Erro ao ler arquivo Excel (Erro desconhecido): {e}")