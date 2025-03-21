from utils.check_sbox import check_sbox
from GF256.gf256 import *
from GF256.inverse1 import *
from GF256.inverse2 import *
from GF256.inverse3 import *
from GF256.inverse4 import *

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

'''
注意，无需转置，需要原矩阵
'''

tower_to_poly_mt = [
    0b00100011,
    0b11010001,
    0b11010110,
    0b10010100,
    0b01111010,
    0b00001100,
    0b01011100,
    0b00000001
]

poly_to_tower_mt = [
    0b01000111,
    0b11011010,
    0b01101011,
    0b11011100,
    0b10001111,
    0b10001011,
    0b11101010,
    0b00000001
]


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

'''
x = (b7, b6, b5, b4, b3, b2, b1, b0)
S(x) = M(Mx + C)^-1 + C
'''


def SM4_SBOX1(x):
    t = G256_new_basis(x, M)  # 仿射变换乘
    t ^= 0xd3
    t = G256_new_basis(t, poly_to_tower_mt)
    t = G256_inv1(t)
    t = G256_new_basis(t, tower_to_poly_mt)
    t = G256_new_basis(t, M)  # 仿射变换乘
    return t ^ 0xd3


def SM4_SBOX2(x):
    t = G256_new_basis(x, M)  # 仿射变换乘
    t ^= 0xd3
    t = G256_new_basis(t, poly_to_tower_mt)
    t = G256_inv2(t)
    t = G256_new_basis(t, tower_to_poly_mt)
    t = G256_new_basis(t, M)  # 仿射变换乘
    return t ^ 0xd3


def SM4_SBOX3(x):
    # 仿射变换和同构矩阵统一为 AND 前的 24 * 8 放射矩阵
    t = G256_inv3(x)
    t = G256_new_basis(t, tower_to_poly_mt)
    t = G256_new_basis(t, M)  # 仿射变换乘
    return t ^ 0xd3


def SM4_SBOX4(x):
    return G256_inv4(x)


def SM4_SBOX5(x):
    return GF256_inverse1(x)


def SM4_SBOX6(x):
    return GF256_inverse2(x)


def SM4_SBOX7(x):
    return GF256_inverse3(x)


def SM4_SBOX8(x):
    return GF256_inverse4(x)


if __name__ == '__main__':
    # check_sbox()
    sbox = []
    for i in range(256):
        sbox.append(SM4_SBOX8(i))

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
