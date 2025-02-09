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
    [1, 1, 1, 1, 1, 1, 1, 1],   # p0 = x7 + x6 + x5 + x4 + x3 + x2 + x1 + x0
    [0, 0, 0, 0, 1, 1, 1, 1],   # p1 = x3 + x2 + x1 + x0
    [1, 0, 1, 0, 1, 0, 1, 0],   # p2 = x7 + x5 + x3 + x1
    [0, 0, 0, 0, 1, 0, 1, 0],   # p3 = x3 + x1
    [0, 1, 0, 1, 0, 1, 0, 1],   # p4 = x6 + x4 + x2 + x0
    [0, 0, 0, 0, 0, 1, 0, 1],   # p5 = x2 + x0
    [1, 1, 0, 0, 1, 1, 0, 0],   # p6 = x7 + x6 + x3 + x2
    [0, 0, 0, 0, 1, 1, 0, 0],   # p7 = x3 + x2
    [1, 0, 0, 0, 1, 0, 0, 0],   # p8 = x7 + x3
    [0, 0, 0, 0, 1, 0, 0, 0],   # p9 = x3
    [0, 1, 0, 0, 0, 1, 0, 0],   # p10 = x6 + x2
    [0, 0, 0, 0, 0, 1, 0, 0],   # p11 = x2
    [0, 0, 1, 1, 0, 0, 1, 1],   # p12 = x5 + x4 + x1 + x0
    [0, 0, 0, 0, 0, 0, 1, 1],   # p13 = x1 + x0
    [0, 0, 1, 0, 0, 0, 1, 0],   # p14 = x5 + x1
    [0, 0, 0, 0, 0, 0, 1, 0],   # p13 = x1
    [0, 0, 0, 1, 0, 0, 0, 1],   # p16 = x4 + x0
    [0, 0, 0, 0, 0, 0, 0, 1],   # p17 = x0
    # ---------------------------------------------------
    [1, 1, 1, 1, 0, 0, 0, 0],   # p18 = x7 + x6 + x5 + x4
    [1, 1, 0, 0, 0, 0, 0, 0],   # p19 = x7 + x6
    [1, 0, 1, 0, 0, 0, 0, 0],   # p20 = x7 + x5
    [0, 1, 0, 1, 0, 0, 0, 0],   # p21 = x6 + x4
    [0, 0, 1, 1, 0, 0, 0, 0],   # p22 = x5 + x4
    [1, 0, 0, 0, 0, 0, 0, 0],   # p23 = x7
    [0, 1, 0, 0, 0, 0, 0, 0],   # p24 = x6
    [0, 0, 1, 0, 0, 0, 0, 0],   # p25 = x5
    [0, 0, 0, 1, 0, 0, 0, 0],   # p26 = x4
])

p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11 = [0] * 12
p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26 = [0] * 15
z0, z1, z2, z3 = [0] * 4


def get_inv_input2(x: int):
    global alpha, sum_ab
    # alpha = get_num([p23, p24, p25, p26], 1)
    # sum_ab = get_num([p8, p10, p14, p16], 1)
    global p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11
    global p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26

    # Mt = Affine3 * P2T * M
    # print(Mt)

    x0, x1, x2, x3 = get_bit(x, 7), get_bit(x, 6), get_bit(x, 5), get_bit(x, 4)
    x4, x5, x6, x7 = get_bit(x, 3), get_bit(x, 2), get_bit(x, 1), get_bit(x, 0)

    p13 = x7
    p15 = x2 ^ x6
    p17 = x7 ^ p15
    p19 = x0 ^ x5
    p11 = x3 ^ p19
    p5 = p17 ^ p11
    p20 = x1 ^ p19
    p22 = x2 ^ x4
    p12 = x7 ^ p22
    p3 = x0 ^ p12
    p1 = p5 ^ p3
    p2 = p20 ^ p3
    p7 = x7 ^ p1
    p6 = p19 ^ p7
    p0 = p12 ^ p6
    p4 = p2 ^ p0
    p9 = p11 ^ p7
    p10 = x6 ^ p2
    p8 = p6 ^ p10
    p14 = p2 ^ p8
    p16 = p4 ^ p10
    p18 = p1 ^ p0
    p21 = p20 ^ p18
    p23 = p9 ^ p8
    p24 = p11 ^ p10
    p25 = p20 ^ p23
    p26 = p21 ^ p24

    # Affine3 * P2T * C: (7, 9, 13, 15, 19, 22, 23, 25) XOR 1
    p7 ^= 1
    p9 ^= 1
    p13 ^= 1
    p15 ^= 1
    p19 ^= 1
    p22 ^= 1
    p23 ^= 1
    p25 ^= 1

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

    t0 = p26 ^ s0
    t1 = p25 ^ s1
    t2 = p20 ^ s2
    t3 = p18 ^ s3
    return get_num([t0, t1, t2, t3], 1)


