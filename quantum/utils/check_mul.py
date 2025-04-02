from typing import List


def gf16_mul1(x, y) -> List[List[int]]:
    a = [0 for _ in range(4)]
    b = [0 for _ in range(4)]
    d = [0 for _ in range(4)]
    for i in range(4):
        a[i] = x[i]
        b[i] = y[i]

    def cx(p, q):
        return p ^ q

    def ccx(r, s, t):
        return (r & s) ^ t
    '''
    初始推导
    '''
    # # a2 = a0 + a2, b2 = b0 + b2
    # a[2] = a[0] ^ a[2]
    # b[2] = b[0] ^ b[2]
    #
    # # a3 = a1 + a3, b3 = b1 + b3
    # a[3] = a[1] ^ a[3]
    # b[3] = b[1] ^ b[3]
    #
    # # a1 = a0 + a1, b1 = b0 + b1
    # a[1] = a[0] ^ a[1]
    # b[1] = b[0] ^ b[1]
    #
    # # a3 = a2 + a3 = a3 + a2 + a1 + a0
    # a[3] = a[2] ^ a[3]
    #
    # # b3 = b2 + b3 = b3 + b2 + b1 + b0
    # b[3] = b[2] ^ b[3]
    #
    # # d3 = a3 * b3 + d3 = (a3 + a2 + a1 + a0) * (b3 + b2 + b1 + b0)
    # d[3] = d[3] ^ (a[3] & b[3])
    #
    # # d2 = a2 * b2 + d2 = (a2 + a0) * (b2 + b0)
    # d[2] = d[2] ^ (a[2] & b[2])
    #
    # # d1 = a1 * b1 + d1 = (a1 + a0) * (b1 + b0)
    # d[1] = d[1] ^ (a[1] & b[1])
    #
    # # d0 = a0 * b0 + d0 = a0 * b0
    # d[0] = d[0] ^ (a[0] & b[0])
    #
    # # a3 = a2 + a3 = a3 + a1
    # a[3] = a[2] ^ a[3]
    #
    # # b3 = b2 + b3 = b3 + b1
    # b[3] = b[2] ^ b[3]
    #
    # # a1 = a1, b1 = b1
    # a[1] = a[1] ^ a[0]
    # b[1] = b[1] ^ b[0]
    #
    # # a3 = a3, b3 = b3
    # a[3] = a[3] ^ a[1]
    # b[3] = b[3] ^ b[1]
    #
    # # a2 = a2, b2 = b2
    # a[2] = a[2] ^ a[0]
    # b[2] = b[2] ^ b[0]
    #
    # # d1 = d0 + d1 = (a1 + a0) * (b1 + b0) + a0 * b0
    # d[1] = d[1] ^ d[0]
    #
    # # d0 = a1 * b1 + d0 = a1 * b1 + a0 * b0
    # d[0] = d[0] ^ (a[1] & b[1])
    #
    # # d2 = d0 + d2 = (a2 + a0) * (b2 + b0) + a1 * b1 + a0 * b0
    # d[2] = d[2] ^ d[0]
    #
    # # d1 = d0 + d1 = (a1 + a0) * (b1 + b0) + a1 * b1
    # d[1] = d[1] ^ d[0]
    #
    # # d3 = d2 + d3 = ∑a * ∑b + (a2 + a0) * (b2 + b0) + a1 * b1 + a0 * b0
    # d[3] = d[3] ^ d[2]
    #
    # # d3 = d1 + d3 = ∑a * ∑b + (a2 + a0) * (b2 + b0) + (a1 + a0) * (b1 + b0) + a0 * b0
    # d[3] = d[3] ^ d[1]
    #
    # # a1 = a3 + a1, b1 = b3 + b1
    # a[1] = a[1] ^ a[3]
    # b[1] = b[1] ^ b[3]
    #
    # # a3 = a2 + a3, b3 = b2 + b3
    # a[3] = a[3] ^ a[2]
    # b[3] = b[3] ^ b[2]
    #
    # # d2 = a1 * b1 + d2 = (a3 + a1) * (b3 + b1) + (a2 + a0) * (b2 + b0) + a1 * b1 + a0 * b0
    # d[2] = d[2] ^ (a[1] & b[1])
    #
    # # d0 = a3 * b3 + d0 = (a3 + a2) * (b3 + b2) + a1 * b1 + a0 * b0
    # d[0] = d[0] ^ (a[3] & b[3])
    #
    # # a3 = a3, b3 = b3
    # a[3] = a[3] ^ a[2]
    # b[3] = b[3] ^ b[2]
    #
    # # a1 = a1, b1 = b1
    # a[1] = a[1] ^ a[3]
    # b[1] = b[1] ^ b[3]
    #
    # # d1 = d0 + d1 = (a3 + a2) * (b3 + b2) + (a1 + a0) * (b1 + b0) + a0 * b0
    # d[1] = d[1] ^ d[0]
    #
    # # d1 = a3 * b3 + d1 = (a3 + a2) * (b3 + b2) + a3 * b3 + (a1 + a0) * (b1 + b0) + a0 * b0
    # d[1] = d[1] ^ (a[3] & b[3])
    #
    # # d0 = a2 * b2 + d0 = (a3 + a2) * (b3 + b2) + a2 * b2 + a1 * b1 + a0 * b0
    # d[0] = d[0] ^ (a[2] & b[2])
    '''
    量子电路转化
    '''
    a[2] = cx(a[0], a[2])
    b[2] = cx(b[0], b[2])
    a[3] = cx(a[1], a[3])
    b[3] = cx(b[1], b[3])
    a[1] = cx(a[0], a[1])
    b[1] = cx(b[0], b[1])
    a[3] = cx(a[2], a[3])
    b[3] = cx(b[2], b[3])
    d[3] = ccx(a[3], b[3], d[3])
    d[2] = ccx(a[2], b[2], d[2])
    d[1] = ccx(a[1], b[1], d[1])
    d[0] = ccx(a[0], b[0], d[0])
    b[3] = cx(b[2], b[3])
    a[3] = cx(a[2], a[3])
    a[1] = cx(a[0], a[1])
    b[1] = cx(b[0], b[1])
    a[3] = cx(a[1], a[3])
    b[3] = cx(b[1], b[3])
    a[2] = cx(a[0], a[2])
    b[2] = cx(b[0], b[2])
    d[1] = cx(d[0], d[1])
    d[0] = ccx(a[1], b[1], d[0])
    d[2] = cx(d[0], d[2])
    d[1] = cx(d[0], d[1])
    d[3] = cx(d[2], d[3])
    d[3] = cx(d[1], d[3])
    a[1] = cx(a[3], a[1])
    b[1] = cx(b[3], b[1])
    a[3] = cx(a[2], a[3])
    b[3] = cx(b[2], b[3])
    d[2] = ccx(a[1], b[1], d[2])
    d[0] = ccx(a[3], b[3], d[0])
    a[3] = cx(a[2], a[3])
    b[3] = cx(b[2], b[3])
    a[1] = cx(a[3], a[1])
    b[1] = cx(b[3], b[1])
    d[1] = cx(d[0], d[1])
    d[1] = ccx(a[3], b[3], d[1])
    d[0] = ccx(a[2], b[2], d[0])
    '''
    存储比特反转：(3, 2, 1, 0) -> (0, 1, 2, 3)
    '''
    # a[1] = cx(a[3], a[1])
    # b[1] = cx(b[3], b[1])
    # a[0] = cx(a[2], a[0])
    # b[0] = cx(b[2], b[0])
    # a[2] = cx(a[3], a[2])
    # b[2] = cx(b[3], b[2])
    # a[0] = cx(a[1], a[0])
    # b[0] = cx(b[1], b[0])
    # d[0] = ccx(a[0], b[0], d[0])
    # d[1] = ccx(a[1], b[1], d[1])
    # d[2] = ccx(a[2], b[2], d[2])
    # d[3] = ccx(a[3], b[3], d[3])
    # b[0] = cx(b[1], b[0])
    # a[0] = cx(a[1], a[0])
    # a[2] = cx(a[3], a[2])
    # b[2] = cx(b[3], b[2])
    # a[0] = cx(a[2], a[0])
    # b[0] = cx(b[2], b[0])
    # a[1] = cx(a[3], a[1])
    # b[1] = cx(b[3], b[1])
    # d[2] = cx(d[3], d[2])
    # d[3] = ccx(a[2], b[2], d[3])
    # d[1] = cx(d[3], d[1])
    # d[2] = cx(d[3], d[2])
    # d[0] = cx(d[1], d[0])
    # d[0] = cx(d[2], d[0])
    # a[2] = cx(a[0], a[2])
    # b[2] = cx(b[0], b[2])
    # a[0] = cx(a[1], a[0])
    # b[0] = cx(b[1], b[0])
    # d[1] = ccx(a[2], b[2], d[1])
    # d[3] = ccx(a[0], b[0], d[3])
    # a[0] = cx(a[1], a[0])
    # b[0] = cx(b[1], b[0])
    # a[2] = cx(a[0], a[2])
    # b[2] = cx(b[0], b[2])
    # d[2] = cx(d[3], d[2])
    # d[2] = ccx(a[0], b[0], d[2])
    # d[3] = ccx(a[1], b[1], d[3])

    return [a, b, d]


