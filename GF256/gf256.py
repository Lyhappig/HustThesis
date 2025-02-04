import os
import sys

from MyThesis.utils.matrix import GF2Matrix

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from GF16.gf16 import *
from utils.util import *
from utils.matrix import *


def G256_inv1(x: int):
    '''
    GF(2^8)的求逆操作
    '''
    alpha1 = (x & 0xF0) >> 4
    alpha0 = x & 0x0F

    theta1 = G16_square_mul_n(alpha1)
    theta2 = alpha1 ^ alpha0
    theta3 = G16_mul(theta2, alpha0)
    theta4 = G16_inv(theta1 ^ theta3)

    gamma1 = G16_mul(theta4, alpha1)
    gamma0 = G16_mul(theta4, theta2)
    return get_num([gamma1, gamma0], 4)


# (x7, x6, x5, x4, x3, x2, x1, x0) -> (t1, t2, t3, t4)
def get_data1(x: int):
    '''
    input: (x7, x6, x5, x4, x3, x2, x1, x0)
    '''
    # alpha
    x7, x6, x5, x4 = get_bit(x, 7), get_bit(x, 6), get_bit(x, 5), get_bit(x, 4)
    # beta
    x3, x2, x1, x0 = get_bit(x, 3), get_bit(x, 2), get_bit(x, 1), get_bit(x, 0)

    # alpha + beta
    p1 = x7 ^ x3
    p2 = x6 ^ x2
    p3 = x5 ^ x1
    p4 = x4 ^ x0

    # begin: (alpha + beta) * beta
    p5 = p1 ^ p3
    p6 = p2 ^ p4
    p7 = x3 ^ x1
    p8 = x2 ^ x0

    # (A1 + A0) * (B1 + B0)
    p9 = p5 ^ p6
    p10 = p7 ^ p8
    q1 = p9 * p10
    q2 = p5 * p7
    q3 = p6 * p8
    r1 = q1 ^ q3
    r2 = q2 ^ q3

    # W * A1 * B1
    p11 = p1 ^ p2
    p12 = x3 ^ x2
    q4 = p11 * p12
    q5 = p1 * x3
    q6 = p2 * x2
    r3 = q4 ^ q5
    r4 = q4 ^ q6

    # A0 * B0
    p13 = p3 ^ p4
    p14 = x1 ^ x0
    q7 = p13 * p14
    q8 = p3 * x1
    q9 = p4 * x0
    r5 = q7 ^ q9
    r6 = q8 ^ q9

    # end: (alpha + beta) * beta
    s1 = r1 ^ r5
    s2 = r2 ^ r6
    s3 = r3 ^ r5
    s4 = r4 ^ r6

    # begin: n * alpha^2
    p15 = x7 ^ x5
    p16 = x6 ^ x4
    p17 = p15 ^ p16

    # end: n * alpha^2
    s5 = x4
    s6 = x5
    s7 = p15
    s8 = p17

    '''
    output: (t1, t2, t3, t4)
    '''
    t1 = s5 ^ s1
    t2 = s6 ^ s2
    t3 = s7 ^ s3
    t4 = s8 ^ s4

    return get_num([t1, t2, t3, t4], 1)


Affine1 = GF2Matrix([
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1]
])