def inverse_alpha():
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
    u0 = p18 * k4
    u1 = p20 * k0
    u2 = p21 * k1
    # C1, C2, C3
    u3 = p19 * k2
    u4 = p23 * z0
    u5 = p24 * z1
    # C1, C2, C3
    u6 = p22 * k3
    u7 = p25 * z2
    u8 = p26 * z3

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
    y0 = v0 ^ v4
    y1 = v1 ^ v5

    # WG2 + G3
    y2 = v2 ^ v4
    y3 = v3 ^ v5
    return get_num([y0, y1, y2, y3], 1)


def inverse_sum_ab():
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


def get_two_mul():
    k0 = z0 ^ z2
    k1 = z1 ^ z3
    k2 = z0 ^ z1
    k3 = z2 ^ z3
    k4 = k0 ^ k1

    # inverse * alpha, G1: C1, C2, C3
    u0 = p18 * k4
    u1 = p20 * k0
    u2 = p21 * k1
    # inverse * alpha, WG2: C1, C2, C3
    u3 = p19 * k2
    u4 = p23 * z0
    u5 = p24 * z1
    # inverse * alpha, G3: C1, C2, C3
    u6 = p22 * k3
    u7 = p25 * z2
    u8 = p26 * z3
    # inverse * (alpha + beta), G1: C1, C2, C3
    u9 = p0 * k4
    u10 = p2 * k0
    u11 = p4 * k1
    # inverse * (alpha + beta), WG2: C1, C2, C3
    u12 = p6 * k2
    u13 = p8 * z0
    u14 = p10 * z1
    # inverse * (alpha + beta), G3: C1, C2, C3
    u15 = p12 * k3
    u16 = p14 * z2
    u17 = p16 * z3

    # inverse * alpha: G1
    v0 = u0 ^ u2
    v1 = u1 ^ u2
    # inverse * alpha: WG2
    v2 = u3 ^ u4
    v3 = u3 ^ u5
    # inverse * alpha: G3
    v4 = u6 ^ u8
    v5 = u7 ^ u8

    # inverse * (alpha + beta): G1
    v6 = u9 ^ u11
    v7 = u10 ^ u11
    # inverse * (alpha + beta): WG2
    v8 = u12 ^ u13
    v9 = u12 ^ u14
    # inverse * (alpha + beta): G3
    v10 = u15 ^ u17
    v11 = u16 ^ u17

    y0 = v0 ^ v4
    y1 = v1 ^ v5
    y2 = v2 ^ v4
    y3 = v3 ^ v5
    y4 = v6 ^ v10
    y5 = v7 ^ v11
    y6 = v8 ^ v10
    y7 = v9 ^ v11

    return get_num([y0, y1, y2, y3, y4, y5, y6, y7], 1)


def G256_inv3(x: int):
    '''
    GF(2^8)的求逆操作
    '''
    global z0, z1, z2, z3
    T = get_inv_input2(x)
    inverse = G16_inv_box(T)
    z0 = get_bit(inverse, 3)
    z1 = get_bit(inverse, 2)
    z2 = get_bit(inverse, 1)
    z3 = get_bit(inverse, 0)
    # gamma1 = G16_mul(inverse, alpha)
    # gamma0 = G16_mul(inverse, sum_ab)
    # gamma1 = inverse_alpha()
    # gamma0 = inverse_sum_ab()
    return get_two_mul()


Out_Affine1 = GF2Matrix([
    [1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1],
])

Out_Affine2 = GF2Matrix([
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
])