'''
19辅助量子比特，14 Toffoli门，52个CNOT门，Toffoli深度为2
'''
def gf16_mul2(x, y) -> List[List[int]]:
    a = [0 for _ in range(4)]
    b = [0 for _ in range(4)]
    d = [0 for _ in range(19)]
    for i in range(4):
        a[i] = x[i]
        b[i] = y[i]

    def cx(x, y):
        return x ^ y

    def ccx(y, z, x):
        return x ^ y * z

    '''
    公式推导
    '''
    # d[4] = cx([a[3], a[2], a[1], a[0]], d[4])
    # d[5] = cx([b[3], b[2], b[1], b[0]], d[5])
    # d[6] = cx([a[2], a[0]], d[6])
    # d[7] = cx([b[2], b[0]], d[7])
    # d[8] = cx([a[1], a[0]], d[8])
    # d[9] = cx([b[1], b[0]], d[9])
    # d[10] = cx([a[3], a[1]], d[10])
    # d[11] = cx([b[3], b[1]], d[11])
    # d[12] = cx([a[3], a[2]], d[12])
    # d[13] = cx([b[3], b[2]], d[13])
    # d[3] = ccx(d[4], d[5], d[3])
    # d[2] = ccx(d[6], d[7], d[2])
    # d[1] = ccx(d[8], d[9], d[1])
    # d[0] = ccx(d[12], d[13], d[0])
    # d[14] = ccx(d[10], d[11], d[14])
    # d[15] = ccx(a[0], b[0], d[15])
    # d[16] = ccx(a[1], b[1], d[16])
    # d[17] = ccx(a[2], b[2], d[17])
    # d[18] = ccx(a[3], b[3], d[18])
    # d[3] = cx([d[2], d[1], d[15]], d[3])
    # d[2] = cx([d[14], d[15], d[16]], d[2])
    # d[1] = cx([d[0], d[15], d[18]], d[1])
    # d[0] = cx([d[15], d[16], d[17]], d[0])
    # d[18] = ccx(a[3], b[3], d[18])
    # d[17] = ccx(a[2], b[2], d[17])
    # d[16] = ccx(a[1], b[1], d[16])
    # d[15] = ccx(a[0], b[0], d[15])
    # d[14] = ccx(d[10], d[11], d[14])
    # d[13] = cx([b[3], b[2]], d[13])
    # d[12] = cx([a[3], a[2]], d[12])
    # d[11] = cx([b[3], b[1]], d[11])
    # d[10] = cx([a[3], a[1]], d[10])
    # d[9] = cx([b[1], b[0]], d[9])
    # d[8] = cx([a[1], a[0]], d[8])
    # d[7] = cx([b[2], b[0]], d[7])
    # d[6] = cx([a[2], a[0]], d[6])
    # d[5] = cx([b[3], b[2], b[1], b[0]], d[5])
    # d[4] = cx([a[3], a[2], a[1], a[0]], d[4])
    '''
    量子电路转化
    '''
    # d[6] = cx(a[2], d[6])
    # d[6] = cx(a[0], d[6])
    # d[7] = cx(b[2], d[7])
    # d[7] = cx(b[0], d[7])
    # d[8] = cx(a[1], d[8])
    # d[8] = cx(a[0], d[8])
    # d[9] = cx(b[1], d[9])
    # d[9] = cx(b[0], d[9])
    # d[10] = cx(a[3], d[10])
    # d[10] = cx(a[1], d[10])
    # d[11] = cx(b[3], d[11])
    # d[11] = cx(b[1], d[11])
    # d[4] = cx(d[10], d[4])
    # d[4] = cx(d[6], d[4])
    # d[5] = cx(d[11], d[5])
    # d[5] = cx(d[7], d[5])
    # d[12] = cx(a[3], d[12])
    # d[12] = cx(a[2], d[12])
    # d[13] = cx(b[3], d[13])
    # d[13] = cx(b[2], d[13])
    # d[3] = ccx(d[4], d[5], d[3])
    # d[2] = ccx(d[6], d[7], d[2])
    # d[1] = ccx(d[8], d[9], d[1])
    # d[0] = ccx(d[12], d[13], d[0])
    # d[14] = ccx(d[10], d[11], d[14])
    # d[15] = ccx(a[0], b[0], d[15])
    # d[16] = ccx(a[1], b[1], d[16])
    # d[17] = ccx(a[2], b[2], d[17])
    # d[18] = ccx(a[3], b[3], d[18])
    # d[3] = cx(d[2], d[3])
    # d[3] = cx(d[1], d[3])
    # d[3] = cx(d[15], d[3])
    # d[2] = cx(d[14], d[2])
    # d[2] = cx(d[15], d[2])
    # d[2] = cx(d[16], d[2])
    # d[1] = cx(d[0], d[1])
    # d[1] = cx(d[15], d[1])
    # d[1] = cx(d[18], d[1])
    # d[0] = cx(d[15], d[0])
    # d[0] = cx(d[16], d[0])
    # d[0] = cx(d[17], d[0])
    # d[18] = ccx(a[3], b[3], d[18])
    # d[17] = ccx(a[2], b[2], d[17])
    # d[16] = ccx(a[1], b[1], d[16])
    # d[15] = ccx(a[0], b[0], d[15])
    # d[14] = ccx(d[10], d[11], d[14])
    # d[13] = cx(b[3], d[13])
    # d[13] = cx(b[2], d[13])
    # d[12] = cx(a[3], d[12])
    # d[12] = cx(a[2], d[12])
    # d[5] = cx(d[11], d[5])
    # d[5] = cx(d[7], d[5])
    # d[4] = cx(d[10], d[4])
    # d[4] = cx(d[6], d[4])
    # d[11] = cx(b[3], d[11])
    # d[11] = cx(b[1], d[11])
    # d[10] = cx(a[3], d[10])
    # d[10] = cx(a[1], d[10])
    # d[9] = cx(b[1], d[9])
    # d[9] = cx(b[0], d[9])
    # d[8] = cx(a[1], d[8])
    # d[8] = cx(a[0], d[8])
    # d[7] = cx(b[2], d[7])
    # d[7] = cx(b[0], d[7])
    # d[6] = cx(a[2], d[6])
    # d[6] = cx(a[0], d[6])
    '''
    存储比特反转：(3, 2, 1, 0) -> (0, 1, 2, 3)
    '''
    d[6] = cx(a[1], d[6])
    d[6] = cx(a[3], d[6])
    d[7] = cx(b[1], d[7])
    d[7] = cx(b[3], d[7])
    d[8] = cx(a[2], d[8])
    d[8] = cx(a[3], d[8])
    d[9] = cx(b[2], d[9])
    d[9] = cx(b[3], d[9])
    d[10] = cx(a[0], d[10])
    d[10] = cx(a[2], d[10])
    d[11] = cx(b[0], d[11])
    d[11] = cx(b[2], d[11])
    d[4] = cx(d[10], d[4])
    d[4] = cx(d[6], d[4])
    d[5] = cx(d[11], d[5])
    d[5] = cx(d[7], d[5])
    d[12] = cx(a[0], d[12])
    d[12] = cx(a[1], d[12])
    d[13] = cx(b[0], d[13])
    d[13] = cx(b[1], d[13])
    d[0] = ccx(d[4], d[5], d[0])
    d[1] = ccx(d[6], d[7], d[1])
    d[2] = ccx(d[8], d[9], d[2])
    d[3] = ccx(d[12], d[13], d[3])
    d[14] = ccx(d[10], d[11], d[14])
    d[15] = ccx(a[3], b[3], d[15])
    d[16] = ccx(a[2], b[2], d[16])
    d[17] = ccx(a[1], b[1], d[17])
    d[18] = ccx(a[0], b[0], d[18])
    d[0] = cx(d[1], d[0])
    d[0] = cx(d[2], d[0])
    d[0] = cx(d[15], d[0])
    d[1] = cx(d[14], d[1])
    d[1] = cx(d[15], d[1])
    d[1] = cx(d[16], d[1])
    d[2] = cx(d[3], d[2])
    d[2] = cx(d[15], d[2])
    d[2] = cx(d[18], d[2])
    d[3] = cx(d[15], d[3])
    d[3] = cx(d[16], d[3])
    d[3] = cx(d[17], d[3])
    d[18] = ccx(a[0], b[0], d[18])
    d[17] = ccx(a[1], b[1], d[17])
    d[16] = ccx(a[2], b[2], d[16])
    d[15] = ccx(a[3], b[3], d[15])
    d[14] = ccx(d[10], d[11], d[14])
    d[13] = cx(b[0], d[13])
    d[13] = cx(b[1], d[13])
    d[12] = cx(a[0], d[12])
    d[12] = cx(a[1], d[12])
    d[5] = cx(d[11], d[5])
    d[5] = cx(d[7], d[5])
    d[4] = cx(d[10], d[4])
    d[4] = cx(d[6], d[4])
    d[11] = cx(b[0], d[11])
    d[11] = cx(b[2], d[11])
    d[10] = cx(a[0], d[10])
    d[10] = cx(a[2], d[10])
    d[9] = cx(b[2], d[9])
    d[9] = cx(b[3], d[9])
    d[8] = cx(a[2], d[8])
    d[8] = cx(a[3], d[8])
    d[7] = cx(b[1], d[7])
    d[7] = cx(b[3], d[7])
    d[6] = cx(a[1], d[6])
    d[6] = cx(a[3], d[6])
    return [a, b, d]


