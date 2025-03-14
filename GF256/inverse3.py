import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.util import *
from utils.matrix import *

p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11 = [0] * 12
p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26 = [0] * 15


def part1(x: int):
    global p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11
    global p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26

    x0, x1, x2, x3 = get_bit(x, 7), get_bit(x, 6), get_bit(x, 5), get_bit(x, 4)
    x4, x5, x6, x7 = get_bit(x, 3), get_bit(x, 2), get_bit(x, 1), get_bit(x, 0)

    p13 = x7 ^ 1
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
    p9 = p15 ^ p3 ^ 1
    p10 = x6 ^ p2
    p8 = p6 ^ p10
    p14 = x6 ^ p6
    p18 = p19 ^ p22
    p21 = x1 ^ p22
    p4 = p5 ^ p21
    p16 = p10 ^ p4
    p23 = x3 ^ p10 ^ 1
    p24 = p11 ^ p10
    p25 = x1 ^ p24 ^ 1
    p26 = x4 ^ p6
    p7 = p7 ^ 1
    p15 = p15 ^ 1
    p19 = p19 ^ 1
    p22 = p22 ^ 1

    q0 = p0 * p1
    q1 = p2 * p3
    q2 = p4 * p5
    q3 = p6 * p7
    q4 = p8 * p9
    q5 = p10 * p11
    q6 = p12 * p13
    q7 = p14 * p15
    q8 = p16 * p17

    r0 = q0 ^ q2
    r1 = q1 ^ q2
    r2 = q3 ^ q4
    r3 = q3 ^ q5
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


def part2(alpha: int) -> int:
    t0, t1, t2, t3 = get_bit(alpha, 3), get_bit(alpha, 2), get_bit(alpha, 1), get_bit(alpha, 0)
    f0 = t0
    f1 = t2
    f2 = t3
    f3 = t1
    g0 = f3 & f1
    f2 = g0 ^ f2
    g1 = f2 & f0
    f3 = g1 ^ f3
    f0 = f3 ^ f0
    f2 = f1 ^ f2
    f3 = f2 ^ f3
    g2 = f0 & f1
    g2 = g2 & f3
    f2 = g2 ^ f2
    g3 = f3 & f2
    f1 = g3 ^ f1
    g4 = f1 & f0
    f3 = g4 ^ f3
    f1 = f2 ^ f1
    f2 = f3 ^ f2
    f1 = f0 ^ f1
    z0 = f0
    z1 = f2
    z2 = f1
    z3 = f3
    return get_num([z0, z1, z2, z3], 1)


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

    v0 = u9 ^ u12
    v1 = u11 ^ u14
    v2 = u16 ^ v0
    v3 = v1 ^ v2
    y0 = u15 ^ v3
    v5 = u13 ^ u17
    v6 = u12 ^ v3
    y4 = v5 ^ v6
    v8 = u5 ^ u6
    v9 = u7 ^ v8
    v10 = u4 ^ v9
    y6 = y4 ^ v10 ^ 1
    v12 = u10 ^ v2
    v13 = v5 ^ v12
    y3 = v10 ^ v13
    v15 = u0 ^ u3
    v16 = v9 ^ v15
    v17 = u2 ^ v16
    v18 = y3 ^ v17
    y7 = y0 ^ v18 ^ 1
    v20 = u13 ^ v0
    v21 = u11 ^ v20
    y5 = v17 ^ v21
    v23 = v13 ^ v16
    v24 = u1 ^ v23
    v25 = u8 ^ v24
    y2 = u7 ^ v25
    v27 = y5 ^ v24
    v28 = y0 ^ v27
    v29 = u5 ^ v28
    y1 = u3 ^ v29 ^ 1
    y0 = y0 ^ 1
    y3 = y3 ^ 1

    return get_num([y0, y1, y2, y3, y4, y5, y6, y7], 1)



def GF256_inverse3(x: int) -> int:
    return part3(part2(part1(x)))