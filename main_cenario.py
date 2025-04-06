import streamlit as st
from views.visualizacao_view import exibir_visualizacao_cenarios_view
from views.cadastro_cenarios_view import exibir_cadastro_cenarios_view

def main():
    """Função principal para a aplicação Streamlit."""
    st.title("Cadastro e Visualização")

    # Menu de seleção horizontal
    opcoes = ("Cenários", "Cadastar Cenários")
    menu = st.radio("Selecione o tipo de cadastro", opcoes, horizontal=True)

    if menu == "Cenários":
        exibir_visualizacao_cenarios_view()
    elif menu == "Cadastar Cenários":
        exibir_cadastro_cenarios_view()

if __name__ == "__main__":
    main()