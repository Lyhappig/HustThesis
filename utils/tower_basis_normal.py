import os
import sys

import galois
import numpy as np

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.matrix import GF2Matrix

# 定义 AES 不可约多项式 x^8 + x^4 + x^3 + x + 1
irreducible_poly = galois.Poly.Degrees([8, 4, 3, 1, 0])
# irreducible_poly = galois.Poly.Degrees([8, 7, 6, 5, 4, 2, 0])

# 定义伽罗瓦域 GF(2^8)
GF_256 = galois.GF(2 ** 8, irreducible_poly=irreducible_poly, repr='poly')

W = GF_256(0)
W_2 = GF_256(0)
Z = GF_256(0)
Z_4 = GF_256(0)
N = GF_256(0)
Y = GF_256(0)
Y_16 = GF_256(0)
n = GF_256(0)

# AES多项式基在塔域正规基下的表示
X = np.array([
        [0, 0, 0, 1, 0, 0, 1, 0],
        [1, 1, 1, 0, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1],
        [0, 1, 0, 0, 0, 0, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 0],
        [1, 0, 1, 1, 0, 0, 1, 0],
        [0, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],], dtype=int)
X_inv = np.array([])

# AES 代数表达式中的矩阵M
M = np.array([
        [1, 1, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 1, 1, 1, 1, 1],
        [1, 0, 0, 0, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 1],
        [1, 1, 1, 1, 0, 0, 0, 1],], dtype=int)
cb = np.array([0, 1, 1, 0, 0, 0, 1, 1], dtype=int).reshape(-1, 1)


def to_8bit_bin(num):
    # 使用格式化字符串将数字转换为8位二进制，前面补0
    return f"{num:08b}"

def print_matrix(matrix):
    print("[", end="")
    for i, row in enumerate(matrix):
        if i > 0:
            print(" ", end="")
        print("[", end="")
        for j, element in enumerate(row):
            print(element, end="")
            if j < len(row) - 1:
                print(", ", end="")
        print("]", end="")
        if i < len(matrix) - 1:
            print(",")
    print("]")

def get_power(x, n):
    if n == 1:
        return x
    mid_pow = get_power(x, n / 2)
    return mid_pow * mid_pow

'''
获得同构矩阵及其逆
'''
def get_isomorphic_matrix():
    global W, W_2, Z, Z_4, N, Y, Y_16, n

    root_W = []
    for i in range(GF_256.order):
        element = GF_256(i)
        if element**2 + element + GF_256(1) == 0:
            W = element
            root_W.append(element)
            # print(hex(element), element)
    W_2, W = GF_256(0xBC), GF_256(0xBD)
    # W_2, W = root_W[0], root_W[1]
    # print(hex(W_2), hex(W))
    # 上述方程的两个根是等价的，任意一个根及其2次方都可以作为 GF(2^2) 下的正规基
    print(hex(get_power(W, 2)), hex(W))

    N = W_2
    root_Z = []
    for i in range(GF_256.order):
        element = GF_256(i)
        if element**2 + element + N == 0:
            Z = element
            root_Z.append(element)
            # print(hex(element), element)
    Z_4, Z = GF_256(0x5D), GF_256(0x5C)
    # Z_4, Z = root_Z[0], root_Z[1]
    # print(hex(Z_4), hex(Z))
    # 上述方程的两个根是等价的，任意一个根及其4次方都可以作为 GF(2^4) 下的正规基
    print(hex(get_power(Z, 4)), hex(Z))

    n = N * N * Z
    root_Y = []
    for i in range(GF_256.order):
        element = GF_256(i)
        if element**2 + element + n == 0:
            Y = element
            root_Y.append(element)
            # print(hex(element), element)
    Y_16, Y = GF_256(0xFE), GF_256(0xFF)
    # Y_16, Y = root_Y[0], root_Y[1]
    # print(hex(Y_16), hex(Y))
    # 上述方程的两个根是等价的，任意一个根及其16次方都可以作为 GF(2^8) 下的正规基
    print(hex(get_power(Y, 16)), hex(Y))

    W_2_Z_4_Y_16 = W_2 * Z_4 * Y_16
    W_Z_4_Y_16 = W * Z_4 * Y_16
    W_2_Z_Y_16 = W_2 * Z * Y_16
    W_Z_Y_16 = W * Z * Y_16
    W_2_Z_4_Y = W_2 * Z_4 * Y
    W_Z_4_Y = W * Z_4 * Y
    W_2_Z_Y = W_2 * Z * Y
    W_Z_Y = W * Z * Y
    print('W_2_Z_4_Y_16\t', to_8bit_bin(W_2_Z_4_Y_16))
    print('W_Z_4_Y_16\t\t', to_8bit_bin(W_Z_4_Y_16))
    print('W_2_Z_Y_16\t\t', to_8bit_bin(W_2_Z_Y_16))
    print('W_Z_Y_16\t\t', to_8bit_bin(W_Z_Y_16))
    print('W_2_Z_4_Y\t\t', to_8bit_bin(W_2_Z_4_Y))
    print('W_Z_4_Y\t\t\t', to_8bit_bin(W_Z_4_Y))
    print('W_2_Z_Y\t\t\t', to_8bit_bin(W_2_Z_Y))
    print('W_Z_Y\t\t\t', to_8bit_bin(W_Z_Y))

    # 原始矩阵
    matrix = [
        to_8bit_bin(W_2_Z_4_Y_16),
        to_8bit_bin(W_Z_4_Y_16),
        to_8bit_bin(W_2_Z_Y_16),
        to_8bit_bin(W_Z_Y_16),
        to_8bit_bin(W_2_Z_4_Y),
        to_8bit_bin(W_Z_4_Y),
        to_8bit_bin(W_2_Z_Y),
        to_8bit_bin(W_Z_Y)
    ]

    X = GF2Matrix([[int(bit) for bit in row] for row in matrix])
    # X.T()
    print("X = ")
    print_matrix(X.matrix)
    X_inv = X.inverse()
    print("X^{-1} = ")
    print_matrix(X_inv.matrix)
    unit = X * X_inv
