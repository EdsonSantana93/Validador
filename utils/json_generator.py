import json
import pandas as pd
from typing import List, Dict
from datetime import datetime
from utils.regra_parser import processar_regra
import streamlit as st

def preencher_json_regras(regras_df: pd.DataFrame, parametros_df: pd.DataFrame) -> List[Dict]:
    """Preenche o JSON com os dados do DataFrame, incluindo racf e data_hora_ultima_alteracao."""
    dados_json = []
    data_hora_ultima_alteracao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for _, parametros_row in parametros_df.iterrows():
        racf = parametros_row["racf"] # Extrai o RACF da linha atual
        dados_regra = {
            "atributo_id": parametros_row["atributo_id"],
            "atributo_contrato": parametros_row["atributo_contrato"],
            "atributo_evento": parametros_row["atributo_evento"],
            "regras": [],
            "racf": racf,
            "data_hora_ultima_alteracao": data_hora_ultima_alteracao
        }

        for _, regra_row in regras_df.iterrows():
            regra = {
                "codigo_tt": regra_row["codigo_tt"],
                "atributos": processar_regra(regra_row["regra"]),
                "atributo_valor": regra_row["atributo_valor"],
                "atributo_data_contabil": regra_row["atributo_data_contabil"],
                "contas": {
                    "debito": regra_row["conta_debito"],
                    "credito": regra_row["conta_credito"]
                }
            }
            dados_regra["regras"].append(regra)
        dados_json.append(dados_regra)
    return dados_json

def gerar_arquivo_json_regras(dados_json: List[Dict], parametros_df: pd.DataFrame) -> None:
    """Gera arquivos JSON individuais para cada regra."""
    for i, dados_regra in enumerate(dados_json):
        nome_arquivo = f'arquivos/regras/{parametros_df["nome_arquivo"][i]}.json'
        try:
            with open(nome_arquivo, "w") as arquivo_json:
                json.dump(dados_regra, arquivo_json, indent=4)
        except Exception as e:
            st.error(f"Erro ao gerar arquivo JSON {nome_arquivo}: {e}") # Adiciona mensagem de erro
            

def preencher_json_cenarios(cenarios_df: pd.DataFrame, parametros_df: pd.DataFrame) -> Dict:
    """Preenche o JSON com os dados dos cenários."""
    try:
        dados_json = []
        cenarios = cenarios_df.groupby('cenario')['codigo_tt'].apply(list).reset_index().to_dict('records')
        for cenario in cenarios:
            dados_json.append({
                "cenario": cenario['cenario'],
                "tts": cenario['codigo_tt']
            })

        data_hora_ultima_atualizacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        return {
            "cenarios": dados_json,
            "racf": parametros_df["racf"][0],
            "data_hora_ultima_atualizacao": data_hora_ultima_atualizacao
        }
    except Exception as e:
        raise ValueError(f"Erro ao preencher JSON de cenários: {e}")

def gerar_arquivos_json_cenarios(dados_json: List[Dict], parametros_df: pd.DataFrame) -> None:
    """Gera um único arquivo JSON contendo um array de cenários."""
    nome_arquivo = f'arquivos/cenarios/{parametros_df["nome_arquivo"][0]}.json'
    try:
        with open(nome_arquivo, "w") as arquivo_json:
            json.dump(dados_json, arquivo_json, indent=4)
    except FileNotFoundError:
        st.error(f"Diretório 'arquivos/cenarios' não encontrado.")
        return
    except Exception as e:
        st.error(f"Erro ao gerar arquivo JSON {nome_arquivo}: {e}")