import joblib
import pandas as pd
import streamlit as st

st.title("Segmentación de Clientes con K-Means")
st.write(
    "Esta aplicación agrupa a los clientes según sus ingresos anuales y su"
    " puntuación de gasto."
)

# Cargar el archivo
try:
  objeto_cargado = joblib.load("model.joblib")
  modelo_cargado = True
except Exception as e:
  modelo_cargado = False
  st.error(f"Error al cargar el archivo: {e}")

# Sliders para que el profe mueva los valores y pruebe
annual_income = st.slider("Ingresos Anuales (k$)", 10, 140, 50)
spending_score = st.slider("Puntuación de Gasto (1-100)", 1, 100, 50)

if modelo_cargado:
  try:
    # Verificamos si lo cargado es un diccionario
    if isinstance(objeto_cargado, dict):
      model = None
      for k in ["model", "modelo", "kmeans", "KMeans"]:
        if k in objeto_cargado:
          model = objeto_cargado[k]
          break
      if model is None:
        for val in objeto_cargado.values():
          if hasattr(val, "predict"):
            model = val
            break
    else:
      model = objeto_cargado

    if model is not None and hasattr(model, "predict"):
      datos_usuario = [[annual_income, spending_score]]
      cluster_predicho = model.predict(datos_usuario)[0]
      st.success(
          f"El cliente pertenece al clúster: **Clúster {cluster_predicho}**"
      )
    else:
      st.error(
          "No se encontró un modelo de Machine Learning válido dentro del"
          " archivo."
      )

  except Exception as e:
    st.error(f"Error al hacer la predicción: {e}")
