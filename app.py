import joblib  # o pickle para cargar tu modelo entrenado
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

st.setTitle('Segmentación de Clientes con K-Means')
st.write(
    'Esta aplicación agrupa a los clientes según sus ingresos anuales y su'
    ' puntuación de gasto.'
)

# Sliders para que el profe mueva los valores y pruebe
annual_income = st.slider('Ingresos Anuales (k$)', 10, 140, 50)
spending_score = st.slider('Puntuación de Gasto (1-100)', 1, 100, 50)

# Aquí cargarías tu modelo previamente guardado (ej. model = joblib.load('kmeans_model.pkl'))
# y harías la predicción para el punto ingresado:
# cluster = model.predict([[annual_income, spending_score]])

st.write(f'El cliente pertenece al clúster: **Ejemplo Clúster 1**')