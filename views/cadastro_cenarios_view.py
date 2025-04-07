import streamlit as st
import pandas as pd
from utils.excel_utils import ler_dados
from utils.json_generator import preencher_json_cenarios, gerar_arquivos_json

def exibir_cadastro_cenarios_view():
    """Exibe a view de cadastro de cenários."""
    st.header("Cadastro de Cenários")
    arquivo_excel = st.file_uploader("Selecione o arquivo Excel com cenários e parâmetros", type=["xlsx", "xls"])

    col1, col2 = st.columns(2)

    with open("arquivos/exemplos/Layout Cadastro Cenários.xlsx", "rb") as file:
        col2.download_button(
            label="Baixar Layout de Cadastro de Cenários",
            data=file,
            file_name="Layout Cadastro Cenários.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

    if arquivo_excel:
        try:
            sheets = ('Cenários', 'parametros_adicionais')
            cenarios_df, parametros_df = ler_dados(arquivo_excel, sheets)
            caminho = 'cenarios'
            if col1.button("Salvar Cenários", type="primary"):
                dados_json = preencher_json_cenarios(cenarios_df, parametros_df)
                gerar_arquivos_json(dados_json, parametros_df, caminho)
                st.toast("Arquivos JSON de cenários gerados com sucesso!")
        except Exception as e:
            st.error(f"Erro ao processar arquivo: {e}")