import streamlit as st
import Controllers.ClienteController as ClienteController
import models.Cliente as cliente
import pandas as pd
import pages.Cliente.Create as PageCreateCliente


def List():
    paramId = st.experimental_get_query_params()
    if paramId == {}:
        st.experimental_set_query_params()
        colms = st.columns((1, 2, 1, 2, 1, 1))
        campos = ['Nº', 'Nome', 'Idade', 'Profissão', 'Excluir', 'Alterar']
        for col, campo_nome in zip(colms, campos):
            col.write(campo_nome)
        
        for item in ClienteController.selecionarTodos():
            col1, col2, col3, col4, col5, col6 = st.columns((1, 2, 1, 2, 1.3, 1))
            col1.write(item.id)
            col2.write(item.nome)
            col3.write(item.idade)
            col4.write(item.profissao)
            button_space_excluir = col5.empty()
            on_click_excluir = button_space_excluir.button('Exluir', 'btnExcluir' + str(item.id))
            button_space_alterar = col6.empty()
            on_click_alterar = button_space_alterar.button('Alterar', 'btnAlterar' + str(item.id))

            if on_click_excluir:
                ClienteController.Excluir(item.id)
                button_space_excluir.button('Excluido', 'btnExcluido' + str(item.id))

            if on_click_alterar:
                st.experimental_set_query_params(
                    id = [item.id]
                )
                st.experimental_rerun()
    else:
        on_click_voltar = st.button("Voltar")
        if on_click_voltar:
            st.experimental_set_query_params()
            st.experimental_rerun()
        PageCreateCliente.Create()






    # st.title("Consultar Cliente")
    # costumerList = []

    # for item in ClienteController.selecionarTodos():
    #     costumerList.append([item.nome, item.idade, item.profissao])

    # df = pd.DataFrame(
    #     costumerList,
    #     columns=["Nome", "Idade", "Profissão"]
    # )

    # st.table(df)