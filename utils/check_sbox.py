import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from typing import List
from utils.tower_basis_poly import get_isomorphic_matrix

tower_to_poly_mt = []
poly_to_tower_mt = []


def get_bit(x: int, i: int) -> int:
    return (x >> i) & 1


def get_num(nums: List[int], bits: int) -> int:
    ret = 0
    for num in nums:
        ret <<= bits
        ret |= num
    return ret


def G4_mul(A: int, B: int) -> int:
    '''
    GF(2^2)的乘法运算
    '''
    a1, a0 = get_bit(A, 1), get_bit(A, 0)
    b1, b0 = get_bit(B, 1), get_bit(B, 0)
    c1 = (a1 ^ a0) & (b1 ^ b0)
    c2 = a1 & b1
    c3 = a0 & b0
    return get_num([c1 ^ c3, c2 ^ c3], 1)


def G4_square(A: int) -> int:
    '''
    GF(2^2)的平方运算
    '''
    a1, a0 = get_bit(A, 1), get_bit(A, 0)
    return get_num([a1, a1 ^ a0], 1)


def G4_inv(A: int) -> int:
    '''
    GF(2^2)的求逆，等价于平方
    '''
    return G4_square(A)


def G4_mul_W(A: int) -> int:
    '''
    GF(2^2)的乘W操作
    '''
    a1, a0 = get_bit(A, 1), get_bit(A, 0)
    return get_num([a1 ^ a0, a1], 1)


def G4_mul_W2(A: int) -> int:
    '''
    GF(2^2)的乘W^2操作
    '''
    a1, a0 = get_bit(A, 1), get_bit(A, 0)
    return get_num([a0, a1 ^ a0], 1)


def G4_square_W(A: int) -> int:
    '''
    GF(2^2)的平方乘W^2操作
    '''
    a1, a0 = get_bit(A, 1), get_bit(A, 0)
    return get_num([a0, a1], 1)


def G4_square_W2(A: int) -> int:
    '''
    GF(2^2)的平方乘W^2操作
    '''
    a1, a0 = get_bit(A, 1), get_bit(A, 0)
    return get_num([a1 ^ a0, a0], 1)


def G16_mul(alpha: int, beta: int) -> int:
    '''
    GF(2^4)的乘法操作，T = 1, N = W
    '''
    A1 = (alpha & 0xc) >> 2
    A0 = alpha & 0x3
    B1 = (beta & 0xc) >> 2
    B0 = beta & 0x3

    C1 = G4_mul(A1 ^ A0, B1 ^ B0)
    C2 = G4_mul(A1, B1)
    C3 = G4_mul(A0, B0)
    C4 = G4_mul_W(C2)
    return get_num([C1 ^ C3, C3 ^ C4], 2)


def G16_square_mul_n(alpha: int) -> int:
    '''
    GF(2^4)的平方乘 n 操作，n = NZ + 1
    '''
    A1 = (alpha & 0xc) >> 2
    A0 = alpha & 0x3

    C1 = G4_square_W(A0)
    C2 = G4_square(A0 ^ A1)
    return get_num([C1, C2], 2)


def G16_mul_t(alpha: int) -> int:
    '''
    GF(2^4)的乘法操作，t = 1
    '''
    return alpha


def G16_inv(alpha: int) -> int:
    '''
    GF(2^4)的求逆操作，T = 1, N = W
    '''
    A1 = (alpha & 0xc) >> 2
    A0 = alpha & 0x3

    C1 = G4_square_W(A1)
    C2 = A1 ^ A0
    C3 = G4_mul(C2, A0)
    C4 = G4_inv(C1 ^ C3)

    D1 = G4_mul(C4, A1)
    D0 = G4_mul(C4, C2)
    return get_num([D1, D0], 2)


def G256_inv(x):
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


def G256_new_basis(x, b):
    '''
    x在新基b下的表示
    '''
    y = 0
    for i in range(8):
        if x & (1 << (7 - i)):
            y ^= b[i]
    return y


M = [0b11100101,
     0b11110010,
     0b01111001,
     0b10111100,
     0b01011110,
     0b00101111,
     0b10010111,
     0b11001011]


def SM4_SBOX(x):
    global tower_to_poly_mt, poly_to_tower_mt
    t = G256_new_basis(x, M)  # 仿射变换乘
    t ^= 0xd3
    t = G256_new_basis(t, poly_to_tower_mt)
    t = G256_inv(t)
    t = G256_new_basis(t, tower_to_poly_mt)
    t = G256_new_basis(t, M)  # 仿射变换乘
    return t ^ 0xd3


