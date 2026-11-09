import os
import joblib
import pandas as pd
import streamlit as st

st.title("Segmentación de Clientes con K-Means")
st.write("Archivos disponibles en la carpeta:")

# Esto mostrará en pantalla todos los archivos que Python ve en el repositorio
archivos_en_carpeta = os.listdir(".")
st.write(archivos_en_carpeta)

# Intentar cargar el modelo dinámicamente según lo que encuentre
modelo_cargado = False
model = None

for archivo in archivos_en_carpeta:
  if archivo.endswith(".joblib") or archivo.endswith(".pkl"):
    try:
      model = joblib.load(archivo)
      st.success(f"¡Modelo cargado exitosamente desde: {archivo}!")
      modelo_cargado = True
      break
    except Exception as e:
      st.error(f"Error al cargar {archivo}: {e}")

annual_income = st.slider("Ingresos Anuales (k$)", 10, 140, 50)
spending_score = st.slider("Puntuación de Gasto (1-100)", 1, 100, 50)

if modelo_cargado:
  datos_usuario = [[annual_income, spending_score]]
  cluster_predicho = model.predict(datos_usuario)[0]
  st.success(f"El cliente pertenece al clúster: **Clúster {cluster_predicho}**")
else:
  st.warning(
      "No se encontró ningún archivo .joblib o .pkl válido en la carpeta."
  )
