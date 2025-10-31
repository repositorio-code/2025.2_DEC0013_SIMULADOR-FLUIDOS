import streamlit as st

def configure_page():
    """Configura as propriedades da página Streamlit"""
    st.set_page_config(
        page_title="Simulação de Escoamento",
        page_icon="🌊",
        layout="wide",
        initial_sidebar_state="expanded"
    )

# Constantes físicas
GRAVITY = 9.81  # m/s²
GAS_CONSTANT = 8.314  # J/(mol·K)
AIR_GAS_CONSTANT = 287.05  # J/(kg·K)

# Materiais de tubulação e suas rugosidades
TUBE_MATERIALS = {
    "PVC": 0.0000015,
    "Cobre": 0.0000015,
    "Aço comercial": 0.000045,
    "Aço galvanizado": 0.00015,
    "Concreto": 0.0003,
    "Ferro fundido": 0.00026,
    "Personalizado": None
}

# Velocidades recomendadas para água (m/s)
WATER_VELOCITY_MIN = 0.5
WATER_VELOCITY_MAX = 3.0

# Velocidade máxima recomendada para ar (m/s)
AIR_VELOCITY_MAX = 15.0
