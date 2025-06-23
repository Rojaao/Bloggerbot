
import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Robô de Futebol - Dados Reais", layout="wide")
st.title("Robô de Futebol com Dados Reais e Atualização em Tempo Real")

tab1, tab2 = st.tabs(["⚽ Jogos AO VIVO", "📅 Jogos FUTUROS"])

# Placeholder - dados fictícios temporários para estrutura visual
now = datetime.now().strftime("%H:%M:%S")
with tab1:
    st.subheader("Jogos ao vivo (atualizado às {})".format(now))
    st.write("🔄 Em breve: dados reais de partidas em andamento com estatísticas de escanteios e gols.")

with tab2:
    st.subheader("Jogos futuros com análise pré-live")
    df = pd.read_csv("data/jogos_futuros.csv")
    df['Destaque'] = df.apply(lambda row: '🟢' if row['prob_gol'] > 85 and float(row['ev']) > 0 else '', axis=1)
    st.dataframe(df)
