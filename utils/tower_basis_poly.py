import os
import sys

import galois
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.matrix import GF2Matrix

# 定义 SM4 不可约多项式 x^8 + x^7 + x^6 + x^5 + x^4 + x^2 + 1
irreducible_poly = galois.Poly.Degrees([8, 7, 6, 5, 4, 2, 0])
# irreducible_poly = galois.Poly.Degrees([8, 4, 3, 1, 0])

# 定义伽罗瓦域 GF(2^8)
GF_256 = galois.GF(2 ** 8, irreducible_poly=irreducible_poly, repr='poly')

target_ls = []

W = GF_256(0)
Z = GF_256(0)
Y = GF_256(0)
T = GF_256(0)
N = GF_256(0)
t = GF_256(0)
n = GF_256(0)

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


def matrix_to_ls(matrix):
    ret = []
    for i in range(8):
        x = 0
        for j in range(8):
            x <<= 1
            x |= matrix[i][j]
        ret.append(x)
    return ret


def get_mt(W, Z, Y):
    # print("\"" + to_8bit_bin(W * Z * Y) + "\",")
    # print("\"" + to_8bit_bin(Z * Y) + "\",")
    # print("\"" + to_8bit_bin(W * Y) + "\",")
    # print("\"" + to_8bit_bin(Y) + "\",")
    # print("\"" + to_8bit_bin(W * Z) + "\",")
    # print("\"" + to_8bit_bin(Z) + "\",")
    # print("\"" + to_8bit_bin(W) + "\",")
    # print("\"" + to_8bit_bin(1) + "\",")
    matrix = [
        to_8bit_bin(W * Z * Y),
        to_8bit_bin(Z * Y),
        to_8bit_bin(W * Y),
        to_8bit_bin(Y),
        to_8bit_bin(W * Z),
        to_8bit_bin(Z),
        to_8bit_bin(W),
        to_8bit_bin(1)
    ]
    X = GF2Matrix([[int(bit) for bit in row] for row in matrix])
    # X.T()

    print("tower_to_poly = ", end='')
    print_matrix(X.matrix)
    X_inv = X.inverse()
    print("poly_to_tower = ", end='')
    print_matrix(X_inv.matrix)
    target_ls.append([matrix_to_ls(X.matrix), matrix_to_ls(X_inv.matrix)])


def get_Y():
    global W, Z, Y, T, N, t, n
    t = GF_256(1)
    n = N * Z + GF_256(1)
    for i in range(GF_256.order):
        y = GF_256(i)
        if y ** 2 + t * y + n == 0:
            Y = y
            get_mt(W, Z, Y)


def get_Z():
    global W, Z, Y, T, N, t, n
    T = GF_256(1)
    N = W
    for i in range(GF_256.order):
        z = GF_256(i)
        if z ** 2 + T * z + N == 0:
            Z = z
            get_Y()


def get_ans():
    global W, Z, Y, T, N, t, n
    for i in range(GF_256.order):
        w = GF_256(i)
        if w ** 2 + w + GF_256(1) == 0:
            W = w
            get_Z()


'''
获得同构矩阵及其逆
[(g7 * W + g6) * Z + (g5W + g4)]Y + [(g3 * W + g2) * Z + (g1W + g0)] =
g7 * W * Z * Y + g6 * Z * Y + g5 * W * Y + g4 * Y + g3 * W * Z + g2 * Z + g1 * W + g0
'''
def get_isomorphic_matrix():
    get_ans()
    return target_ls