def gf16_mul2_inv(x, y, z) -> List[List[int]]:
    a = [0 for _ in range(4)]
    b = [0 for _ in range(4)]
    d = [0 for _ in range(19)]
    for i in range(4):
        a[i] = x[i]
        b[i] = y[i]
        d[i] = z[i]

    def cx(x, y):
        return x ^ y

    def ccx(y, z, x):
        return x ^ y * z

    d[6] = cx(a[3], d[6])
    d[6] = cx(a[1], d[6])
    d[7] = cx(b[3], d[7])
    d[7] = cx(b[1], d[7])
    d[8] = cx(a[3], d[8])
    d[8] = cx(a[2], d[8])
    d[9] = cx(b[3], d[9])
    d[9] = cx(b[2], d[9])
    d[10] = cx(a[2], d[10])
    d[10] = cx(a[0], d[10])
    d[11] = cx(b[2], d[11])
    d[11] = cx(b[0], d[11])
    d[4] = cx(d[6], d[4])
    d[4] = cx(d[10], d[4])
    d[5] = cx(d[7], d[5])
    d[5] = cx(d[11], d[5])
    d[12] = cx(a[1], d[12])
    d[12] = cx(a[0], d[12])
    d[13] = cx(b[1], d[13])
    d[13] = cx(b[0], d[13])
    d[14] = ccx(d[10], d[11], d[14])
    d[15] = ccx(a[3], b[3], d[15])
    d[16] = ccx(a[2], b[2], d[16])
    d[17] = ccx(a[1], b[1], d[17])
    d[18] = ccx(a[0], b[0], d[18])
    d[3] = cx(d[17], d[3])
    d[3] = cx(d[16], d[3])
    d[3] = cx(d[15], d[3])
    d[2] = cx(d[18], d[2])
    d[2] = cx(d[15], d[2])
    d[2] = cx(d[3], d[2])
    d[1] = cx(d[16], d[1])
    d[1] = cx(d[15], d[1])
    d[1] = cx(d[14], d[1])
    d[0] = cx(d[15], d[0])
    d[0] = cx(d[2], d[0])
    d[0] = cx(d[1], d[0])
    d[18] = ccx(a[0], b[0], d[18])
    d[17] = ccx(a[1], b[1], d[17])
    d[16] = ccx(a[2], b[2], d[16])
    d[15] = ccx(a[3], b[3], d[15])
    d[14] = ccx(d[10], d[11], d[14])
    d[3] = ccx(d[12], d[13], d[3])
    d[2] = ccx(d[8], d[9], d[2])
    d[1] = ccx(d[6], d[7], d[1])
    d[0] = ccx(d[4], d[5], d[0])
    d[13] = cx(b[1], d[13])
    d[13] = cx(b[0], d[13])
    d[12] = cx(a[1], d[12])
    d[12] = cx(a[0], d[12])
    d[5] = cx(d[7], d[5])
    d[5] = cx(d[11], d[5])
    d[4] = cx(d[6], d[4])
    d[4] = cx(d[10], d[4])
    d[11] = cx(b[2], d[11])
    d[11] = cx(b[0], d[11])
    d[10] = cx(a[2], d[10])
    d[10] = cx(a[0], d[10])
    d[9] = cx(b[3], d[9])
    d[9] = cx(b[2], d[9])
    d[8] = cx(a[3], d[8])
    d[8] = cx(a[2], d[8])
    d[7] = cx(b[3], d[7])
    d[7] = cx(b[1], d[7])
    d[6] = cx(a[3], d[6])
    d[6] = cx(a[1], d[6])
    return [a, b, d]


