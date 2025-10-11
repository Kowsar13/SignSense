import numpy as np
import matplotlib.pyplot as plt

# Define the constants
Is = 1e-9  # Reverse saturation current (A)
n = 1.5  # Ideality factor
Vt = 0.025  # Thermal voltage (V)
Rs = 0  # Series resistance (ohms)
Rsh = 100  # Shunt resistance (ohms)
Iph = 0.1  # Photocurrent (A)

# Define the voltage range
V = np.linspace(0, 1, 100)

# Calculate the current using the Shockley diode equation
I = Iph - Is * (np.exp(V / (n * Vt)) - 1) - V / Rs

# Calculate the maximum power point (MPP)
P = I * V
mpp_index = np.argmax(P)
V_mpp = V[mpp_index]
I_mpp = I[mpp_index]

# Plot the I-V curve
plt.plot(V, I)
plt.scatter(V_mpp, I_mpp, color='red', label='MPP')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlabel('Voltage (V)')
plt.ylabel('Current (A)')
plt.title('I-V Characteristics of a Single Junction Solar Cell')
plt.legend()
plt.grid(True)
plt.show()
