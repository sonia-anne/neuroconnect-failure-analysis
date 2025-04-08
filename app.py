
import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(page_title="NeuroConnect Dashboard", layout="wide")

# Encabezado y estilo
st.markdown("""
<style>
    .main {
        background-color: #0f1117;
        color: #ffffff;
        font-family: 'Segoe UI', sans-serif;
    }
</style>
""", unsafe_allow_html=True)

st.title("🧠 NeuroConnect: Comparativa de Tratamientos para el Autismo")

st.markdown("### Estado del Arte: ¿Por qué fallan los tratamientos actuales?")

# Datos simulados para demostración
data = {
    "Tratamiento": ["ABA", "Risperidona", "EMT", "NeuroConnect"],
    "Mejora en comunicación no verbal (%)": [25, 15, 40, 85],
    "Reducción de crisis sensoriales (%)": [20, 18, 35, 82],
}

df = pd.DataFrame(data)

# Crear gráfico interactivo
fig = go.Figure()
fig.add_trace(go.Bar(
    x=df["Tratamiento"],
    y=df["Mejora en comunicación no verbal (%)"],
    name="Comunicación no verbal",
    text=df["Mejora en comunicación no verbal (%)"],
    textposition='auto'
))
fig.add_trace(go.Bar(
    x=df["Tratamiento"],
    y=df["Reducción de crisis sensoriales (%)"],
    name="Crisis sensoriales",
    text=df["Reducción de crisis sensoriales (%)"],
    textposition='auto'
))

fig.update_layout(
    barmode='group',
    title="Comparación de Eficacia de Tratamientos",
    xaxis_title="Tratamiento",
    yaxis_title="Mejora (%)",
    template="plotly_dark",
    legend=dict(x=0.8, y=1.2),
    height=600
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("✅ NeuroConnect muestra una eficacia significativamente superior en ambas categorías analizadas, según simulaciones clínicas proyectadas.")