def get_data2(x: int):
    '''
    input: (x7, x6, x5, x4, x3, x2, x1, x0)
    '''
    # alpha
    x7, x6, x5, x4 = get_bit(x, 7), get_bit(x, 6), get_bit(x, 5), get_bit(x, 4)
    # beta
    x3, x2, x1, x0 = get_bit(x, 3), get_bit(x, 2), get_bit(x, 1), get_bit(x, 0)

    input = GF2Matrix(get_bit_list(x))
    input.T()
    out = (Affine1 * input).matrix
    p1, p2, p3, p4, p5, p6, p7, p8, p9 = out[0][0], out[1][0], out[2][0], out[3][0], out[4][0], out[5][0], out[6][0], \
    out[7][0], out[8][0]
    p10, p11, p12, p13, p14, p15, p16, p17, p18 = out[9][0], out[10][0], out[11][0], out[12][0], out[13][0], out[14][0], \
    out[15][0], out[16][0], out[17][0]

    q1 = p1 * p2
    q2 = p3 * p4
    q3 = p5 * p6
    r1 = q1 ^ q3
    r2 = q2 ^ q3

    q4 = p7 * p8
    q5 = p9 * p10
    q6 = p11 * p12
    r3 = q4 ^ q5
    r4 = q4 ^ q6

    q7 = p13 * p14
    q8 = p15 * p16
    q9 = p17 * p18
    r5 = q7 ^ q9
    r6 = q8 ^ q9

    s1 = r1 ^ r5
    s2 = r2 ^ r6
    s3 = r3 ^ r5
    s4 = r4 ^ r6

    r7 = x7 ^ x5
    r8 = x6 ^ x4
    r9 = r7 ^ r8

    s5 = x4
    s6 = x5
    s7 = r7
    s8 = r9

    t1 = s5 ^ s1
    t2 = s6 ^ s2
    t3 = s7 ^ s3
    t4 = s8 ^ s4
    return get_num([t1, t2, t3, t4], 1)


def G256_inv2(x: int):
    '''
    GF(2^8)的求逆操作
    '''
    alpha = (x & 0xF0) >> 4
    beta = x & 0x0F
    # 代数表达式
    # inverse = G16_inv_box(get_data1(x))
    # 提取 AND 之前的 18* 8 矩阵
    inverse = G16_inv_box(get_data2(x))
    gamma1 = G16_mul(inverse, alpha)
    gamma0 = G16_mul(inverse, alpha ^ beta)
    return get_num([gamma1, gamma0], 4)


M = GF2Matrix([
    [1, 1, 0, 1, 0, 0, 1, 1],
    [1, 1, 1, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 1, 1, 0],
    [0, 1, 0, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 1, 1, 1]
])

P2T = GF2Matrix([
    [0, 1, 0, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 1, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [1, 0, 0, 1, 1, 0, 0, 0],
    [1, 1, 1, 0, 1, 1, 1, 0],
    [1, 0, 1, 0, 1, 1, 0, 1]
])

T2P = GF2Matrix([
    [0, 1, 1, 1, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 1, 0],
    [1, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 1, 1, 0],
    [0, 0, 1, 1, 0, 1, 1, 0],
    [1, 0, 1, 0, 1, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 1]
])

Affine2 = GF2Matrix([
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 0],   # x4
    [0, 0, 1, 0, 0, 0, 0, 0],   # x5
    [1, 0, 1, 0, 0, 0, 0, 0],   # x7 + x5
    [1, 1, 1, 1, 0, 0, 0, 0]    # x7 + x6 + x5 + x4
])

alpha, sum_ab = 0, 0

# 22 * 8 Matrix
def get_inv_input1(x: int):
    global alpha, sum_ab

    input = GF2Matrix(get_bit_list(x))
    input.T()
    Mt = Affine2 * P2T * M
    out = (Mt * input).matrix

    # Affine2 * P2T * C = [[0 0 0 0 0 0 0 1 0 1 0 0 0 1 0 1 0 0 0 1 0 0]]
    # p8, p10, p14, p16, s6: XOR 1
    p1, p2, p3, p4, p5, p6, p7, p8, p9 = out[0][0], out[1][0], out[2][0], out[3][0], out[4][0], out[5][0], out[6][0], \
        out[7][0] ^ 1, out[8][0]
    p10, p11, p12, p13, p14, p15, p16, p17, p18 = out[9][0] ^ 1, out[10][0], out[11][0], out[12][0], out[13][0] ^ 1, out[14][0], \
        out[15][0] ^ 1, out[16][0], out[17][0]
    s5, s6, s7, s8 = out[18][0], out[19][0] ^ 1, out[20][0], out[21][0]

    alpha = get_num([s6 ^ s7, p11 ^ p12, s6, s5], 1)
    sum_ab = get_num([p9, p11, p15, p17], 1)

    q1 = p1 * p2
    q2 = p3 * p4
    q3 = p5 * p6
    r1 = q1 ^ q3
    r2 = q2 ^ q3

    q4 = p7 * p8
    q5 = p9 * p10
    q6 = p11 * p12
    r3 = q4 ^ q5
    r4 = q4 ^ q6

    q7 = p13 * p14
    q8 = p15 * p16
    q9 = p17 * p18
    r5 = q7 ^ q9
    r6 = q8 ^ q9

    s1 = r1 ^ r5
    s2 = r2 ^ r6
    s3 = r3 ^ r5
    s4 = r4 ^ r6

    t1 = s5 ^ s1
    t2 = s6 ^ s2
    t3 = s7 ^ s3
    t4 = s8 ^ s4
    return get_num([t1, t2, t3, t4], 1)


