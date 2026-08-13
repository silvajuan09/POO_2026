import streamlit as st
from paciente import Paciente

class PacienteUI:
    def main():
        st.header("Dados do Paciente")
        nome = st.text_input('Nome: ')
        cpf = st.text_input('CPF (apenas números): ')
        fone = st.text_input('Telefone: ')
        nascimento = st.text_input('Data de nascimento: ')
        if st.button('Idade'):
            classe = Paciente(nome, cpf, fone, nascimento)
            st.write(f'{classe.idade()}')
            st.write(classe)