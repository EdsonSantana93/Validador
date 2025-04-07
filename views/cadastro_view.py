import streamlit as st
import pandas as pd
from utils.excel_utils import ler_dados
from utils.json_generator import  preencher_json_regras, gerar_arquivos_json

def exibir_cadastro_view_regras():
    """Exibe a view de cadastro de regras."""
    st.header("Cadastro de Regras")
    arquivo_excel = st.file_uploader("Selecione o arquivo Excel com regras e parâmetros", type=["xlsx", "xls"])

    col1, col2 = st.columns(2)

    with open("arquivos/exemplos/Layout Cadastro Regras.xlsx", "rb") as file:
        col2.download_button(
            label="Baixar Layout de Cadastro de Regras",
            data=file,
            file_name="Layout Cadastro Regras.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    if arquivo_excel:
        try:
            sheets = ('regras', 'parametros_adicionais')
            caminho = 'regras'
            regras_df, parametros_df = ler_dados(arquivo_excel, sheets)
            if col1.button("Salvar Regras", type="primary"):
                dados_json = preencher_json_regras(regras_df, parametros_df)
                gerar_arquivos_json(dados_json, parametros_df, caminho)
                st.toast("Arquivos JSON gerados com sucesso!")
        except Exception as e:
            st.error(f"Erro ao processar arquivo: {e}")