def qt9(x, y, z) -> List[List[int]]:
    a = [0 for _ in range(4)]
    b = [0 for _ in range(4)]
    d = [0 for _ in range(4)]
    for i in range(4):
        a[i] = x[i]
        b[i] = y[i]
        d[i] = z[i]

    def cx(p, q):
        return p ^ q

    def ccx(r, s, t):
        return (r & s) ^ t

    d[2] = cx(d[3], d[2])
    d[0] = cx(d[2], d[0])
    d[0] = cx(d[1], d[0])
    d[1] = cx(d[3], d[1])
    #
    a[1] = cx(a[3], a[1])
    b[1] = cx(b[3], b[1])
    a[0] = cx(a[2], a[0])
    b[0] = cx(b[2], b[0])
    a[2] = cx(a[3], a[2])
    b[2] = cx(b[3], b[2])
    a[0] = cx(a[1], a[0])
    b[0] = cx(b[1], b[0])
    d[0] = ccx(a[0], b[0], d[0])
    d[1] = ccx(a[1], b[1], d[1])
    d[2] = ccx(a[2], b[2], d[2])
    d[3] = ccx(a[3], b[3], d[3])
    b[0] = cx(b[1], b[0])
    a[0] = cx(a[1], a[0])
    a[2] = cx(a[3], a[2])
    b[2] = cx(b[3], b[2])
    a[0] = cx(a[2], a[0])
    b[0] = cx(b[2], b[0])
    a[1] = cx(a[3], a[1])
    b[1] = cx(b[3], b[1])
    d[2] = cx(d[3], d[2])
    d[3] = ccx(a[2], b[2], d[3])
    d[1] = cx(d[3], d[1])
    d[2] = cx(d[3], d[2])
    d[0] = cx(d[1], d[0])
    d[0] = cx(d[2], d[0])
    a[2] = cx(a[0], a[2])
    b[2] = cx(b[0], b[2])
    a[0] = cx(a[1], a[0])
    b[0] = cx(b[1], b[0])
    d[1] = ccx(a[2], b[2], d[1])
    d[3] = ccx(a[0], b[0], d[3])
    a[0] = cx(a[1], a[0])
    b[0] = cx(b[1], b[0])
    a[2] = cx(a[0], a[2])
    b[2] = cx(b[0], b[2])
    d[2] = cx(d[3], d[2])
    d[2] = ccx(a[0], b[0], d[2])
    d[3] = ccx(a[1], b[1], d[3])
    return [a, b, d]


