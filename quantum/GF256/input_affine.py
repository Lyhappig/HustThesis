import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister


def input_affine():
    b = QuantumRegister(8, 'b')
    qc = QuantumCircuit(b)

    # b[7] = b[7] ^ b[6]
    qc.cx(b[6], b[7])

    # b[6] = b[6] ^ b[2]
    qc.cx(b[2], b[6])       # y[6] = b[6]

    # b[5] = b[5] ^ b[0]
    qc.cx(b[0], b[5])

    # b[0] = b[0] ^ b[7]
    qc.cx(b[7], b[0])

    # b[7] = b[7] ^ b[2]
    qc.cx(b[2], b[7])       # y[7] = b[7]

    # b[4] = b[4] ^ b[0]
    qc.cx(b[0], b[4])       # y[4] = b[4]

    # b[0] = b[0] ^ b[3]
    qc.cx(b[3], b[0])       # y[3] = b[0]

    # b[2] = b[2] ^ b[3]
    qc.cx(b[3], b[2])

    # b[3] = b[3] ^ b[5]
    qc.cx(b[5], b[3])       # y[5] = b[3]

    # b[2] = b[2] ^ b[4]
    qc.cx(b[4], b[2])       # y[2] = b[2]

    # b[1] = b[1] ^ b[2]
    qc.cx(b[2], b[1])       # y[1] = b[1]

    # b[5] = b[5] ^ b[1]
    qc.cx(b[1], b[5])       # y[0] = b[5]

    qc.swap(b[0], b[3])

    qc.swap(b[0], b[5])

    # y[0] = y[0] ^ 1
    qc.x(b[0])

    # y[2] = y[2] ^ 1
    qc.x(b[2])

    # y[4] = y[4] ^ 1
    qc.x(b[4])

    # y[6] = y[6] ^ 1
    qc.x(b[6])

    print(qc.depth())
    qc.draw(output="mpl")
    plt.show()


if __name__ == '__main__':
    input_affine()