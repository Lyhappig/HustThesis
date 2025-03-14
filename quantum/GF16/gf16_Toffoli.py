import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, QuantumRegister


def gf16_toffoli():
    d = QuantumRegister(4, 'd')
    qc = QuantumCircuit(d)

    qc.cx(d[0], d[1])
    qc.cx(d[0], d[2])
    qc.cx(d[1], d[3])

    # gf16_mul

    print(qc.depth())
    qc.draw(output="mpl")
    plt.show()


if __name__ == '__main__':
    gf16_toffoli()