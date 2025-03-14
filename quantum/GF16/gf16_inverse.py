import matplotlib.pyplot as plt
from qiskit import QuantumCircuit, QuantumRegister


'''
DORCIS，8 个 Toffoli 门，Toffoli 深度 8
'''
def gf16_inverse_DORCIS1():
    a = QuantumRegister(4, 'a')
    d = QuantumRegister(1, 'd')
    qc = QuantumCircuit(a, d)

    qc.ccx(a[3], a[1], a[2])
    qc.ccx(a[2], a[0], a[3])
    qc.cx(a[1], a[2])
    qc.cx(a[3], a[0])
    qc.cx(a[2], a[3])

    # qc.cccx(a[0], a[1], a[3], a[2])
    qc.ccx(a[0], a[1], d[0])
    qc.ccx(a[3], d[0], a[2])
    qc.ccx(a[0], a[1], d[0])
    qc.ccx(a[3], d[0], a[2])

    qc.ccx(a[3], a[2], a[1])
    qc.ccx(a[1], a[0], a[3])
    qc.cx(a[2], a[1])
    qc.cx(a[3], a[2])
    qc.cx(a[0], a[1])
    print(qc.depth())
    qc.draw(output="mpl")
    plt.show()


'''
DORCIS，使用 1 个辅助量子比特，7 个 Toffoli 门，Toffoli 深度 7
'''
def gf16_inverse_DORCIS2():
    a = QuantumRegister(4, 'a')
    d = QuantumRegister(1, 'd')
    qc = QuantumCircuit(a, d)

    qc.ccx(a[3], a[1], a[2])
    qc.ccx(a[2], a[0], a[3])
    qc.cx(a[1], a[2])
    qc.cx(a[3], a[0])
    qc.cx(a[2], a[3])

    # qc.cccx(a[0], a[1], a[3], a[2])
    qc.ccx(a[0], a[1], d[0])
    qc.ccx(a[3], d[0], a[2])
    qc.ccx(a[0], a[1], d[0])

    qc.ccx(a[3], a[2], a[1])
    qc.ccx(a[1], a[0], a[3])
    qc.cx(a[2], a[1])
    qc.cx(a[3], a[2])
    qc.cx(a[0], a[1])
    print(qc.depth())
    qc.draw(output="mpl")
    plt.show()


