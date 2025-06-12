import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Título do dashboard
st.title("📈 Painel do Ibovespa - Últimos 5 anos")

# Datas para consulta
data_fim = datetime.today()
data_inicio = data_fim - timedelta(days=5*365)

# Ticker do Ibovespa no Yahoo Finance
ticker_ibov = "^BVSP"

# Carregando dados do Ibovespa
st.write("Carregando dados do Ibovespa...")
dados_ibov = yf.download(ticker_ibov, start=data_inicio, end=data_fim)

# Verificação se os dados foram carregados
if dados_ibov.empty:
    st.error("Não foi possível carregar os dados do Ibovespa.")
else:
    # Exibe os dados em tabela
    st.subheader("📊 Dados Históricos (últimos 5 anos)")
    st.dataframe(dados_ibov.tail())

    # Gráfico de preços de fechamento
    st.subheader("📉 Gráfico de Preço de Fechamento do Ibovespa")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(dados_ibov.index, dados_ibov['Close'], color='blue')
    ax.set_title("Fechamento do Ibovespa (5 anos)", fontsize=14)
    ax.set_xlabel("Data")
    ax.set_ylabel("Preço (BRL)")
    ax.grid(True)
    st.pyplot(fig)
