
import streamlit as st
from service import Service
import time


class PerfilProfissionalUI:

    def main():
        st.header("Meus Dados")
        op = Service.profissional_listar_id(st.session_state["usuario_id"])
        st.subheader("Foto de perfil")

        if op.get_foto():
            st.image(
                op.get_foto(),
                width=180,
                caption="Foto atual"
            )
        else:
            st.info("Você ainda não possui uma foto de perfil.")

        foto = st.file_uploader(
            "Escolha uma nova foto",
            type=["png", "jpg", "jpeg", "webp"],
            key="foto_perfil_profissional"
        )

        if foto is not None:
            st.image(
                foto,
                width=180,
                caption="Pré-visualização da nova foto"
            )

        st.divider()

        nome = st.text_input("Informe o novo nome", op.get_nome())
        email = st.text_input("Informe o novo e-mail", op.get_email())
        especialidade = st.text_input("Informe a nova especialidade", op.get_especialidade())
        senha = st.text_input("Informe a nova senha", op.get_senha(), type="password")

        if st.button("Atualizar"):
            try:
                id = op.get_id()
                imagem = foto.getvalue() if foto is not None else None
                Service.profissional_atualizar(id, nome, email, especialidade, senha, imagem)
                st.success("Perfil atualizado com sucesso!")
                time.sleep(2)
                st.rerun()
            except ValueError as erro:
                st.error(str(erro))