import streamlit as st
import Controllers.ClienteController as ClienteController
import models.Cliente as cliente
import pandas as pd
import pages.Cliente.Create as PageCreateCliente
import pages.Cliente.List as PageListCliente



st.sidebar.title("Menu")
page_cliente = st.sidebar.selectbox("Cliente", ['Incluir', 'Alterar', 'Excluir', 'Consultar'])

if page_cliente == "Consultar":
    PageListCliente.List()

if page_cliente ==  "Incluir":
    PageCreateCliente.Create()

if page_cliente == "Alterar":
    st.title("Alterar Cliente")



# if st.button("Validar"):
#     ClienteController.selecionarTodos()
#     print ('ok')

