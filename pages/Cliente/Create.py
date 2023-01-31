import streamlit as st
import Controllers.ClienteController as ClienteController
import models.Cliente as cliente

def Create():
    st.title("Incluir Cliente")
    with st.form(key="include_cliente"):
        input_name = st.text_input("Insira p seu nome")
        input_age = st.number_input("Insira sua idade", format="%d", step=1)
        input_occupation = st.selectbox("Selecione sua profissão",['Desenvolvedor', 'Programador', 'musico'])
        input_button_submit = st.form_submit_button("Enviar")

    if input_button_submit:
        ClienteController.Incluir(cliente.Cliente(0, input_name, input_age, input_occupation))
        st.success("Cliente Inlcuido com sucesso")