def get_two_mul2():
    '''
    M * T2P * Out_Affine1 = [8 * 18]:
    [[0 0 0 0 0 0 0 0 0 1 0 1 1 0 1 1 1 0]
     [0 1 1 1 0 1 0 0 0 1 1 0 1 0 1 1 0 1]
     [1 1 0 1 0 1 1 0 1 1 1 0 1 1 0 0 1 1]
     [0 0 0 0 1 1 1 1 0 1 1 0 1 1 0 0 1 1]
     [0 0 0 0 0 0 0 0 0 1 0 1 0 1 1 0 1 1]
     [1 0 1 1 0 1 1 1 0 1 0 1 1 1 0 0 0 0]
     [0 0 0 0 1 1 1 1 0 1 0 1 0 1 1 0 1 1]
     [1 0 1 1 1 0 0 0 0 0 1 1 0 1 1 1 0 1]]

     M * T2P * Out_Affine2 = [8 * 12]
     [[0 0 0 0 0 0 1 0 0 1 1 1]
     [0 1 0 1 0 0 1 1 0 1 1 0]
     [1 1 0 1 1 0 1 1 1 0 0 1]
     [0 0 1 1 1 1 1 1 1 0 0 1]
     [0 0 0 0 0 0 1 0 1 1 0 1]
     [1 0 0 1 1 1 1 0 1 0 0 0]
     [0 0 1 1 1 1 1 0 1 1 0 1]
     [1 0 1 0 0 0 0 1 1 1 1 0]]
    '''
    k0 = z0 ^ z2
    k1 = z1 ^ z3
    k2 = z0 ^ z1
    k3 = z2 ^ z3
    k4 = k0 ^ k1

    u0 = p18 * k4
    u1 = p20 * k0
    u2 = p21 * k1
    u3 = p19 * k2
    u4 = p23 * z0
    u5 = p24 * z1
    u6 = p22 * k3
    u7 = p25 * z2
    u8 = p26 * z3
    u9 = p0 * k4
    u10 = p2 * k0
    u11 = p4 * k1
    u12 = p6 * k2
    u13 = p8 * z0
    u14 = p10 * z1
    u15 = p12 * k3
    u16 = p14 * z2
    u17 = p16 * z3

    # 32 XOR 得到结果，还能更优
    t0 = u9 ^ u16
    t1 = u13 ^ u17
    t2 = u11 ^ u14
    t3 = t0 ^ t1
    y4 = t2 ^ t3
    t5 = u15 ^ t0
    t6 = u12 ^ t5
    y0 = t2 ^ t6
    t8 = u5 ^ u6
    t9 = u7 ^ t8
    t10 = u4 ^ t9
    y6 = y4 ^ t10
    t12 = u10 ^ t5
    t13 = y6 ^ t12
    y3 = y0 ^ t13
    t15 = u0 ^ u3
    t16 = u2 ^ t9
    t17 = t15 ^ t16
    y7 = t13 ^ t17
    t19 = u9 ^ u11
    t20 = u12 ^ u13
    t21 = t19 ^ t20
    y5 = t17 ^ t21
    t23 = u1 ^ u4
    t24 = u0 ^ t13
    t25 = u5 ^ y5
    t26 = t23 ^ t24
    y1 = t25 ^ t26
    t28 = u3 ^ u7
    t29 = u8 ^ y0
    t30 = t26 ^ t28
    y2 = t29 ^ t30

    y0 ^= 1
    y1 ^= 1
    y3 ^= 1
    y6 ^= 1
    y7 ^= 1

    return get_num([y0, y1, y2, y3, y4, y5, y6, y7], 1)


def G256_inv4(x: int):
    '''
    GF(2^8)的求逆操作
    '''
    global z0, z1, z2, z3
    T = get_inv_input2(x)
    inverse = G16_inv_box(T)
    z0 = get_bit(inverse, 3)
    z1 = get_bit(inverse, 2)
    z2 = get_bit(inverse, 1)
    z3 = get_bit(inverse, 0)
    # gamma1 = G16_mul(inverse, alpha)
    # gamma0 = G16_mul(inverse, sum_ab)
    # gamma1 = inverse_alpha()
    # gamma0 = inverse_sum_ab()
    return get_two_mul2()