def qt10(x, y, z) -> List[List[int]]:
    a = [0 for _ in range(4)]
    b = [0 for _ in range(4)]
    t = [0 for _ in range(4)]
    d = [0 for _ in range(15)]
    for i in range(4):
        a[i] = x[i]
        b[i] = y[i]
        t[i] = z[i]

    def cx(p, q):
        return p ^ q

    def ccx(p, q, r):
        return (p & q) ^ r

    t[2] = cx(t[3], t[2])
    t[0] = cx(t[2], t[0])
    t[0] = cx(t[1], t[0])
    # mul2
    d[2] = cx(a[1], d[2])
    d[2] = cx(a[3], d[2])
    d[3] = cx(b[1], d[3])
    d[3] = cx(b[3], d[3])
    d[4] = cx(a[2], d[4])
    d[4] = cx(a[3], d[4])
    d[5] = cx(b[2], d[5])
    d[5] = cx(b[3], d[5])
    d[6] = cx(a[0], d[6])
    d[6] = cx(a[2], d[6])
    d[7] = cx(b[0], d[7])
    d[7] = cx(b[2], d[7])
    d[0] = cx(d[6], d[0])
    d[0] = cx(d[2], d[0])
    d[1] = cx(d[7], d[1])
    d[1] = cx(d[3], d[1])
    d[8] = cx(a[0], d[8])
    d[8] = cx(a[1], d[8])
    d[9] = cx(b[0], d[9])
    d[9] = cx(b[1], d[9])
    t[0] = ccx(d[0], d[1], t[0])
    t[1] = ccx(d[2], d[3], t[1])
    t[2] = ccx(d[4], d[5], t[2])
    t[3] = ccx(d[8], d[9], t[3])
    d[10] = ccx(d[6], d[7], d[10])
    d[11] = ccx(a[3], b[3], d[11])
    d[12] = ccx(a[2], b[2], d[12])
    d[13] = ccx(a[1], b[1], d[13])
    d[14] = ccx(a[0], b[0], d[14])
    t[0] = cx(t[1], t[0])
    t[0] = cx(t[2], t[0])
    t[0] = cx(d[11], t[0])
    t[1] = cx(d[10], t[1])
    t[1] = cx(d[11], t[1])
    t[1] = cx(d[12], t[1])
    t[2] = cx(t[3], t[2])
    t[2] = cx(d[11], t[2])
    t[2] = cx(d[14], t[2])
    t[3] = cx(d[11], t[3])
    t[3] = cx(d[12], t[3])
    t[3] = cx(d[13], t[3])
    d[14] = ccx(a[0], b[0], d[14])
    d[13] = ccx(a[1], b[1], d[13])
    d[12] = ccx(a[2], b[2], d[12])
    d[11] = ccx(a[3], b[3], d[11])
    d[10] = ccx(d[6], d[7], d[10])
    d[9] = cx(b[0], d[9])
    d[9] = cx(b[1], d[9])
    d[8] = cx(a[0], d[8])
    d[8] = cx(a[1], d[8])
    d[1] = cx(d[7], d[1])
    d[1] = cx(d[3], d[1])
    d[0] = cx(d[6], d[0])
    d[0] = cx(d[2], d[0])
    d[7] = cx(b[0], d[7])
    d[7] = cx(b[2], d[7])
    d[6] = cx(a[0], d[6])
    d[6] = cx(a[2], d[6])
    d[5] = cx(b[2], d[5])
    d[5] = cx(b[3], d[5])
    d[4] = cx(a[2], d[4])
    d[4] = cx(a[3], d[4])
    d[3] = cx(b[1], d[3])
    d[3] = cx(b[3], d[3])
    d[2] = cx(a[1], d[2])
    d[2] = cx(a[3], d[2])

    return [a, b, d, t]


