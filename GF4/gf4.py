import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from typing import List
from utils.util import *

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
