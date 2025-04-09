# app.py
import streamlit as st
from pn_junction import simulate_pn_junction
from bjt import simulate_bjt
from jfet import simulate_jfet
from nano_materials import simulate_nanobandgap


import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(page_title="Semiconductor Simulator", page_icon="⚡", layout="centered")

# Title section
st.markdown("""
    <style>
    .title-text {
        font-size: 2.5em;
        font-weight: bold;
        color: #0e4c92;
    }
    .intro {
        font-size: 1.1em;
        color: #333;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title-text">🔬 Semiconductor Device Simulator</div>', unsafe_allow_html=True)
st.markdown('<div class="intro">Welcome to the <strong>Interactive Semiconductor Simulator</strong>!<br>Choose a device from the sidebar to simulate and visualize its behavior.</div>', unsafe_allow_html=True)

# --------------------------
# 💎 Sidebar - Enhanced UI
# --------------------------
st.sidebar.markdown("""
    <style>
    .sidebar-title {
        font-size: 1.6em;
        font-weight: 600;
        color: #0e4c92;
        padding-bottom: 10px;
    }
    .sidebar-info {
        font-size: 0.95em;
        color: #444;
        padding-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

st.sidebar.markdown('<div class="sidebar-title">🔧 Choose a Device</div>', unsafe_allow_html=True)
st.sidebar.markdown('<div class="sidebar-info">Select a semiconductor device to explore its characteristics. Visualize how voltage, current, and other factors affect behavior.</div>', unsafe_allow_html=True)

# Sidebar radio with emojis for a better look
device = st.sidebar.radio("📱 Device Type:", [
    "🔌 PN Junction Diode",
    "🔋 BJT (Bipolar Junction Transistor)",
    "🌀 JFET",
    "🔮 Nano Materials"
])






# ------------------- PN Junction -------------------
if device == "🔌 PN Junction Diode":
    st.header("📈 PN Junction Diode Simulation")

    col1, col2 = st.columns(2)
    with col1:
        voltage_start = st.slider("Voltage Start (V)", -2.0, 0.0, -1.0)
    with col2:
        voltage_end = st.slider("Voltage End (V)", 0.0, 2.0, 1.0)

    temperature = st.slider("Temperature (K)", 250, 400, 300)
    saturation_current = st.number_input("Saturation Current (Is in A)", value=1e-12, format="%.1e")

    if st.button("🔍 Simulate Diode"):
        fig = simulate_pn_junction((voltage_start, voltage_end), temperature, saturation_current, return_fig=True)
        st.pyplot(fig)

        # Explanation
        st.subheader("📖 Characteristics Explained:")
        st.markdown(f"""
        - **Forward Bias (V > 0)**: The current increases **exponentially** as voltage increases.
        - **Reverse Bias (V < 0)**: The current remains nearly **zero**, except for a tiny leakage.
        - **Temperature = {temperature} K** → Thermal voltage increases slightly, making current increase faster in forward bias.
        - **Saturation Current Is = {saturation_current:.1e} A** → Higher Is leads to more leakage in reverse bias.
        """)

# ------------------- BJT Simulation -------------------
elif device == "🔋 BJT (Bipolar Junction Transistor)":
    st.header("🔁 BJT Simulation (Common Emitter Output)")

    beta = st.slider("Current Gain (β)", 50, 300, 100)
    Vce_start, Vce_end = st.slider("Vce Voltage Range (V)", 0.0, 10.0, (0.0, 5.0))
    ib_input = st.text_input("Base Currents (µA, comma-separated)", value="10, 20, 30, 40")

    try:
        Ib_values = [float(i.strip()) for i in ib_input.split(",") if i.strip()]
    except ValueError:
        Ib_values = []

    if st.button("🔍 Simulate BJT"):
        if not Ib_values:
            st.warning("Please enter valid base currents!")
        else:
            fig = simulate_bjt((Vce_start, Vce_end), beta, Ib_values, return_fig=True)
            st.pyplot(fig)

            # Explanation
            st.subheader("📖 Characteristics Explained:")
            ib_list = ", ".join(f"{ib} µA" for ib in Ib_values)
            st.markdown(f"""
            - **Common Emitter Output Characteristics** are shown for base currents: {ib_list}.
            - **As base current (Ib) increases**, collector current (Ic) also increases.
            - **β (gain) = {beta}** → Higher β means a small Ib produces a much larger Ic.
            - The graph shows **saturation region** (flat lines) and **active region** (where Ic ∝ Ib).
            - At higher Vce, the transistor enters **saturation** where further increases in Vce have little effect on Ic.
            """)

# ------------------- Coming Soon -------------------

elif device == "🌀 JFET":
    st.header("📊 JFET Output Characteristics")

    Vds_start, Vds_end = st.slider("Vds Range (V)", 0.0, 10.0, (0.0, 5.0))
    Vgs_input = st.text_input("Gate Voltages Vgs (V, comma-separated)", value="-1, -2, -3")
    Idss = st.number_input("Idss (max drain current at Vgs=0, in A)", value=10e-3, format="%.2e")
    Vp = st.number_input("Pinch-Off Voltage (Vp in V)", value=-4.0)

    try:
        Vgs_values = [float(i.strip()) for i in Vgs_input.split(",") if i.strip()]
    except:
        Vgs_values = []

    if st.button("📈 Simulate JFET"):
        if not Vgs_values:
            st.warning("Please enter valid Vgs values.")
        else:
            fig = simulate_jfet((Vds_start, Vds_end), Vgs_values, Idss, Vp, return_fig=True)
            st.pyplot(fig)

            st.subheader("📖 Characteristics Explained:")
            st.markdown(f"""
            - **Vgs values = {', '.join(str(v) for v in Vgs_values)} V**
            - As Vgs becomes more negative, the channel narrows and **Id decreases**.
            - At **pinch-off (Vgs = Vp)**, current becomes nearly **zero**.
            - The graph shows **Ohmic region**, **Pinch-off**, and **Saturation**.
            """)

elif device == "🔮 Nano Materials":
    st.header("⚛️ Nanomaterial Band Gap Simulation")

    size_min, size_max = st.slider("Particle Size Range (nm)", 1.0, 10.0, (1.0, 6.0))
    Eg_bulk = st.number_input("Bulk Band Gap (eV)", value=1.1)
    alpha = st.slider("Quantum Confinement Factor (α)", 0.5, 3.0, 1.5)

    if st.button("🔬 Simulate Band Gap"):
        fig = simulate_nanobandgap((size_min, size_max), Eg_bulk, alpha, return_fig=True)
        st.pyplot(fig)

        st.subheader("📖 Characteristics Explained:")
        st.markdown(f"""
        - **Quantum Confinement**: Smaller particles lead to **larger band gaps**.
        - Bulk Band Gap = {Eg_bulk} eV  
        - As size decreases, band gap increases due to energy quantization.
        - Important for **LEDs, solar cells, quantum dots**.
        """)


else:
    st.info("This module will be available soon. Stay tuned!")





