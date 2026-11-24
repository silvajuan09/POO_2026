import streamlit as st
from service import Service
import time

class AbrirContaUI:
    def main():
        st.header("Abrir Conta no Sistema")
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o fone")
        senha = st.text_input("Informe a senha", type="password")
        foto = st.file_uploader("Selecione uma foto de perfil", type=["png", "jpg", "jpeg", "webp"])
        if foto is not None:
            st.image(
                foto,
                caption="Pré-visualização da foto",
                width=150
            )
        if st.button("Inserir"):
            try:
                imagem = foto.getvalue() if foto is not None else None
                Service.cliente_inserir(nome, email, fone, senha, imagem)
                st.success("Conta criada com sucesso")
                time.sleep(2)
                st.rerun()
            except ValueError as erro:
                st.error(str(erro))
            