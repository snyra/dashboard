import streamlit as st
import pandas as pd
import plotly.express as px

# Leitura do arquivo CSV
car_data = pd.read_csv('vehicles.csv')

# Cabeçalho
st.header("Dashboard de Anúncios de Carros")

# Botão para criar histograma
hist_button = st.button('Criar Histograma')

if hist_button:
    st.write('Criando um histograma para a coluna "odometer"')
    
    # Criar um histograma
    fig_hist = px.histogram(car_data, x="odometer")
    
    # Exibir o gráfico Plotly interativo
    st.plotly_chart(fig_hist, use_container_width=True)

# Adicionar outro botão para criar um gráfico de dispersão
scatter_button = st.button('Criar Gráfico de Dispersão')

if scatter_button:
    st.write('Criando um gráfico de dispersão para as colunas "odometer" e "price"')
    
    # Criar um gráfico de dispersão
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    
    # Exibir o gráfico Plotly interativo
    st.plotly_chart(fig_scatter, use_container_width=True)
