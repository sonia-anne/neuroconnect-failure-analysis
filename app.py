
import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(page_title="NeuroConnect Interactive Dashboard", layout="wide")

# Custom styling
st.markdown("""
<style>
    .main {
        background-color: #0f1117;
        color: #ffffff;
        font-family: 'Segoe UI', sans-serif;
    }
</style>
""", unsafe_allow_html=True)

st.title("🧠 NeuroConnect: Comparative Analysis of Autism Treatments")

st.markdown("### Section 3: Why Current Treatments Fail")

# Simulated clinical outcome data
data = {
    "Treatment": ["ABA", "Risperidone", "rTMS", "NeuroConnect"],
    "Improved Non-verbal Communication (%)": [25, 15, 40, 85],
    "Sensory Crisis Reduction (%)": [20, 18, 35, 82],
}

df = pd.DataFrame(data)

# Create interactive grouped bar chart
fig = go.Figure()
fig.add_trace(go.Bar(
    x=df["Treatment"],
    y=df["Improved Non-verbal Communication (%)"],
    name="Non-verbal Communication",
    marker_color='rgb(55, 83, 109)',
    text=df["Improved Non-verbal Communication (%)"],
    textposition='auto'
))
fig.add_trace(go.Bar(
    x=df["Treatment"],
    y=df["Sensory Crisis Reduction (%)"],
    name="Sensory Crisis Reduction",
    marker_color='rgb(26, 118, 255)',
    text=df["Sensory Crisis Reduction (%)"],
    textposition='auto'
))

fig.update_layout(
    barmode='group',
    title="Projected Clinical Impact: NeuroConnect vs Conventional Approaches",
    xaxis_title="Treatment",
    yaxis_title="Improvement (%)",
    template="plotly_dark",
    height=600,
    legend=dict(x=0.7, y=1.15, orientation='h')
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("""
✅ **Insight**: Simulated clinical data suggests NeuroConnect significantly outperforms conventional methods in both communication and sensory regulation metrics.  
It demonstrates the potential of a nano-enabled, AI-guided intervention targeting synaptic connectivity in severe autism spectrum conditions.
""")
