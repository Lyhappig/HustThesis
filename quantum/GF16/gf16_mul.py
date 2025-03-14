import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, QuantumRegister

'''
12 个量子比特，9 个 Toffoli 门，30 个 CNOT 门，Toffoli 深度是 5，电路深度 15
'''
def gf16_mul1():
    a = QuantumRegister(4, 'a')
    b = QuantumRegister(4, 'b')
    d = QuantumRegister(4, 'd')
    qc = QuantumCircuit(a, b, d)

    # a2 = a0 + a2, b2 = b0 + b2
    qc.cx(a[0], a[2])
    qc.cx(b[0], b[2])

    # a3 = a1 + a3, b3 = b1 + b3
    qc.cx(a[1], a[3])
    qc.cx(b[1], b[3])

    # a3 = a2 + a3 = a3 + a2 + a1 + a0
    qc.cx(a[2], a[3])

    # b3 = b2 + b3 = b3 + b2 + b1 + b0
    qc.cx(b[2], b[3])

    # d3 = a3 * b3 + d3 = (a3 + a2 + a1 + a0) * (b3 + b2 + b1 + b0)
    qc.ccx(a[3], b[3], d[3])

    # d2 = a2 * b2 + d2 = (a2 + a0) * (b2 + b0)
    qc.ccx(a[2], b[2], d[2])

    # a3 = a2 + a3 = a3 + a1
    qc.cx(a[2], a[3])

    # b3 = b2 + b3 = b3 + b1
    qc.cx(b[2], b[3])

    # a3 = a3, b3 = b3
    qc.cx(a[1], a[3])
    qc.cx(b[1], b[3])

    # a2 = a2, b2 = b2
    qc.cx(a[0], a[2])
    qc.cx(b[0], b[2])

    # a1 = a0 + a1, b1 = b0 + b1
    qc.cx(a[0], a[1])
    qc.cx(b[0], b[1])

    # d1 = a1 * b1 + d1 = (a1 + a0) * (b1 + b0)
    qc.ccx(a[1], b[1], d[1])

    # d0 = a0 * b0 + d0 = a0 * b0
    qc.ccx(a[0], b[0], d[0])

    # a1 = a1, b1 = b1
    qc.cx(a[0], a[1])
    qc.cx(b[0], b[1])

    # d1 = d0 + d1 = (a1 + a0) * (b1 + b0) + a0 * b0
    qc.cx(d[0], d[1])

    # d0 = a1 * b1 + d0 = a1 * b1 + a0 * b0
    qc.ccx(a[1], b[1], d[0])

    # d2 = d0 + d2 = (a2 + a0) * (b2 + b0) + a1 * b1 + a0 * b0
    qc.cx(d[0], d[2])

    # d1 = d0 + d1 = (a1 + a0) * (b1 + b0) + a1 * b1
    qc.cx(d[0], d[1])

    # d3 = d2 + d3 = ∑a * ∑b + (a2 + a0) * (b2 + b0) + a1 * b1 + a0 * b0
    qc.cx(d[2], d[3])

    # d3 = d1 + d3 = ∑a * ∑b + (a2 + a0) * (b2 + b0) + (a1 + a0) * (b1 + b0) + a0 * b0
    qc.cx(d[1], d[3])

    # a1 = a3 + a1, b1 = b3 + b1
    qc.cx(a[3], a[1])
    qc.cx(b[3], b[1])

    # a3 = a2 + a3, b3 = b2 + b3
    qc.cx(a[2], a[3])
    qc.cx(b[2], b[3])

    # d2 = a1 * b1 + d2 = (a3 + a1) * (b3 + b1) + (a2 + a0) * (b2 + b0) + a1 * b1 + a0 * b0
    qc.ccx(a[1], b[1], d[2])

    # d0 = a3 * b3 + d0 = (a3 + a2) * (b3 + b2) + a1 * b1 + a0 * b0
    qc.ccx(a[3], b[3], d[0])

    # a1 = a1, b1 = b1
    qc.cx(a[3], a[1])
    qc.cx(b[3], b[1])

    # a3 = a3, b3 = b3
    qc.cx(a[2], a[3])
    qc.cx(b[2], b[3])

    # d1 = d0 + d1 = (a3 + a2) * (b3 + b2) + (a1 + a0) * (b1 + b0) + a0 * b0
    qc.cx(d[0], d[1])

    # d1 = a3 * b3 + d1 = (a3 + a2) * (b3 + b2) + a3 * b3 + (a1 + a0) * (b1 + b0) + a0 * b0
    qc.ccx(a[3], b[3], d[1])

    # d0 = a2 * b2 + d0 = (a3 + a2) * (b3 + b2) + a2 * b2 + a1 * b1 + a0 * b0
    qc.ccx(a[2], b[2], d[0])
    print(qc.depth())
    qc.draw(output="mpl")
    plt.show()


