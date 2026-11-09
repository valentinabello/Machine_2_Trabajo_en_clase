import joblib
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

st.title("Segmentación de Clientes con K-Means")
st.write(
    "Esta aplicación agrupa a los clientes según sus ingresos anuales y su"
    " puntuación de gasto."
)

# Sliders para que el profe mueva los valores y pruebe
annual_income = st.slider("Ingresos Anuales (k$)", 10, 140, 50)
spending_score = st.slider("Puntuación de Gasto (1-100)", 1, 100, 50)

# Aquí puedes cargar tu modelo cuando lo tengas conectado
# model = joblib.load('modelo.joblib')

st.write(f"El cliente pertenece al clúster: **Ejemplo Clúster 1**")
