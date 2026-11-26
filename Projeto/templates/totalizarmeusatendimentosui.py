
import streamlit as st
import pandas as pd
from datetime import date
from service import Service


class TotalizarMeusAtendimentosUI:

    @staticmethod
    def main():
        st.header("Totalizar Meus Atendimentos")
        id_profissional = st.session_state["usuario_id"]
        profissional = Service.profissional_listar_id(id_profissional)

        st.write(f"Profissional: **{profissional.get_nome()}**")
        with st.form("form_totalizar_meus_atendimentos"):
            col1, col2 = st.columns(2)
            data_inicial = col1.date_input(
                "Data inicial",
                value=date.today().replace(day=1)
            )
            data_final = col2.date_input(
                "Data final",
                value=date.today()
            )
            consultar = st.form_submit_button("Gerar relatório")

        if consultar:
            try:
                dados = Service.atendimento_totalizar_servicos_profissional(
                    id_profissional,
                    data_inicial,
                    data_final
                )
                df = pd.DataFrame(
                    dados,
                    columns=["Serviço", "Quantidade"]
                )
                st.subheader("Resultado")

                total = int(df["Quantidade"].sum())

                st.metric(
                    "Total de atendimentos",
                    total
                )
                st.dataframe(
                    df,
                    use_container_width=True,
                    hide_index=True
                )
                st.subheader("Atendimentos por tipo de serviço")

                if len(df) > 0:
                    grafico = df.set_index("Serviço")
                    st.bar_chart(grafico)
                else:
                    st.info("Nenhum serviço cadastrado.")

            except ValueError as erro:
                st.error(str(erro))