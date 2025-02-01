import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils.matrix import GF2Matrix

M = [
    [1, 1, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 1, 1, 1],
    [1, 1, 0, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 0, 0, 0, 1]
]

TX = [
    [1, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 1],
    [0, 0, 1, 0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 0, 1, 1],
    [0, 1, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 0, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 1, 0, 1]
]

TMX = [
    [1, 0, 1, 0, 1, 1, 0, 0],
    [1, 1, 1, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 1, 1, 0],
    [1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 1],
    [0, 0, 1, 0, 1, 0, 1, 0]
]

def trans_matrix(A):
    R = [[0] * 8 for i in range(8)]
    l = 7
    for i in range(8):
        r = 7
        for j in range(8):
            R[l][r] = A[i][j]
            r -= 1
        l -= 1
    return R

def is_equal(A, B):
    for i in range(8):
        for j in range(8):
            if A[i][j] != B[i][j]:
                return False
    return True


if __name__ == "__main__":
    # gx = GF2Matrix(trans_matrix(TX))
    # gx_inv = gx.inverse()
    # gm = GF2Matrix(M)
    # mx = gm * gx_inv
    # MX = trans_matrix(TMX)
    # print(is_equal(mx.matrix, MX))
    #
    # poly_to_tower = gx
    # poly_to_tower.T()
    # print(poly_to_tower)
    #
    # tower_to_poly = gx_inv
    # tower_to_poly.T()
    # print(tower_to_poly)

