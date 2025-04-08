
import streamlit as st
import plotly.graph_objects as go
import taichi as ti
import numpy as np

st.set_page_config(page_title="NeuroConnect Dashboard", layout="wide")

st.title("📊 NeuroConnect: Fallos de Tratamientos Actuales para el Autismo")

# Datos de ejemplo
tratamientos = ["ABA", "Risperidona", "EMT", "NeuroConnect"]
mejoras = [25, 15, 40, 85]  # Valores en %

fig = go.Figure(data=[
    go.Bar(name='Mejora en Comunicación No Verbal', x=tratamientos, y=mejoras),
])

fig.update_layout(
    title="Comparativa de Eficacia: NeuroConnect vs Tratamientos Actuales",
    xaxis_title="Tratamiento",
    yaxis_title="Mejora (%)",
    template="plotly_dark",
    height=500
)

st.plotly_chart(fig, use_container_width=True)

# Efecto Taichi simulado (por GPU en fondo)
ti.init(arch=ti.gpu)

n = 320 * 240
pixels = ti.field(dtype=float, shape=n)

@ti.kernel
def render(t: float):
    for i in pixels:
        x = (i % 320) / 320.0
        y = (i // 320) / 240.0
        pixels[i] = (ti.sin(10 * x + t) + ti.cos(10 * y + t)) * 0.5 + 0.5

canvas = st.empty()
for frame in range(60):
    render(frame * 0.03)
    canvas.line_chart(np.reshape(pixels.to_numpy(), (240, 320)))