def check_mul1():
    for i in range(16):
        for j in range(16):
            a = [((i >> k) & 1) for k in range(4)]
            b = [((j >> k) & 1) for k in range(4)]
            ret = gf16_mul1(a, b)
            a1, b1, d1 = ret[0], ret[1], ret[2]

            for k in range(4):
                if a[k] != a1[k]:
                    print("check_mul1: a not match")
                    exit(0)
                if b[k] != b1[k]:
                    print("check_mul1: b not match")
                    exit(0)

            for k in range(len(d1)):
                if k >= 4 and d1[k] != 0:
                    print("check_mul1: can't recover auxiliary qubits")
                    exit(0)

            d2 = [0] * 4
            d2[3] = (a[3] ^ a[2] ^ a[1] ^ a[0]) * (b[3] ^ b[2] ^ b[1] ^ b[0]) ^ (a[2] ^ a[0]) * (b[2] ^ b[0]) ^ (
                        a[1] ^ a[0]) * (b[1] ^ b[0]) ^ a[0] * b[0]
            d2[2] = (a[3] ^ a[1]) * (b[3] ^ b[1]) ^ (a[2] ^ a[0]) * (b[2] ^ b[0]) ^ a[1] * b[1] ^ a[0] * b[0]
            d2[1] = (a[3] ^ a[2]) * (b[3] ^ b[2]) ^ a[3] * b[3] ^ (a[1] ^ a[0]) * (b[1] ^ b[0]) ^ a[0] * b[0]
            d2[0] = (a[3] ^ a[2]) * (b[3] ^ b[2]) ^ a[2] * b[2] ^ a[1] * b[1] ^ a[0] * b[0]

            # d2[0] = (a[0] ^ a[1] ^ a[2] ^ a[3]) * (b[0] ^ b[1] ^ b[2] ^ b[3]) ^ (a[1] ^ a[3]) * (b[1] ^ b[3]) ^ (
            #         a[2] ^ a[3]) * (b[2] ^ b[3]) ^ a[3] * b[3]
            # d2[1] = (a[0] ^ a[2]) * (b[0] ^ b[2]) ^ (a[1] ^ a[3]) * (b[1] ^ b[3]) ^ a[2] * b[2] ^ a[3] * b[3]
            # d2[2] = (a[0] ^ a[1]) * (b[0] ^ b[1]) ^ a[0] * b[0] ^ (a[2] ^ a[3]) * (b[2] ^ b[3]) ^ a[3] * b[3]
            # d2[3] = (a[0] ^ a[1]) * (b[0] ^ b[1]) ^ a[1] * b[1] ^ a[2] * b[2] ^ a[3] * b[3]

            for k in range(4):
                if d1[k] != d2[k]:
                    print("check_mul1: answer not match")
                    exit(0)

    print("OK")


