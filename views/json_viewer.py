import streamlit as st
import pandas as pd
import json
from typing import Dict, List

def exibir_json_amigavel_regras(dados_json: List[Dict]) -> None:
    """Exibe os dados JSON em um formato mais amigável."""
    try:
        if isinstance(dados_json, list) and len(dados_json) == 1: # Verifica se é um array de um objeto
            dados_json = dados_json[0] # Extrai o objeto do array
            col1, col2 = st.columns(2)
            col1.write(f"**Responsável Alteração:** {dados_json['racf']}")
            col2.write(f"**Data Última Alteração:** {dados_json['data_hora_ultima_alteracao']}")

            for regra in dados_json["regras"]:
                with st.expander(f"Regra: {regra['codigo_tt']}"):
                    st.write(f"**Atributos:**")
                    for atributo in regra["atributos"]:
                        st.write(f"  - {atributo['nome']}: {atributo['condicao']}")
                    st.write(f"**Atributo Valor:** {regra['atributo_valor']}")
                    st.write(f"**Atributo Data Contábil:** {regra['atributo_data_contabil']}")
                    st.write(f"**Contas:**")
                    st.write(f"  - Débito: {regra['contas']['debito']}")
                    st.write(f"  - Crédito: {regra['contas']['credito']}")
                    st.divider()

        elif isinstance(dados_json, list) and "cenarios" in dados_json[0]:  # Verifica se é um array de cenários
            for cenario in dados_json:
                with st.expander(f"Cenário: {cenario['cenario']}"):
                    st.write(f"**TTs:** {', '.join(cenario['tts'])}")
                    st.divider()

            col1, col2 = st.columns(2)
            col1.write(f"**Responsável Alteração:** {dados_json[0]['racf']}")
            col2.write(f"**Data Última Alteração:** {dados_json[0]['data_hora_ultima_atualizacao']}")
        else:
            st.write(json.dumps(dados_json, indent=4))
    except Exception as e:
        st.error(f"Erro ao exibir dados em formato amigável: {e}")
        st.write(json.dumps(dados_json, indent=4))
        
        
def exibir_json_amigavel_cenarios(dados_json: Dict) -> None:
    """Exibe os dados JSON em um formato mais amigável."""
    try:
        st.divider()
        st.subheader("Informações Gerais")
        col1, col2 = st.columns(2)
        col1.write(f"**Responsável Alteração:** {dados_json['racf']}")
        col2.write(f"**Data Última Alteração:** {dados_json['data_hora_ultima_atualizacao']}")

        for cenario in dados_json["cenarios"]:
            with st.expander(f"Cenário: {cenario['cenario']}"):
                st.write(f"**TTs:** {', '.join(cenario['tts'])}")
                st.divider()

    except Exception as e:
        st.error(f"Erro ao exibir dados em formato amigável: {e}")
        st.write(json.dumps(dados_json, indent=4))