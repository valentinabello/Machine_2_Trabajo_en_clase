import joblib
import pandas as pd
import streamlit as st

st.title("Segmentación de Clientes con K-Means")
st.write(
    "Esta aplicación agrupa a los clientes según sus ingresos anuales y su"
    " puntuación de gasto."
)

# Cargar el modelo
try:
  model = joblib.load("model.joblib")
  modelo_cargado = True
except Exception as e:
  modelo_cargado = False

# Sliders para que el profe mueva los valores y pruebe
annual_income = st.slider("Ingresos Anuales (k$)", 10, 140, 50)
spending_score = st.slider("Puntuación de Gasto (1-100)", 1, 100, 50)

if modelo_cargado:
  try:
    # Creamos un DataFrame con los nombres exactos de las columnas que usa K-Means
    # (Generalmente 'Annual Income (k$)' y 'Spending Score (1-100)' en este dataset)
    datos_usuario = pd.DataFrame(
        [[annual_income, spending_score]],
        columns=["Annual Income (k$)", "Spending Score (1-100)"],
    )

    cluster_predicho = model.predict(datos_usuario)[0]
    st.success(
        f"El cliente pertenece al clúster: **Clúster {cluster_predicho}**"
    )
  except Exception as e:
    # Si las columnas con nombre fallan, intentamos pasarlo como matriz simple de números
    try:
      cluster_predicho = model.predict([[annual_income, spending_score]])[0]
      st.success(
          f"El cliente pertenece al clúster: **Clúster {cluster_predicho}**"
      )
    except Exception as err:
      st.error(f"Error al hacer la predicción: {err}")
else:
  st.warning("No se pudo cargar el modelo model.joblib.")
