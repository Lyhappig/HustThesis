import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.util import *
from utils.matrix import *

p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11 = [0] * 12
p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26 = [0] * 15


# 41 XOR, depth: 8
def part1(x: int):
    global p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11
    global p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26

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
    p9 = p15 ^ p3
    p6 = x3 ^ p9
    p10 = x6 ^ p2
    p18 = p19 ^ p22
    p0 = p1 ^ p18
    p21 = x1 ^ p22
    p4 = p5 ^ p21
    w0 = x2 ^ x3
    p8 = p20 ^ w0
    p14 = p3 ^ w0
    p16 = x0 ^ w0
    p23 = p9 ^ p8
    p25 = p15 ^ p14
    p26 = p17 ^ p16
    p24 = p21 ^ p26

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


# 25 XOR, depth: 12
def part2(alpha: int) -> int:
    t0, t1, t2, t3 = get_bit(alpha, 3), get_bit(alpha, 2), get_bit(alpha, 1), get_bit(alpha, 0)
    # Here
    # 输入
    a0 = t1 ^ t2
    a1 = t0 ^ t1
    a2 = t2 ^ t3
    a3 = t0 ^ t2
    a4 = t1 ^ t3
    a5 = t3
    b0 = t0
    # 非线性部分
    b1 = 1 ^ a0
    c0 = b0 & b1
    d0 = a0 ^ a5
    b2 = d0 ^ c0
    b3 = 1 ^ a1 ^ c0
    c1 = b2 & b3
    b4 = b3 ^ a2 ^ c1
    b5 = a0 ^ c1
    c2 = b4 & b5
    d1 = a3 ^ c2
    b6 = d1 ^ a5
    b7 = d0 ^ c2
    c3 = b6 & b7
    b8 = d1 ^ c0 ^ c1
    b9 = a1 ^ a5 ^ c1
    c4 = b8 & b9
    # 输出
    c5 = c2 ^ c3
    z0 = b2 ^ c5 ^ c4
    z1 = a4 ^ c2 ^ c4
    z2 = b4 ^ 1 ^ c3
    z3 = b3 ^ 1 ^ c5

    return get_num([z0, z1, z2, z3], 1)


# 40 XOR, depth: 7
def part3(gamma: int) -> int:
    z0, z1, z2, z3 = get_bit(gamma, 3), get_bit(gamma, 2), get_bit(gamma, 1), get_bit(gamma, 0)
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

    v0 = u9 ^ u16
    v1 = u13 ^ u17
    v2 = u11 ^ u14
    v3 = v0 ^ v1
    y4 = v2 ^ v3
    v4 = u5 ^ u6
    v5 = u7 ^ v4
    v6 = u10 ^ u12
    v7 = u0 ^ u3
    v8 = u4 ^ v5
    y6 = y4 ^ v8
    v9 = v3 ^ v6
    y3 = v8 ^ v9
    v10 = u15 ^ v0
    v11 = u2 ^ v5
    v12 = u1 ^ v9
    v13 = u9 ^ u13
    v14 = u12 ^ v2
    y0 = v10 ^ v14
    v15 = u14 ^ v13
    v16 = u8 ^ v4
    v17 = v7 ^ v16
    y2 = v12 ^ v17
    v18 = v7 ^ v11
    v19 = v14 ^ v15
    y5 = v18 ^ v19
    v20 = u2 ^ u4
    v21 = v7 ^ v9
    v22 = y0 ^ v20
    y7 = v21 ^ v22
    v23 = u2 ^ u3
    v24 = u5 ^ v10
    v25 = v15 ^ v23
    v26 = v24 ^ v25
    y1 = v12 ^ v26

    y0 ^= 1
    y1 ^= 1
    y3 ^= 1
    y6 ^= 1
    y7 ^= 1

    return get_num([y0, y1, y2, y3, y4, y5, y6, y7], 1)



def GF256_inverse2(x: int) -> int:
    return part3(part2(part1(x)))