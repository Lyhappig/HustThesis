import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister


def gf16_n_square():
    a = QuantumRegister(4, 'a')
    c = ClassicalRegister(4, 'c')

    qc = QuantumCircuit(a, c)

    qc.cx(a[2], a[0])
    qc.cx(a[3], a[1])
    qc.cx(a[0], a[1])
    qc.swap(a[2], a[3])
    qc.swap(a[0], a[2])
    qc.swap(a[1], a[3])
    # [a3, a2, a0 + a2, a0 + a2 + a3 + a1]

    print(qc.depth())
    qc.draw(output="mpl")
    plt.show()


if __name__ == "__main__":
    gf16_n_square()