def check_mul2():
    for i in range(16):
        for j in range(16):
            a = [0 for _ in range(4)]
            b = [0 for _ in range(4)]
            for k in range(4):
                a[k] = (i >> (3 - k)) & 1
                b[k] = (j >> (3 - k)) & 1
            ret = gf16_mul2(a, b)
            a1, b1, d1 = ret[0], ret[1], ret[2]

            for k in range(4):
                if a[k] != a1[k]:
                    print("check_mul2: a not match")
                    exit(0)
                if b[k] != b1[k]:
                    print("check_mul2: b not match")
                    exit(0)

            for k in range(len(d1)):
                if k >= 4 and d1[k] != 0:
                    print("check_mul2: can't recover auxiliary qubits")
                    exit(0)


            d2 = [0] * 4
            # d2[3] = (a[3] ^ a[2] ^ a[1] ^ a[0]) * (b[3] ^ b[2] ^ b[1] ^ b[0]) ^ (a[2] ^ a[0]) * (b[2] ^ b[0]) ^ (
            #         a[1] ^ a[0]) * (b[1] ^ b[0]) ^ a[0] * b[0]
            # d2[2] = (a[3] ^ a[1]) * (b[3] ^ b[1]) ^ (a[2] ^ a[0]) * (b[2] ^ b[0]) ^ a[1] * b[1] ^ a[0] * b[0]
            # d2[1] = (a[3] ^ a[2]) * (b[3] ^ b[2]) ^ a[3] * b[3] ^ (a[1] ^ a[0]) * (b[1] ^ b[0]) ^ a[0] * b[0]
            # d2[0] = (a[3] ^ a[2]) * (b[3] ^ b[2]) ^ a[2] * b[2] ^ a[1] * b[1] ^ a[0] * b[0]

            d2[0] = (a[0] ^ a[1] ^ a[2] ^ a[3]) * (b[0] ^ b[1] ^ b[2] ^ b[3]) ^ (a[1] ^ a[3]) * (b[1] ^ b[3]) ^ (
                    a[2] ^ a[3]) * (b[2] ^ b[3]) ^ a[3] * b[3]
            d2[1] = (a[0] ^ a[2]) * (b[0] ^ b[2]) ^ (a[1] ^ a[3]) * (b[1] ^ b[3]) ^ a[2] * b[2] ^ a[3] * b[3]
            d2[2] = (a[0] ^ a[1]) * (b[0] ^ b[1]) ^ a[0] * b[0] ^ (a[2] ^ a[3]) * (b[2] ^ b[3]) ^ a[3] * b[3]
            d2[3] = (a[0] ^ a[1]) * (b[0] ^ b[1]) ^ a[1] * b[1] ^ a[2] * b[2] ^ a[3] * b[3]

            for k in range(4):
                if d1[k] != d2[k]:
                    print("check_mul2: answer not match")
                    exit(0)

            res = gf16_mul2_inv(a, b, d1)
            a2, b2, d3 = res[0], res[1], res[2]

            for k in range(19):
                if k < 4 and a[k] != a2[k]:
                    print("gf16_mul2_inv: a not match")
                    exit(0)
                if k < 4 and b[k] != b2[k]:
                    print("gf16_mul2_inv: b not match")
                    exit(0)
                if d3[k] != 0:
                    print("gf16_mul2_inv: can't recover auxiliary qubits")
                    exit(0)

    print("OK")


