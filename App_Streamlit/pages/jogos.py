import streamlit as st
import pandas as pd
from datetime import date

# Título do aplicativo Streamlit
st.title("Jogos do dia")

# Data de análise (usuário seleciona)
dia = st.date_input("Data de analise", date.today())


# Função para carregar os dados de jogos
def load_data_jogos(dia):
    # Formatar a data corretamente para o nome do arquivo
    dia_str = dia.strftime("%d%m%Y")

    # Construir a URL para acessar o arquivo CSV raw no GitHub
    url = f"https://raw.githubusercontent.com/CMatheus7/Jogos_do_Dia_FlashScore/main/jogos_{dia_str}.csv"

    try:
        # Carregar o CSV diretamente
        data_jogos = pd.read_csv(url)
        return data_jogos
    except Exception as e:
        st.error(f"Erro ao carregar os dados: {e}")
        return pd.DataFrame()  # Retorna um DataFrame vazio em caso de erro


# Carregar os dados dos jogos para a data selecionada
df_jogos = load_data_jogos(dia)

# Exibir os dados no Streamlit, se existirem
if not df_jogos.empty:
    st.dataframe(df_jogos)
else:
    st.write("Nenhum jogo encontrado para a data selecionada.")
