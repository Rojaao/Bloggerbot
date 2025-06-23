
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Robô de Futebol - EV", layout="centered")
st.title("Robô de Análise de Valor Esperado (EV)")
st.write("Exemplo de jogos com cálculos de EV e probabilidade")

# Carrega os dados
df = pd.read_csv("data/exemplo_jogos.csv")

# Destaca onde EV é positivo e prob > 85%
df['Destaque'] = df.apply(lambda row: '🟢' if row['prob_gol'] > 85 and float(row['ev']) > 0 else '', axis=1)

st.dataframe(df)
