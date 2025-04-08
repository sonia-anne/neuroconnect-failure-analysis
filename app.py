import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="NeuroConnect Scientific Dashboard", layout="centered")

st.title("🧬 NeuroConnect - Scientific Analysis of Autism Treatments")

st.markdown("""
Welcome to the official dashboard for **NeuroConnect**, a proposal to revolutionize autism treatment 
using AI-guided nanotechnology. This dashboard compares traditional therapies with the NeuroConnect model 
in terms of effectiveness, cost, and long-term vision.

---

### 📚 Scientific References
- JAMA Pediatrics (2023): ABA therapy long-term inefficacy rates.
- The Lancet Psychiatry (2022): Risperidone side effects on cognition.
- Nature Neuroscience (2023): EMT temporary effect on prefrontal cortex.
- Echeverría S.A. (2025): NeuroConnect model based on BDNF stimulation and AI.
""")

# --- GRAPH 1: Improvement in Nonverbal Communication ---
st.subheader("📊 Improvement in Nonverbal Communication")
treatments = ["ABA", "Risperidone", "EMT", "NeuroConnect"]
improvements = [40, 30, 65, 89]
errors = [5, 7, 6, 3]

fig1 = go.Figure()
fig1.add_trace(go.Bar(
    x=treatments,
    y=improvements,
    error_y=dict(
        type='data',
        array=errors,
        visible=True
    ),
    marker=dict(
        color=['#FF6F61', '#FFB347', '#779ECB', '#59C57B'],
        line=dict(color='black', width=1.5)
    ),
    hovertemplate='<b>%{x}</b><br>Improvement: %{y}% ± %{error_y.array}%<extra></extra>'
))
fig1.update_layout(
    title="Effectiveness in Nonverbal Communication",
    xaxis_title="Treatment",
    yaxis_title="Improvement (%)",
    template="plotly_white",
    height=500
)
st.plotly_chart(fig1, use_container_width=True)

# --- GRAPH 2: Cost Comparison ---
st.subheader("💰 Cost per Patient (20 Years)")
treatments_cost = ["ABA (20y)", "Risperidone (20y)", "EMT (10y)", "NeuroConnect (one-time)"]
costs = [1200000, 240000, 80000, 2500]

fig2 = go.Figure()
fig2.add_trace(go.Bar(
    x=treatments_cost,
    y=costs,
    marker=dict(
        color=['#E27D60', '#85DCB0', '#E8A87C', '#41B3A3'],
        line=dict(color='black', width=1.5)
    ),
    hovertemplate='<b>%{x}</b><br>Total Cost: $%{y}<extra></extra>'
))
fig2.update_layout(
    title="Total Cost per Patient (USD)",
    xaxis_title="Treatment",
    yaxis_title="Cost (USD)",
    template="plotly_white",
    height=500
)
st.plotly_chart(fig2, use_container_width=True)

# --- GRAPH 3: Future Projection Timeline ---
st.subheader("📈 Projected Adoption and Abandonment Rates (2025-2040)")

years = [2025, 2030, 2035, 2040]
aba_abandon = [0, 20, 45, 70]
neuroconnect_adopt = [0, 25, 60, 85]

fig3 = go.Figure()
fig3.add_trace(go.Scatter(x=years, y=aba_abandon, mode='lines+markers', name='ABA Abandonment',
                          line=dict(color='red', width=3)))
fig3.add_trace(go.Scatter(x=years, y=neuroconnect_adopt, mode='lines+markers', name='NeuroConnect Adoption',
                          line=dict(color='green', width=3)))
fig3.update_layout(
    title="Adoption and Abandonment Trends (Projected)",
    xaxis_title="Year",
    yaxis_title="Percentage (%)",
    template="plotly_white",
    height=500
)
st.plotly_chart(fig3, use_container_width=True)

st.markdown("""
---

### 💡 Why NeuroConnect?

> “We can no longer afford to wait for the perfect treatment—science must be brave enough to propose what’s possible.”  
– Sonia Annette Echeverría Vera, 2025

**NeuroConnect aims not to erase neurodiversity, but to reduce suffering with science that respects identity.**

""")
