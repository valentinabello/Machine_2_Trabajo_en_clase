# Segmentación K-Means - Despliegue en Streamlit y Docker

Aplicación interactiva construida en Streamlit para clasificar registros en clusters obtenidos con K-Means.

## Estructura del Repositorio
- `app.py`: Aplicación principal de Streamlit.
- `make_demo_model.py`: Script para generar el modelo `model.joblib` de demostración.
- `requirements.txt`: Dependencias de la aplicación.
- `Dockerfile`: Archivo de configuración de Docker.

## Instrucciones de Ejecución Local
1. Crear un entorno virtual e instalar dependencias:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # En Windows: .venv\Scripts\activate
   pip install -r requirements.txt