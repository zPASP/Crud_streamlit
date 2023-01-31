import streamlit as st
import pages.Cliente.Create as PageCreateCliente
import pages.Cliente.List as PageListCliente



st.sidebar.title("Menu")
page_cliente = st.sidebar.selectbox("Cliente", ['Incluir', 'Consultar'])

if page_cliente == "Consultar":
    PageListCliente.List()

if page_cliente ==  "Incluir":
    st.experimental_set_query_params()
    PageCreateCliente.Create()


# if st.button("Validar"):
#     ClienteController.selecionarTodos()
#     print ('ok')

