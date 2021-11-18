import numpy as np
import matplotlib.pyplot as plt

from qiskit import QuantumCircuit

circ = QuantumCircuit(3)

# Hadamard gate on qubit 0
circ.h(0)

# CNOT gate between qubit 0 and 1
circ.cx(0,1)

# CNOT gate between quibit 0 and 1
circ.cx(0,2) 

circ.draw('mpl')

plt.show()
