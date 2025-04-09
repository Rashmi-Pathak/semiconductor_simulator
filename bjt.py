# BJT module
# bjt.py
import numpy as np
import matplotlib.pyplot as plt

def simulate_bjt(Vce_range=(0, 5), beta=100, Ib_values=None, return_fig=False):
    """
    Simulate and plot output characteristics of a BJT in common emitter configuration.
    
    Parameters:
    - Vce_range: Tuple of (start, end) for collector-emitter voltage sweep
    - beta: Current gain (typically 100)
    - Ib_values: List of base currents in microamperes (uA)
    - return_fig: If True, returns the matplotlib figure
    """
    if Ib_values is None:
        Ib_values = [10, 20, 30, 40, 50]  # microamperes

    Vce = np.linspace(Vce_range[0], Vce_range[1], 200)

    fig, ax = plt.subplots(figsize=(8, 5))
    for Ib in Ib_values:
        Ib_A = Ib * 1e-6  # Convert uA to A
        Ic = beta * Ib_A
        Ic_curve = np.where(Vce < 0.2, 0, Ic)  # Basic cutoff at low Vce
        ax.plot(Vce, Ic_curve, label=f"Ib = {Ib} µA")

    ax.set_title("BJT Output Characteristics (Common Emitter)")
    ax.set_xlabel("Collector-Emitter Voltage Vce (V)")
    ax.set_ylabel("Collector Current Ic (A)")
    ax.grid(True)
    ax.legend()
    fig.tight_layout()

    if return_fig:
        return fig
    else:
        plt.show()