sm4_sbox = [
    0xD6, 0x90, 0xE9, 0xFE, 0xCC, 0xE1, 0x3D, 0xB7, 0x16, 0xB6, 0x14, 0xC2, 0x28, 0xFB, 0x2C, 0x05,
    0x2B, 0x67, 0x9A, 0x76, 0x2A, 0xBE, 0x04, 0xC3, 0xAA, 0x44, 0x13, 0x26, 0x49, 0x86, 0x06, 0x99,
    0x9C, 0x42, 0x50, 0xF4, 0x91, 0xEF, 0x98, 0x7A, 0x33, 0x54, 0x0B, 0x43, 0xED, 0xCF, 0xAC, 0x62,
    0xE4, 0xB3, 0x1C, 0xA9, 0xC9, 0x08, 0xE8, 0x95, 0x80, 0xDF, 0x94, 0xFA, 0x75, 0x8F, 0x3F, 0xA6,
    0x47, 0x07, 0xA7, 0xFC, 0xF3, 0x73, 0x17, 0xBA, 0x83, 0x59, 0x3C, 0x19, 0xE6, 0x85, 0x4F, 0xA8,
    0x68, 0x6B, 0x81, 0xB2, 0x71, 0x64, 0xDA, 0x8B, 0xF8, 0xEB, 0x0F, 0x4B, 0x70, 0x56, 0x9D, 0x35,
    0x1E, 0x24, 0x0E, 0x5E, 0x63, 0x58, 0xD1, 0xA2, 0x25, 0x22, 0x7C, 0x3B, 0x01, 0x21, 0x78, 0x87,
    0xD4, 0x00, 0x46, 0x57, 0x9F, 0xD3, 0x27, 0x52, 0x4C, 0x36, 0x02, 0xE7, 0xA0, 0xC4, 0xC8, 0x9E,
    0xEA, 0xBF, 0x8A, 0xD2, 0x40, 0xC7, 0x38, 0xB5, 0xA3, 0xF7, 0xF2, 0xCE, 0xF9, 0x61, 0x15, 0xA1,
    0xE0, 0xAE, 0x5D, 0xA4, 0x9B, 0x34, 0x1A, 0x55, 0xAD, 0x93, 0x32, 0x30, 0xF5, 0x8C, 0xB1, 0xE3,
    0x1D, 0xF6, 0xE2, 0x2E, 0x82, 0x66, 0xCA, 0x60, 0xC0, 0x29, 0x23, 0xAB, 0x0D, 0x53, 0x4E, 0x6F,
    0xD5, 0xDB, 0x37, 0x45, 0xDE, 0xFD, 0x8E, 0x2F, 0x03, 0xFF, 0x6A, 0x72, 0x6D, 0x6C, 0x5B, 0x51,
    0x8D, 0x1B, 0xAF, 0x92, 0xBB, 0xDD, 0xBC, 0x7F, 0x11, 0xD9, 0x5C, 0x41, 0x1F, 0x10, 0x5A, 0xD8,
    0x0A, 0xC1, 0x31, 0x88, 0xA5, 0xCD, 0x7B, 0xBD, 0x2D, 0x74, 0xD0, 0x12, 0xB8, 0xE5, 0xB4, 0xB0,
    0x89, 0x69, 0x97, 0x4A, 0x0C, 0x96, 0x77, 0x7E, 0x65, 0xB9, 0xF1, 0x09, 0xC5, 0x6E, 0xC6, 0x84,
    0x18, 0xF0, 0x7D, 0xEC, 0x3A, 0xDC, 0x4D, 0x20, 0x79, 0xEE, 0x5F, 0x3E, 0xD7, 0xCB, 0x39, 0x48,
]


def compare():
    sbox = []
    for i in range(256):
        sbox.append(SM4_SBOX(i))  # 生成sbox

    flag = True
    for i in range(256):
        if sbox[i] != sm4_sbox[i]:
            flag = False
            break

    print(flag)

    for i, s in enumerate(sbox):
        print(f'%02x' % s, ', ', end='')
        if (i + 1) % 16 == 0:
            print()


def check_sbox():
    global tower_to_poly_mt, poly_to_tower_mt
    ls = get_isomorphic_matrix()
    for i in range(len(ls)):
        tower_to_poly_mt = ls[i][0]
        poly_to_tower_mt = ls[i][1]
        compare()
