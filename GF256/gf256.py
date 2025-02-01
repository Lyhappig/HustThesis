import os
import sys

from MyThesis.utils.matrix import GF2Matrix

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from GF16.gf16 import *
from utils.util import *
from utils.matrix import *


def G256_inv(x: int):
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
def get_data(x: int):
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


data_mt = [
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
]


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
    affine = GF2Matrix(data_mt)
    out = (affine * input).matrix
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


def G256_inv2(x: int):
    '''
    GF(2^8)的求逆操作
    '''
    alpha = (x & 0xF0) >> 4
    beta = x & 0x0F

    inverse = G16_inv_box(get_data2(x))
    gamma1 = G16_mul(inverse, alpha)
    gamma0 = G16_mul(inverse, alpha ^ beta)
    return get_num([gamma1, gamma0], 4)