def check_qt9(delta):
    for i in range(16):
        for j in range(16):
            a = [0 for _ in range(4)]
            b = [0 for _ in range(4)]
            c = [0 for _ in range(4)]
            for k in range(4):
                a[k] = (i >> (3 - k)) & 1
                b[k] = (j >> (3 - k)) & 1
                c[k] = (delta >> (3 - k)) & 1

            ret = qt9(a, b, c)
            a1, b1, d1 = ret[0], ret[1], ret[2]

            for k in range(4):
                if a[k] != a1[k]:
                    print("check_qt9: a not match")
                    return False
                if b[k] != b1[k]:
                    print("check_qt9: b not match")
                    return False

            for k in range(len(d1)):
                if k >= 4 and d1[k] != 0:
                    print("check_qt9: can't recover auxiliary qubits")
                    return False


            d2 = [0] * 4
            d2[0] = (a[0] ^ a[1] ^ a[2] ^ a[3]) * (b[0] ^ b[1] ^ b[2] ^ b[3]) ^ (a[1] ^ a[3]) * (b[1] ^ b[3]) ^ (
                    a[2] ^ a[3]) * (b[2] ^ b[3]) ^ a[3] * b[3]
            d2[1] = (a[0] ^ a[2]) * (b[0] ^ b[2]) ^ (a[1] ^ a[3]) * (b[1] ^ b[3]) ^ a[2] * b[2] ^ a[3] * b[3]
            d2[2] = (a[0] ^ a[1]) * (b[0] ^ b[1]) ^ a[0] * b[0] ^ (a[2] ^ a[3]) * (b[2] ^ b[3]) ^ a[3] * b[3]
            d2[3] = (a[0] ^ a[1]) * (b[0] ^ b[1]) ^ a[1] * b[1] ^ a[2] * b[2] ^ a[3] * b[3]

            ans, res = 0, 0
            for k in range(4):
                ans = (ans << 1) | d2[k]
                res = (res << 1) | d1[k]
            if res != (delta ^ ans):
                print(res, delta ^ ans)
                print("check_qt9: answer not match")
                return False
    return True


def check_qt10(delta):
    for i in range(16):
        for j in range(16):
            a = [0 for _ in range(4)]
            b = [0 for _ in range(4)]
            c = [0 for _ in range(4)]
            for k in range(4):
                a[k] = (i >> (3 - k)) & 1
                b[k] = (j >> (3 - k)) & 1
                c[k] = (delta >> (3 - k)) & 1

            ret = qt10(a, b, c)
            a1, b1, d1, t1 = ret[0], ret[1], ret[2], ret[3]

            for k in range(4):
                if a[k] != a1[k]:
                    print("check_qt10: a not match")
                    return False
                if b[k] != b1[k]:
                    print("check_qt10: b not match")
                    return False

            for k in range(len(d1)):
                if d1[k] != 0:
                    print("check_qt10: can't recover auxiliary qubits")
                    return False


            t2 = [0] * 4
            t2[0] = (a[0] ^ a[1] ^ a[2] ^ a[3]) * (b[0] ^ b[1] ^ b[2] ^ b[3]) ^ (a[1] ^ a[3]) * (b[1] ^ b[3]) ^ (
                    a[2] ^ a[3]) * (b[2] ^ b[3]) ^ a[3] * b[3]
            t2[1] = (a[0] ^ a[2]) * (b[0] ^ b[2]) ^ (a[1] ^ a[3]) * (b[1] ^ b[3]) ^ a[2] * b[2] ^ a[3] * b[3]
            t2[2] = (a[0] ^ a[1]) * (b[0] ^ b[1]) ^ a[0] * b[0] ^ (a[2] ^ a[3]) * (b[2] ^ b[3]) ^ a[3] * b[3]
            t2[3] = (a[0] ^ a[1]) * (b[0] ^ b[1]) ^ a[1] * b[1] ^ a[2] * b[2] ^ a[3] * b[3]

            ans, res = 0, 0
            for k in range(4):
                ans = (ans << 1) | t2[k]
                res = (res << 1) | t1[k]
            if res != (delta ^ ans):
                print(res, delta ^ ans)
                print("check_qt10: answer not match")
                return False
    return True


if __name__ == "__main__":
    check_mul1()

    check_mul2()

    for k in range(16):
        if not check_qt9(k):
            print("error")
            exit(-1)
    print("OK")

    for k in range(16):
        if not check_qt10(k):
            print("error")
            exit(-1)
    print("OK")