'''
DORCIS，使用 5 个辅助量子比特，5 个 Toffoli 门，Toffoli 深度 5
'''
def gf16_inverse_Stofflen():
    a = QuantumRegister(4, 'a')
    c = QuantumRegister(5, 'c')
    qc = QuantumCircuit(a, c)
    # part1
    qc.x(a[1])
    qc.cx(a[2], a[1])
    qc.ccx(a[0], a[1], c[0])
    qc.cx(a[2], a[1])
    qc.x(a[1])
    # part2
    qc.cx(a[1], c[4])
    qc.cx(a[2], c[4])
    qc.cx(a[2], c[3])
    qc.cx(a[3], c[3])
    qc.cx(a[1], a[2])
    qc.cx(a[3], a[2])
    qc.cx(c[0], a[2])
    qc.x(a[1])
    qc.cx(a[0], a[1])
    qc.cx(c[0], a[1])
    qc.ccx(a[1], a[2], c[1])
    qc.cx(c[3], a[1])
    qc.cx(c[1], a[1])
    qc.cx(c[1], c[4])
    qc.ccx(a[1], c[4], c[2])
    qc.cx(c[1], c[4])
    qc.cx(c[3], a[1])
    qc.cx(c[1], a[1])
    qc.cx(a[0], a[1])
    qc.cx(c[0], a[1])
    qc.x(a[1])
    qc.cx(a[1], a[2])
    qc.cx(a[3], a[2])
    qc.cx(c[0], a[2])
    qc.cx(a[2], c[3])
    qc.cx(a[3], c[3])
    qc.cx(a[1], c[4])
    qc.cx(a[2], c[4])
    # part3
    qc.cx(a[2], a[0])
    qc.cx(a[3], a[0])
    qc.cx(c[2], a[0])
    qc.cx(a[2], a[1])
    qc.cx(a[3], a[1])
    qc.cx(c[2], a[1])
    qc.ccx(a[0], a[1], c[3])
    qc.cx(a[2], a[1])
    qc.cx(a[3], a[1])
    qc.cx(c[2], a[1])
    qc.cx(a[2], a[0])
    qc.cx(a[3], a[0])
    qc.cx(c[2], a[0])
    # part4
    qc.cx(a[0], a[2])
    qc.cx(c[0], a[2])
    qc.cx(c[1], a[2])
    qc.cx(c[2], a[2])
    qc.cx(a[0], a[1])
    qc.cx(a[3], a[1])
    qc.cx(c[1], a[1])
    qc.ccx(a[1], a[2], c[4])
    qc.cx(a[0], a[1])
    qc.cx(a[3], a[1])
    qc.cx(c[1], a[1])
    qc.cx(a[0], a[2])
    qc.cx(c[0], a[2])
    qc.cx(c[1], a[2])
    qc.cx(c[2], a[2])
    # part5
    qc.cx(c[0], a[0])
    qc.cx(c[3], a[0])
    qc.cx(a[1], c[0])
    qc.cx(a[2], c[0])
    qc.cx(a[3], c[0])
    qc.cx(c[2], c[0])
    qc.cx(c[3], c[0])
    qc.cx(c[4], c[0])
    qc.cx(a[1], c[4])
    qc.cx(a[3], c[4])
    qc.cx(c[2], c[4])
    qc.cx(a[0], c[1])
    qc.cx(a[1], c[1])
    qc.cx(a[2], c[1])
    qc.cx(a[3], c[1])
    qc.cx(a[0], c[2])
    qc.cx(a[1], c[2])

    print(qc.depth())


'''
根据塔域直接构造求逆量子电路
15 个辅助量子比特，9个Toffoli门，29个CNOT门，Toffoli深度为2，电路深度18
'''
def gf16_inverse_tower_field():
    a = QuantumRegister(4, 'a')
    d = QuantumRegister(15, 'd')
    qc = QuantumCircuit(a, d)
    qc.cx(a[1], d[1])
    qc.cx(a[0], d[1])
    qc.cx(a[3], d[2])
    qc.cx(a[1], d[2])
    qc.cx(a[2], d[3])
    qc.cx(a[0], d[3])
    qc.cx(d[2], d[0])
    qc.cx(d[3], d[0])
    qc.ccx(d[0], d[1], d[4])
    qc.ccx(d[2], a[1], d[5])
    qc.ccx(d[3], a[0], d[6])
    qc.cx(d[4], d[6])
    qc.cx(a[2], d[6])
    qc.cx(d[4], d[5])
    qc.cx(a[2], d[5])
    qc.cx(a[3], d[5])
    qc.cx(a[3], d[2])
    qc.cx(a[1], d[2])
    qc.cx(d[6], d[2])
    qc.cx(a[2], d[3])
    qc.cx(a[0], d[3])
    qc.cx(d[5], d[3])
    qc.cx(d[0], d[1])
    qc.cx(a[3], a[1])
    qc.cx(a[2], a[0])
    qc.cx(d[6], d[7])
    qc.cx(d[5], d[7])
    qc.cx(d[7], d[8])
    qc.ccx(d[7], d[1], d[9])
    qc.ccx(d[6], a[3], d[10])
    qc.ccx(d[5], a[2], d[11])
    qc.ccx(d[8], d[0], d[12])
    qc.ccx(d[2], a[1], d[13])
    qc.ccx(d[3], a[0], d[14])
    qc.cx(d[11], d[9])
    qc.cx(d[11], d[10])
    qc.cx(d[14], d[12])
    qc.cx(d[14], d[13])

    print(qc.depth())


if __name__ == '__main__':
    gf16_inverse_Stofflen()