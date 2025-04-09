# PN Junction module
import numpy as np
import matplotlib.pyplot as plt

def simulate_pn_junction(V_range=(-1, 1), T=300, Is=1e-12, return_fig=False):
    """
    Simulate and plot I-V characteristics of a PN junction diode.
    
    Parameters:
    - V_range: Tuple (start, end) for voltage range (in Volts)
    - T: Temperature in Kelvin
    - Is: Saturation current (in Amps)
    - return_fig: If True, returns the matplotlib figure instead of showing
    """
    V = np.linspace(V_range[0], V_range[1], 500)
    q = 1.6e-19        # charge of electron (C)
    k = 1.38e-23       # Boltzmann constant (J/K)
    VT = k * T / q     # Thermal voltage

    # Shockley diode equation
    I = Is * (np.exp(V / VT) - 1)

    # Plotting
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(V, I, label=f"T = {T} K", color='blue')
    ax.axhline(0, color='gray', linestyle='--')
    ax.axvline(0, color='gray', linestyle='--')
    ax.set_title("PN Junction Diode I-V Characteristics")
    ax.set_xlabel("Voltage (V)")
    ax.set_ylabel("Current (A)")
    ax.grid(True)
    ax.legend()
    fig.tight_layout()

    if return_fig:
        return fig
    else:
        plt.show()


