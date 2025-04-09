# Nanomaterial bandgap module
# nano_materials.py
import numpy as np
import matplotlib.pyplot as plt

def simulate_nanobandgap(size_nm_range=(1, 10), Eg_bulk=1.1, alpha=1.5, return_fig=False):
    """
    Visualize quantum confinement effect on nanomaterial bandgap.

    Parameters:
    - size_nm_range: Tuple of min and max particle sizes in nm
    - Eg_bulk: Bulk band gap (e.g., Silicon ~1.1 eV)
    - alpha: Scaling factor for confinement effect
    """
    size = np.linspace(size_nm_range[0], size_nm_range[1], 200)
    Eg = Eg_bulk + alpha / (size ** 2)

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(size, Eg, color='purple')
    ax.set_title("Band Gap vs Nanoparticle Size")
    ax.set_xlabel("Size (nm)")
    ax.set_ylabel("Band Gap (eV)")
    ax.grid(True)
    ax.axhline(Eg_bulk, color='gray', linestyle='--', label='Bulk Band Gap')
    ax.legend()
    plt.tight_layout()
    if return_fig:
        return fig
    else:
        plt.show()

