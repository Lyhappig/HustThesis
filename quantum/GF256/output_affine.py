import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister


def output_affine():
    a = QuantumRegister(8, 'a')
    qc = QuantumCircuit(a)

    # a[2] = a[2] ^ a[6]
    qc.cx(a[6], a[2])

    # a[4] = a[4] ^ a[7]
    qc.cx(a[7], a[4])       # y[0] = a[4]

    # a[3] = a[3] ^ a[4]
    qc.cx(a[4], a[3])

    # a[1] = a[1] ^ a[5]
    qc.cx(a[5], a[1])

    # a[2] = a[2] ^ a[3]
    qc.cx(a[3], a[2])       # y[6] = a[2]

    # a[5] = a[5] ^ a[2]
    qc.cx(a[2], a[5])

    # a[0] = a[0] ^ a[7]
    qc.cx(a[7], a[0])

    # a[7] = a[7] ^ a[5]
    qc.cx(a[5], a[7])       # y[3] = a[7]

    # a[0] = a[0] ^ a[3]
    qc.cx(a[3], a[0])

    # a[5] = a[5] ^ a[0]
    qc.cx(a[0], a[5])       # y[7] = a[5]

    # a[0] = a[0] ^ a[6]
    qc.cx(a[6], a[0])       # y[5] = a[0]

    # a[6] = a[6] ^ a[4]
    qc.cx(a[4], a[6])       # y[4] = a[6]

    # a[3] = a[3] ^ a[1]
    qc.cx(a[1], a[3])       # y[1] = a[3]

    # a[1] = a[1] ^ a[0]
    qc.cx(a[0], a[1])       # y[2] = a[1]

    qc.swap(a[4], a[0])
    qc.swap(a[4], a[5])
    qc.swap(a[4], a[7])
    qc.swap(a[4], a[3])
    qc.swap(a[4], a[1])
    qc.swap(a[4], a[2])
    qc.swap(a[4], a[6])

    qc.x(a[0])
    qc.x(a[1])
    qc.x(a[3])
    qc.x(a[6])
    qc.x(a[7])

    print(qc.depth())
    qc.draw(output="mpl")
    plt.show()


if __name__ == '__main__':
    output_affine()