'''
12 个量子比特，9 个 Toffoli 门，30 个 CNOT 门，Toffoli 深度是 4，电路深度 12
'''
def gf16_mul2():
    a = QuantumRegister(4, 'a')
    b = QuantumRegister(4, 'b')
    d = QuantumRegister(4, 'd')

    qc = QuantumCircuit(a, b, d)

    # a2 = a0 + a2, b2 = b0 + b2
    qc.cx(a[0], a[2])
    qc.cx(b[0], b[2])

    # a3 = a1 + a3, b3 = b1 + b3
    qc.cx(a[1], a[3])
    qc.cx(b[1], b[3])

    # a1 = a0 + a1, b1 = b0 + b1
    qc.cx(a[0], a[1])
    qc.cx(b[0], b[1])

    # a3 = a2 + a3 = a3 + a2 + a1 + a0
    qc.cx(a[2], a[3])

    # b3 = b2 + b3 = b3 + b2 + b1 + b0
    qc.cx(b[2], b[3])

    # d3 = a3 * b3 + d3 = (a3 + a2 + a1 + a0) * (b3 + b2 + b1 + b0)
    qc.ccx(a[3], b[3], d[3])

    # d2 = a2 * b2 + d2 = (a2 + a0) * (b2 + b0)
    qc.ccx(a[2], b[2], d[2])

    # d1 = a1 * b1 + d1 = (a1 + a0) * (b1 + b0)
    qc.ccx(a[1], b[1], d[1])

    # d0 = a0 * b0 + d0 = a0 * b0
    qc.ccx(a[0], b[0], d[0])

    # b3 = b2 + b3 = b3 + b1
    qc.cx(b[2], b[3])

    # a3 = a2 + a3 = a3 + a1
    qc.cx(a[2], a[3])

    # a1 = a1, b1 = b1
    qc.cx(a[0], a[1])
    qc.cx(b[0], b[1])

    # a3 = a3, b3 = b3
    qc.cx(a[1], a[3])
    qc.cx(b[1], b[3])

    # a2 = a2, b2 = b2
    qc.cx(a[0], a[2])
    qc.cx(b[0], b[2])

    # d1 = d0 + d1 = (a1 + a0) * (b1 + b0) + a0 * b0
    qc.cx(d[0], d[1])

    # d0 = a1 * b1 + d0 = a1 * b1 + a0 * b0
    qc.ccx(a[1], b[1], d[0])

    # d2 = d0 + d2 = (a2 + a0) * (b2 + b0) + a1 * b1 + a0 * b0
    qc.cx(d[0], d[2])

    # d1 = d0 + d1 = (a1 + a0) * (b1 + b0) + a1 * b1
    qc.cx(d[0], d[1])

    # d3 = d2 + d3 = ∑a * ∑b + (a2 + a0) * (b2 + b0) + a1 * b1 + a0 * b0
    qc.cx(d[2], d[3])

    # d3 = d1 + d3 = ∑a * ∑b + (a2 + a0) * (b2 + b0) + (a1 + a0) * (b1 + b0) + a0 * b0
    qc.cx(d[1], d[3])

    # a1 = a3 + a1, b1 = b3 + b1
    qc.cx(a[3], a[1])
    qc.cx(b[3], b[1])

    # a3 = a2 + a3, b3 = b2 + b3
    qc.cx(a[2], a[3])
    qc.cx(b[2], b[3])

    # d2 = a1 * b1 + d2 = (a3 + a1) * (b3 + b1) + (a2 + a0) * (b2 + b0) + a1 * b1 + a0 * b0
    qc.ccx(a[1], b[1], d[2])

    # d0 = a3 * b3 + d0 = (a3 + a2) * (b3 + b2) + a1 * b1 + a0 * b0
    qc.ccx(a[3], b[3], d[0])

    # a1 = a1, b1 = b1
    qc.cx(a[3], a[1])
    qc.cx(b[3], b[1])

    # a3 = a3, b3 = b3
    qc.cx(a[2], a[3])
    qc.cx(b[2], b[3])

    # d1 = d0 + d1 = (a3 + a2) * (b3 + b2) + (a1 + a0) * (b1 + b0) + a0 * b0
    qc.cx(d[0], d[1])

    # d1 = a3 * b3 + d1 = (a3 + a2) * (b3 + b2) + a3 * b3 + (a1 + a0) * (b1 + b0) + a0 * b0
    qc.ccx(a[3], b[3], d[1])

    # d0 = a2 * b2 + d0 = (a3 + a2) * (b3 + b2) + a2 * b2 + a1 * b1 + a0 * b0
    qc.ccx(a[2], b[2], d[0])

    print(qc.depth())
    qc.draw(output="mpl")
    plt.show()