Affine3 = GF2Matrix([
    [1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 1, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 0, 0, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0],
    [1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 1, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0],   # p19 = x7
    [0, 1, 0, 0, 0, 0, 0, 0],   # p20 = x6
    [0, 0, 0, 1, 0, 0, 0, 0],   # s1 = x4
    [0, 0, 1, 0, 0, 0, 0, 0],   # s2 = x5
    [1, 0, 1, 0, 0, 0, 0, 0],   # s3 = x7 + x5
    [1, 1, 1, 1, 0, 0, 0, 0]    # s4 = x7 + x6 + x5 + x4
])

p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11 = [0] * 12
p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23 = [0] * 12
z0, z1, z2, z3 = [0] * 4

def get_inv_input2(x: int):
    global alpha, sum_ab
    global p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11
    global p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23

    # input = GF2Matrix(get_bit_list(x))
    # input.T()
    # Mt = Affine3 * P2T * M
    # out = (Mt * input).matrix
    # Affine3 * P2T * C: (8, 10, 14, 16, 19, 22) XOR 1
    # p1, p2, p3, p4, p5, p6, p7, p8, p9 = out[0][0], out[1][0], out[2][0], out[3][0], out[4][0], out[5][0], out[6][0], \
    #     out[7][0] ^ 1, out[8][0]
    # p10, p11, p12, p13, p14, p15, p16, p17, p18 = out[9][0] ^ 1, out[10][0], out[11][0], out[12][0], out[13][0] ^ 1, out[14][0], \
    #     out[15][0] ^ 1, out[16][0], out[17][0]
    #
    # p19,  p20 = out[18][0] ^ 1, out[19][0]
    # s5, s6, s7, s8 = out[20][0], out[21][0] ^ 1, out[22][0], out[23][0]

    x0, x1, x2, x3 = get_bit(x, 7), get_bit(x, 6), get_bit(x, 5), get_bit(x, 4)
    x4, x5, x6, x7 = get_bit(x, 3), get_bit(x, 2), get_bit(x, 1), get_bit(x, 0)

    p13 = x7
    p15 = x2 ^ x6
    p17 = x7 ^ p15
    k1 = x0 ^ x3
    p0 = p15 ^ k1
    p11 = x5 ^ k1
    p5 = p17 ^ p11
    p16 = x6 ^ p0
    p20 = p17 ^ p16
    p6 = x4 ^ p20
    p9 = x3 ^ p6
    p3 = p15 ^ p9
    p1 = p5 ^ p3
    p7 = p11 ^ p9
    p12 = p0 ^ p6
    p14 = p16 ^ p12
    p21 = p15 ^ p14
    p19 = x1 ^ p21
    p10 = p11 ^ p19
    p2 = x6 ^ p10
    p4 = p16 ^ p10
    p8 = p14 ^ p2
    p18 = p9 ^ p8
    p22 = p21 ^ p18
    p23 = p0 ^ p1

    # Affine3 * P2T * C: (8, 10, 14, 16, 19, 22) XOR 1
    p7 ^= 1
    p9 ^= 1
    p13 ^= 1
    p15 ^= 1
    p18 ^= 1
    p21 ^= 1

    alpha = get_num([p18, p19, p21, p20], 1)
    sum_ab = get_num([p8, p10, p14, p16], 1)

    q0 = p0 * p1
    q1 = p2 * p3
    q2 = p4 * p5
    r0 = q0 ^ q2
    r1 = q1 ^ q2

    q3 = p6 * p7
    q4 = p8 * p9
    q5 = p10 * p11
    r2 = q3 ^ q4
    r3 = q3 ^ q5

    q6 = p12 * p13
    q7 = p14 * p15
    q8 = p16 * p17
    r4 = q6 ^ q8
    r5 = q7 ^ q8

    s0 = r0 ^ r4
    s1 = r1 ^ r5
    s2 = r2 ^ r4
    s3 = r3 ^ r5

    t0 = p20 ^ s0
    t1 = p21 ^ s1
    t2 = p22 ^ s2
    t3 = p23 ^ s3
    return get_num([t0, t1, t2, t3], 1)


