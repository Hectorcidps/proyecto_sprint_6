import pandas as pd 
import plotly.express as px 
import streamlit as st 

# leer el CSV con la informacion necesaria 
car_data = pd.read_csv('./vehicles_us.csv')

# Crear un encabezado 
st.header('Anuncios de ventas de coches')

# Crear un checkbox para construir un histograma 
hist_checkbox = st.checkbox('Ver Histograma')

if hist_checkbox:
    # Mensaje al presionar el boton 'Ver Histograma'
    st.write('Creación de un histograma con la información del conjunto de datos de anuncios de venta de coches')
    
    # crear el histograma 
    histo = px.histogram(car_data,
                         x='odometer', 
                         color_discrete_sequence=px.colors.qualitative.Vivid)
    
    # mostrar el grafico 
    st.plotly_chart(histo, use_container_width=True)


# Crear un checkbox para construir un grafico de dispersion 
scatter_checkbox = st.checkbox('Ver Gráfico de dispersión')

if scatter_checkbox:
    st.write('Creación de un gráfico de dispersión con la información del conjunto de datos de anuncios de venta de coches')
    
    # crear el scatter
    scatter = px.scatter(car_data,
                         x='odometer',
                         y='price',
                         color_continuous_scale='Inferno',
                         template='plotly_dark')
    
    # mostrar el grafico 
    st.plotly_chart(scatter, use_container_width=True )