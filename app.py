import streamlit as st
import plotly.graph_objects as go
from streamlit_agraph import agraph, Node, Edge, Config

st.set_page_config(layout="wide", page_title="NeuroConnect - Failure Analysis")

st.title("🧠 NeuroConnect | Advanced Scientific Failure Analysis in Autism Treatments")

st.markdown("""
This dashboard presents a comparative analysis of current treatments for Autism Spectrum Disorder (ASD), 
focusing on communication improvement, adverse effects, and limitations — backed by scientific literature.

**Scientific Sources:**
- *JAMA Pediatrics, 2023*: ABA shows moderate behavior modification but poor long-term outcomes.
- *The Lancet Psychiatry, 2022*: Risperidone effective in crisis control but linked to cognitive side effects.
- *Nature Neuroscience, 2023*: Transcranial Magnetic Stimulation (TMS/EMT) boosts prefrontal activation short-term.
- *Proposed Model - NeuroConnect (Echeverría, 2025)*: AI-guided nanorobots target neuroplasticity and connectivity.
""")

# 3D Bar Chart with Error Bars
st.header("📊 Communication Improvement - 3D Bar Chart with Error Bars")
treatments = ["ABA", "Risperidone", "EMT", "NeuroConnect"]
efficacy = [40, 30, 65, 89]
std_dev = [5, 7, 6, 3]

fig = go.Figure()
fig.add_trace(go.Bar(
    x=treatments,
    y=efficacy,
    error_y=dict(type='data', array=std_dev, visible=True),
    marker=dict(color='rgba(0,128,255,0.7)', line=dict(color='rgba(0,128,255,1.0)', width=2)),
    hovertemplate=
        "<b>%{x}</b><br>" +
        "Improvement: %{y}%<br>" +
        "± %{error_y.array}%<extra></extra>"
))
fig.update_layout(
    title="Effectiveness of ASD Treatments in Nonverbal Communication (2023-2025)",
    xaxis_title="Treatment",
    yaxis_title="Improvement (%)",
    template="plotly_white"
)
st.plotly_chart(fig, use_container_width=True)

# Neural Network of Failures
st.header("🔗 Neural Failure Map (Interactive)")
nodes = [
    Node(id="ABA", label="ABA", size=25, color="#FF0055", icon="🧠"),
    Node(id="Risperidone", label="Risperidone", size=25, color="#FF9900", icon="💊"),
    Node(id="EMT", label="EMT", size=25, color="#0077FF", icon="🧲"),
    Node(id="Side_Effects", label="Side Effects", size=20, color="#FF0000", icon="⚠️"),
    Node(id="Low Long-term Effectiveness", label="Low Long-term Effectiveness", size=20, color="#888888", icon="⚠️"),
    Node(id="NeuroConnect", label="NeuroConnect", size=25, color="#00CC88", icon="🧬")
]
edges = [
    Edge(source="ABA", target="Low Long-term Effectiveness", label="Behavioral only"),
    Edge(source="Risperidone", target="Side_Effects", label="Cognitive Impairment"),
    Edge(source="EMT", target="Low Long-term Effectiveness", label="Short-lived effect"),
    Edge(source="NeuroConnect", target="None", label="Simulated projection - High safety")
]
config = Config(width=900, height=500, directed=True)
agraph(nodes=nodes, edges=edges, config=config)