def get_mul1():
    # x7 x6 x5 x4
    # p18, p19, p21, p20
    # y3 y2 y1 y0
    # z0, z1, z2, z3

    # y3 + y1
    k0 = z0 ^ z2
    # y2 + y0
    k1 = z1 ^ z3
    # y3 + y2
    k2 = z0 ^ z1
    # y1 + y0
    k3 = z2 ^ z3
    # (y3 + y1) + (y2 + y0)
    k4 = k0 ^ k1

    # G1
    v0 = (p23 * k4) ^ ((p19 ^ p20) * k1)
    v1 = (p22 * k0) ^ ((p19 ^ p20) * k1)
    # WG2
    v2 = ((p18 ^ p19) * k2) ^ (p18 * z0)
    v3 = ((p18 ^ p19) * k2) ^ (p19 * z1)
    # G3
    v4 = ((p21 ^ p20) * k3) ^ (p20 * z3)
    v5 = (p21 * z2) ^ (p20 * z3)

    # G1 + G3
    y0 = v0 ^ v4
    y1 = v1 ^ v5

    # WG2 + G3
    y2 = v2 ^ v4
    y3 = v3 ^ v5
    return get_num([y0, y1, y2, y3], 1)


def get_mul2():
    # global p0, p2, p4, p6, p8, p10, p12, p14, p16
    # global t0, t1, t2, t3

    # y3 + y1
    k0 = z0 ^ z2
    # y2 + y0
    k1 = z1 ^ z3
    # y3 + y2
    k2 = z0 ^ z1
    # y1 + y0
    k3 = z2 ^ z3
    # (y3 + y1) + (y2 + y0)
    k4 = k0 ^ k1

    # C1, C2, C3
    u0 = p0 * k4
    u1 = p2 * k0
    u2 = p4 * k1
    # C1, C2, C3
    u3 = p6 * k2
    u4 = p8 * z0
    u5 = p10 * z1
    # C1, C2, C3
    u6 = p12 * k3
    u7 = p14 * z2
    u8 = p16 * z3

    # G1
    v0 = u0 ^ u2
    v1 = u1 ^ u2
    # WG2
    v2 = u3 ^ u4
    v3 = u3 ^ u5
    # G3
    v4 = u6 ^ u8
    v5 = u7 ^ u8

    # G1 + G3
    y4 = v0 ^ v4
    y5 = v1 ^ v5

    # WG2 + G3
    y6 = v2 ^ v4
    y7 = v3 ^ v5

    return get_num([y4, y5, y6, y7], 1)

def G256_inv3(x: int):
    '''
    GF(2^8)的求逆操作
    '''
    global alpha, sum_ab
    global z0, z1, z2, z3
    inverse = G16_inv_box(get_inv_input2(x))
    z0 = get_bit(inverse, 3)
    z1 = get_bit(inverse, 2)
    z2 = get_bit(inverse, 1)
    z3 = get_bit(inverse, 0)
    # gamma1 = G16_mul(inverse, alpha)
    gamma1 = get_mul1()
    # gamma0 = G16_mul(inverse, sum_ab)
    gamma0 = get_mul2()
    return get_num([gamma1, gamma0], 4)
