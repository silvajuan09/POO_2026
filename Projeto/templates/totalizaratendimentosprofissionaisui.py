
import streamlit as st
import pandas as pd
from datetime import date
from service import Service


class TotalizarAtendimentosProfissionaisUI:

    @staticmethod
    def main():
        st.header("Totalizar Atendimentos dos Profissionais")
        with st.form("form_totalizar_profissionais"):
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
                dados = Service.atendimento_totalizar_profissionais(
                    data_inicial,
                    data_final
                )
                df = pd.DataFrame(
                    dados,
                    columns=["Profissional", "Atendimentos"]
                )
                st.subheader("Resultado")

                total = int(df["Atendimentos"].sum())

                st.metric(
                    "Total de atendimentos",
                    total
                )
                st.dataframe(
                    df,
                    use_container_width=True,
                    hide_index=True
                )
                st.subheader("Atendimentos por profissional")

                if len(df) > 0:
                    grafico = df.set_index("Profissional")
                    st.bar_chart(grafico)
                else:
                    st.info("Nenhum profissional cadastrado.")

            except ValueError as erro:
                st.error(str(erro))