import streamlit as st
import json
from views.json_viewer import exibir_json_amigavel_regras, exibir_json_amigavel_cenarios
import os

'''def listar_arquivos_json_regras(diretorio: str = ".") -> list:
    """Lista os arquivos JSON disponíveis no diretório especificado."""
    arquivos_json = [arquivo for arquivo in os.listdir(f'{diretorio}/arquivos/regras') if arquivo.endswith(".json")]
    return arquivos_json'''

def exibir_visualizacao_view_regras():
    """Exibe a view de visualização de JSON."""
    diretorio = "arquivos/regras"
    st.header("Visualização de JSON")
    arquivos_json = listar_arquivos_json(diretorio)

    if arquivos_json:
        arquivo_selecionado = st.selectbox("Selecione um arquivo JSON para visualizar", arquivos_json)
        
        st.divider()
        
        if arquivo_selecionado:
            try:
                with open(f'arquivos/regras/{arquivo_selecionado}', "r") as arquivo:
                    dados_json = json.load(arquivo)
                    exibir_json_amigavel_regras(dados_json)
                    st.download_button(
                        label="Baixar JSON",
                        data=json.dumps(dados_json, indent=4),
                        file_name=arquivo_selecionado,
                        mime="application/json"
                    )
            except json.JSONDecodeError:
                st.error("Arquivo JSON inválido.")
            except FileNotFoundError:
                st.error("Arquivo JSON não encontrado.")
            except Exception as e:
                st.error(f"Erro ao visualizar arquivo JSON: {e}")
    else:
        st.info("Nenhum arquivo JSON encontrado no diretório atual.")


def exibir_visualizacao_cenarios_view():
    """Exibe a view de visualização de cenários."""
    diretorio = "arquivos/cenarios"
    st.header("Visualização de Cenários")
    arquivos_json = listar_arquivos_json(diretorio)

    if arquivos_json:
        arquivo_selecionado = st.selectbox("Selecione um arquivo JSON para visualizar", arquivos_json)
        if arquivo_selecionado:
            try:
                with open(os.path.join("arquivos/cenarios", arquivo_selecionado), "r") as arquivo:
                    dados_json = json.load(arquivo)
                    exibir_json_amigavel_cenarios(dados_json)
                    st.download_button(
                        label="Baixar JSON",
                        data=json.dumps(dados_json, indent=4),
                        file_name=arquivo_selecionado,
                        mime="application/json"
                    )
            except json.JSONDecodeError:
                st.error("Arquivo JSON inválido.")
            except FileNotFoundError:
                st.error("Arquivo JSON não encontrado.")
            except Exception as e:
                st.error(f"Erro ao visualizar arquivo JSON: {e}")
    else:
        st.info("Nenhum arquivo JSON encontrado no diretório atual.")
        

def listar_arquivos_json(diretorio: str) -> list:
    """Lista os arquivos JSON disponíveis no diretório especificado."""
    arquivos_json = [arquivo for arquivo in os.listdir(diretorio) if arquivo.endswith(".json")]
    return arquivos_json