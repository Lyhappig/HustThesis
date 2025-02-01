import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from GF4.gf4 import *
from utils.util import *

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
    C2 = G4_square(A1 ^ A0)
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


gf16_sbox = [0x0, 0x1, 0x3, 0x2, 0xf, 0xc, 0x9, 0xb, 0xa, 0x6, 0x8, 0x7, 0x5, 0xe, 0xd, 0x4]


def G16_inv_box(alpha: int) -> int:
    return gf16_sbox[alpha]
