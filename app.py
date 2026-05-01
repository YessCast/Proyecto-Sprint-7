import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objs as go

# Leer el archivo CSV con los datos de los vehículos
car_data = pd.read_csv(
    'https://raw.githubusercontent.com/YessCast/Proyecto-Sprint-7/refs/heads/main/vehicles_us.csv')

# Encabezado de la aplicación
st.header('Car Data Analysis')


# Botón para gradicar un grafico de dispersión
button_scatter = st.button('Graficar gráfico de dispersión')


# Crear una casilla de selección para elegir el tipo de gráfico
chart_type = st.selectbox('Selecciona el tipo de gráfico', [
                          'Histograma', 'Gráfico de dispersión'])
# Lógica para mostrar el gráfico seleccionado
if chart_type == 'Histograma':

    # Escribir un mensaje en la aplicación
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear una figura de Plotly
    fig = go.Figure()

    # Agregar un gráfico de dispersión para visualizar la relación entre el año y el precio
    fig.add_trace(go.Scatter(
        x=car_data['year'], y=car_data['price'], mode='markers', name='Price vs Year'))

    # Configurar el diseño del gráfico
    fig.update_layout(title='Price vs Year of Vehicles',
                      xaxis_title='Year',
                      yaxis_title='Price',
                      showlegend=True)

    st.plotly_chart(fig, use_container_width=True)

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig)
elif chart_type == 'Gráfico de dispersión':
    # Escribir un mensaje en la aplicación
    st.write('Creación de un gráfico de dispersión ')

    # Crear una figura de Plotly
    fig = go.Figure()

    # Agregar un gráfico de dispersión para visualizar la relación entre el año y el precio
    fig.add_trace(go.Scatter(
        x=car_data['year'], y=car_data['price'], mode='markers', name='Price vs Year'))

    # Configurar el diseño del gráfico
    fig.update_layout(title='Price vs Year of Vehicles',
                      xaxis_title='Year',
                      yaxis_title='Price',
                      showlegend=True)

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig, use_container_width=True)
