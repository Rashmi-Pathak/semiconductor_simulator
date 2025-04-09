# jfet.py
import numpy as np
import matplotlib.pyplot as plt

def simulate_jfet(Vds_range=(0, 10), Vgs_values=[-1, -2, -3], Idss=10e-3, Vp=-4, return_fig=False):
    """
    Simulate and plot the I-V characteristics of a JFET.
    
    Parameters:
    - Vds_range: Tuple (start, end) for drain-source voltage
    - Vgs_values: List of gate-source voltages
    - Idss: Maximum drain current at Vgs=0 (in Amps)
    - Vp: Pinch-off voltage (in Volts)
    - return_fig: If True, return matplotlib figure instead of showing
    """
    Vds = np.linspace(Vds_range[0], Vds_range[1], 200)
    fig, ax = plt.subplots(figsize=(8, 5))

    for Vgs in Vgs_values:
        Id = []
        for vds in Vds:
            if Vgs <= Vp:
                Id.append(0)
            elif vds < (Vgs - Vp):
                id_val = Idss * (1 - Vgs / Vp) ** 2 * (vds / (Vgs - Vp))
                Id.append(id_val)
            else:
                id_val = Idss * (1 - Vgs / Vp) ** 2
                Id.append(id_val)
        ax.plot(Vds, Id, label=f"Vgs = {Vgs} V")

    ax.set_title("JFET Output Characteristics")
    ax.set_xlabel("Vds (V)")
    ax.set_ylabel("Id (A)")
    ax.grid(True)
    ax.axhline(0, color='gray', linestyle='--')
    ax.axvline(0, color='gray', linestyle='--')
    ax.legend()
    plt.tight_layout()
    if return_fig:
        return fig
    else:
        plt.show()

