import streamlit as st
import pandas as pd
import json
from typing import Dict, List

def exibir_json_amigavel_regras(dados_json: Dict) -> None:
    """Exibe os dados JSON em um formato mais amigável."""
    try:
        st.subheader("Informações Gerais")
        col1, col2 = st.columns(2)
        col1.write(f"**Atributo ID:** {dados_json['atributo_id']}")
        col1.write(f"**Atributo Contrato:** {dados_json['atributo_contrato']}")
        col2.write(f"**Atributo Evento:** {dados_json['atributo_evento']}")
        col2.write(f"**Responsável Alteração:** {dados_json['racf']}")
        st.write(f"**Data Última Alteração:** {dados_json['data_hora_ultima_alteracao']}")

        st.subheader("Regras")
        for i, regra in enumerate(dados_json["regras"]):
            with st.expander(f"Regra: {regra['codigo_tt']}"):
                col1, col2 = st.columns(2)
                col1.write(f"**Código TT:** {regra['codigo_tt']}")
                col1.write(f"**Atributo Valor:** {regra['atributo_valor']}")
                col1.write(f"**Atributo Data Contábil:** {regra['atributo_data_contabil']}")
                col2.write(f"**Conta Débito:** {regra['contas']['debito']}")
                col2.write(f"**Conta Crédito:** {regra['contas']['credito']}")

                st.divider()

                st.markdown("Atributos e Condições:")
                atributos_df = pd.DataFrame(regra["atributos"])
                st.dataframe(atributos_df, hide_index=True)

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