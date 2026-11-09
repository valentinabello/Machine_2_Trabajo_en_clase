from pathlib import Path
import pandas as pd
import joblib
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

BASE_DIR = Path(__file__).resolve().parent

# 1. Cargar los datos reales (usamos la URL pública para que no dependas del archivo local)
url = "https://raw.githubusercontent.com/kennedykwangari/Mall-Customer-Segmentation-Data/master/Mall_Customers.csv"
df = pd.read_csv(url)

# 2. Definir las variables que tu compañero usó para segmentar
features = ["Annual Income (k$)", "Spending Score (1-100)"]

# 3. Construir el pipeline de entrenamiento (Escalado + KMeans con K=5)
# Usamos los 5 clusters que definimos con el método del codo
model = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler()),
    ("cluster", KMeans(n_clusters=5, random_state=42, n_init=10))
])

# 4. Entrenar el modelo con los datos
model.fit(df[features])

# 5. Crear el artefacto final con los perfiles reales que definimos antes
artifact = {
    "model": model,
    "features": features,
    "numeric_features": features,
    "categorical_features": [],
    "task": "clustering",
    "cluster_descriptions": {
        0: "Cliente promedio: Ingreso medio y Gasto medio.",
        1: "Cliente objetivo (VIP): Ingreso alto y Gasto alto.",
        2: "Gastador impulsivo: Ingreso bajo y Gasto alto.",
        3: "Ahorrador / Conservador: Ingreso alto y Gasto bajo.",
        4: "Bajo potencial: Ingreso bajo y Gasto bajo."
    }
}

# 6. Guardar el modelo para que la app de Streamlit lo pueda usar
MODEL_PATH = BASE_DIR / "model.joblib"
joblib.dump(artifact, MODEL_PATH)
print(f"Modelo real de Mall Customers generado exitosamente en: {MODEL_PATH}")