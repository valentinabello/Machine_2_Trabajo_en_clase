import joblib
import pandas as pd
import streamlit as st

st.title("Segmentación de Clientes con K-Means")
st.write(
    "Esta aplicación agrupa a los clientes según sus ingresos anuales y su"
    " puntuación de gasto."
)

# Cargar el modelo que subiste a GitHub (asegúrate de que el nombre coincida)
try:
  model = joblib.load("modelo.joblib")
  modelo_cargado = True
except Exception as e:
  modelo_cargado = False

# Sliders para que el profe mueva los valores y pruebe
annual_income = st.slider("Ingresos Anuales (k$)", 10, 140, 50)
spending_score = st.slider("Puntuación de Gasto (1-100)", 1, 100, 50)

if modelo_cargado:
  # Hacer la predicción con los datos del usuario
  # Nota: si entrenaste tu K-Means con un DataFrame que tenga los nombres de columnas,
  # puedes pasarlo como DataFrame o como lista doble [[annual_income, spending_score]]
  datos_usuario = [[annual_income, spending_score]]
  cluster_predicho = model.predict(datos_usuario)[0]

  st.success(
      f"El cliente pertenece al clúster: **Clúster {cluster_predicho}**"
  )
else:
  st.warning(
      "No se pudo cargar el archivo modelo.joblib. Revisa el nombre en"
      " GitHub."
  )
