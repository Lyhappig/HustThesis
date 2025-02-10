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


def part2(alpha: int) -> int:
    x0, x1, x2, x3 = get_bit(alpha, 3), get_bit(alpha, 2), get_bit(alpha, 1), get_bit(alpha, 0)
    # Here
    # 输入
    r0 = x1 ^ x2
    r1 = x0 ^ x1
    r2 = x2 ^ x3
    r3 = x0 ^ x2
    r4 = r0 ^ r2
    r5 = x3
    q0 = x0
    # 非线性部分
    q1 = 1 ^ r0
    t0 = q0 & q1
    s0 = r0 ^ r5
    q2 = s0 ^ t0
    q3 = 1 ^ r1 ^ t0
    t1 = q2 & q3
    q4 = q3 ^ r2 ^ t1
    q5 = r0 ^ t1
    t2 = q4 & q5
    s1 = r3 ^ t2
    q6 = s1 ^ r5
    q7 = s0 ^ t2
    t3 = q6 & q7
    q8 = s1 ^ t0 ^ t1
    q9 = r1 ^ r5 ^ t1
    t4 = q8 & q9
    # 输出
    t5 = t2 ^ t3
    y0 = q2 ^ t5 ^ t4
    y1 = r4 ^ t2 ^ t4
    y2 = q4 ^ 1 ^ t3
    y3 = q3 ^ 1 ^ t5

    return get_num([y0, y1, y2, y3], 1)


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



def GF256_inverse(x: int) -> int:
    return part3(part2(part1(x)))