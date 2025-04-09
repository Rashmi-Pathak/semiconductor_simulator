# Entry point to run the app
# main.py
from pn_junction import simulate_pn_junction
from bjt import simulate_bjt

# Simulate PN Junction
simulate_pn_junction(V_range=(-1, 1), T=300, Is=1e-12)

# Simulate BJT
simulate_bjt(Vce_range=(0, 5), beta=100, Ib_values=[10, 20, 30])


