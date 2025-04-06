import streamlit as st
from views.cadastro_view import exibir_cadastro_view_regras
from views.visualizacao_view import exibir_visualizacao_view_regras

def main():
    """Função principal para a aplicação Streamlit."""
    st.title("Cadastro e Visualização de Regras")

    # Menu de seleção horizontal
    opcoes = ("Visualização", "Cadastro")
    menu = st.radio("Selecione a funcionalidade", ("Visualização", "Cadastro"), horizontal=True)

    if menu == "Visualização":
        exibir_visualizacao_view_regras()
    elif menu == "Cadastro":
        exibir_cadastro_view_regras()

if __name__ == "__main__":
    main()