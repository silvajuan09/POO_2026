
import streamlit as st
from service import Service


class RegistrarAtendimentoUI:

    @staticmethod
    def main():
        st.header("Registrar Atendimento")
        id_profissional = st.session_state["usuario_id"]
        horarios = Service.horario_listar_para_registrar_atendimento(id_profissional)

        if not horarios:
            st.info("Não existem atendimentos disponíveis para registro.")
            return

        def formatar_horario(h):
            cliente = Service.cliente_listar_id(h.get_id_cliente())
            servico = Service.servico_listar_id(h.get_id_servico())

            nome_cliente = cliente.get_nome() if cliente else "Cliente não encontrado"
            nome_servico = servico.get_descricao() if servico else "Serviço não encontrado"

            return (
                f"{h.get_data():%d/%m/%Y %H:%M} - "
                f"{nome_cliente} - {nome_servico}"
            )

        horario = st.selectbox(
            "Selecione o atendimento",
            horarios,
            format_func=formatar_horario
        )
        cliente = Service.cliente_listar_id(
            horario.get_id_cliente()
        )
        servico = Service.servico_listar_id(
            horario.get_id_servico()
        )

        st.subheader("Dados do atendimento")

        st.write(
            "**Cliente:**",
            cliente.get_nome() if cliente else "Não encontrado"
        )
        st.write(
            "**Serviço:**",
            servico.get_descricao() if servico else "Não encontrado"
        )
        st.write(
            "**Data:**",
            horario.get_data().strftime("%d/%m/%Y %H:%M")
        )
        st.divider()

        with st.form("form_registrar_atendimento"):

            queixa = st.text_area(
                "Queixa principal / solicitação"
            )
            historico = st.text_area(
                "Histórico / observações"
            )
            avaliacao = st.text_area(
                "Avaliação do serviço"
            )
            prescricao = st.text_area(
                "Prescrição / recomendações"
            )
            enviar = st.form_submit_button(
                "Registrar Atendimento"
            )

            if enviar:
                try:
                    Service.atendimento_registrar(
                        horario.get_id(),
                        id_profissional,
                        queixa,
                        historico,
                        avaliacao,
                        prescricao
                    )
                    st.success(
                        "Atendimento registrado com sucesso!"
                    )
                    st.rerun()

                except ValueError as erro:

                    st.error(str(erro))