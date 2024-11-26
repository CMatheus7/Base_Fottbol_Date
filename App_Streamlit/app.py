# Importando as bibliotecas necessárias
import streamlit as st  # Streamlit para criar a interface web
import pandas as pd  # Pandas para manipulação de dados
import numpy as np  # Numpy para operações numéricas (não utilizado diretamente, mas importado)

# Título do aplicativo Streamlit
st.title("FOOTBALL DATA")

# Adicionando a barra lateral com as opções para o usuário escolher a liga
st.sidebar.header("league")
selected_league = st.sidebar.selectbox(
    "league", ["England", "Germany", "Italy", "Spain", "France"]
)

# Adicionando a barra lateral com as opções para o usuário escolher a temporada
st.sidebar.header("season")
selected_season = st.sidebar.selectbox(
    "Season",
    [
        "2013/2014",
        "2014/2015",
        "2015/2016",
        "2016/2017",
        "2017/2018",
        "2018/2019",
        "2019/2020",
        "2020/2021",
        "2021/2022",
        "2022/2023",
        "2023/2024",
        "2024/2025",
    ],
)


# Função para carregar os dados de futebol via web scraping
def load_data(league, season):
    # Mapeando o nome da liga selecionada para o código correspondente
    if selected_league == "England":
        league = "E0"  # Código para a liga da Inglaterra
    if selected_league == "Germany":
        league = "D1"  # Código para a liga da Alemanha
    if selected_league == "Italy":
        league = "I1"  # Código para a liga da Itália
    if selected_league == "Spain":
        league = "SP1"  # Código para a liga da Espanha
    if selected_league == "France":
        league = "F1"  # Código para a liga da França

    # Mapeando o nome da temporada para o formato necessário
    if selected_season == "2012/2013":
        season = "1213"
    if selected_season == "2013/2014":
        season = "1314"
    if selected_season == "2014/2015":
        season = "1415"
    if selected_season == "2015/2016":
        season = "1516"
    if selected_season == "2016/2017":
        season = "1617"
    if selected_season == "2017/2018":
        season = "1718"
    if selected_season == "2018/2019":
        season = "1819"
    if selected_season == "2019/2020":
        season = "1920"
    if selected_season == "2020/2021":
        season = "2021"
    if selected_season == "2021/2022":
        season = "2122"
    if selected_season == "2022/2023":
        season = "2223"
    if selected_season == "2023/2024":
        season = "2324"
    if selected_season == "2024/2025":
        season = "2425"

    # Construindo a URL para acessar o arquivo CSV com os dados
    url = "https://www.football-data.co.uk/mmz4281/" + season + "/" + league + ".csv"

    # Carregando os dados CSV a partir da URL
    data = pd.read_csv(url)
    return data


# Carregando os dados para o campeonato e temporada selecionados
df = load_data(selected_league, selected_season)

# Exibindo o título da seção de dados com o nome da liga selecionada
st.subheader("Dataframe: " + selected_league)

# Exibindo o dataframe carregado na interface Streamlit
st.dataframe(df)