'''
根据塔域结构构建的量子电路
19辅助量子比特，14 Toffoli门，52个CNOT门，Toffoli深度为2，电路深度18
'''
def gf16_mul3():
    a = QuantumRegister(4, 'a')
    b = QuantumRegister(4, 'b')
    d = QuantumRegister(19, 'd')
    qc = QuantumCircuit(a, b, d)

    qc.cx(a[2], d[6])
    qc.cx(a[0], d[6])
    qc.cx(b[2], d[7])
    qc.cx(b[0], d[7])
    qc.cx(a[1], d[8])
    qc.cx(a[0], d[8])
    qc.cx(b[1], d[9])
    qc.cx(b[0], d[9])
    qc.cx(a[3], d[10])
    qc.cx(a[1], d[10])
    qc.cx(b[3], d[11])
    qc.cx(b[1], d[11])
    qc.cx(d[10], d[4])
    qc.cx(d[6], d[4])
    qc.cx(d[11], d[5])
    qc.cx(d[7], d[5])
    qc.cx(a[3], d[12])
    qc.cx(a[2], d[12])
    qc.cx(b[3], d[13])
    qc.cx(b[2], d[13])
    qc.ccx(d[4], d[5], d[3])
    qc.ccx(d[6], d[7], d[2])
    qc.ccx(d[8], d[9], d[1])
    qc.ccx(d[12], d[13], d[0])
    qc.ccx(d[10], d[11], d[14])
    qc.ccx(a[0], b[0], d[15])
    qc.ccx(a[1], b[1], d[16])
    qc.ccx(a[2], b[2], d[17])
    qc.ccx(a[3], b[3], d[18])
    qc.cx(d[2], d[3])
    qc.cx(d[1], d[3])
    qc.cx(d[15], d[3])
    qc.cx(d[14], d[2])
    qc.cx(d[15], d[2])
    qc.cx(d[16], d[2])
    qc.cx(d[0], d[1])
    qc.cx(d[15], d[1])
    qc.cx(d[18], d[1])
    qc.cx(d[15], d[0])
    qc.cx(d[16], d[0])
    qc.cx(d[17], d[0])
    qc.ccx(a[3], b[3], d[18])
    qc.ccx(a[2], b[2], d[17])
    qc.ccx(a[1], b[1], d[16])
    qc.ccx(a[0], b[0], d[15])
    qc.ccx(d[10], d[11], d[14])
    qc.cx(b[3], d[13])
    qc.cx(b[2], d[13])
    qc.cx(a[3], d[12])
    qc.cx(a[2], d[12])
    qc.cx(d[11], d[5])
    qc.cx(d[7], d[5])
    qc.cx(d[10], d[4])
    qc.cx(d[6], d[4])
    qc.cx(b[3], d[11])
    qc.cx(b[1], d[11])
    qc.cx(a[3], d[10])
    qc.cx(a[1], d[10])
    qc.cx(b[1], d[9])
    qc.cx(b[0], d[9])
    qc.cx(a[1], d[8])
    qc.cx(a[0], d[8])
    qc.cx(b[2], d[7])
    qc.cx(b[0], d[7])
    qc.cx(a[2], d[6])
    qc.cx(a[0], d[6])

    print(qc.depth())


if __name__ == "__main__":
    gf16_mul3()
