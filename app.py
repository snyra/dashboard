# app.py
import streamlit as st
import pandas as pd
import plotly.express as px

# Leitura do arquivo CSV
car_data = pd.read_csv('vehicles.csv')

# Cabeçalho
st.header("Dashboard de Anúncios de Carros")

# Caixa de seleção para escolher entre histograma e gráfico de dispersão
chart_choice = st.radio("Escolha o tipo de gráfico:", ("Histograma", "Gráfico de Dispersão"))

# Verificar a escolha do usuário e criar o gráfico correspondente
if chart_choice == "Histograma":
    st.write('Criando um histograma para a coluna "odometer"')
    
    # Criar um histograma mais elaborado com cores
    fig_hist = px.histogram(car_data, x="odometer", color="fuel", title="Distribuição de Quilometragem",
                            labels={"odometer": "Quilometragem", "count": "Número de Carros"})
    
    # Exibir o gráfico Plotly interativo
    st.plotly_chart(fig_hist, use_container_width=True)
elif chart_choice == "Gráfico de Dispersão":
    st.write('Criando um gráfico de dispersão para as colunas "odometer" e "price"')
    
    # Criar um gráfico de dispersão mais elaborado com cores e tamanhos diferentes
    fig_scatter = px.scatter(car_data, x="odometer", y="price", color="manufacturer", size="model_year",
                             title="Relação entre Quilometragem e Preço",
                             labels={"odometer": "Quilometragem", "price": "Preço"})
    
    # Exibir o gráfico Plotly interativo
    st.plotly_chart(fig_scatter, use_container_width=True)

