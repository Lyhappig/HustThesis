import numpy as np


class GF2Matrix:
    def __init__(self, data):
        """
        初始化 GF(2) 矩阵。
        :param data: 二维列表或 np.array，表示矩阵数据。
        """
        self.matrix = np.array(data) % 2  # 确保所有元素在 GF(2) 上

    def __str__(self):
        """
        返回矩阵的字符串表示。
        """
        return str(self.matrix)

    def __add__(self, other):
        """
        重载加法运算符，实现 GF(2) 上的矩阵加法。
        """
        if self.matrix.shape != other.matrix.shape:
            raise ValueError("矩阵形状不匹配，无法相加")
        return GF2Matrix((self.matrix + other.matrix) % 2)

    def __mul__(self, other):
        """
        重载乘法运算符，实现 GF(2) 上的矩阵乘法。
        """
        if self.matrix.shape[1] != other.matrix.shape[0]:
            raise ValueError("矩阵不匹配，无法相乘")
        return GF2Matrix(np.dot(self.matrix, other.matrix) % 2)

    def T(self):
        self.matrix = self.matrix.T

    def inverse(self):
        """
        计算 GF(2) 上的矩阵逆。
        如果矩阵不可逆，抛出 ValueError。
        """
        n = self.matrix.shape[0]
        if self.matrix.shape[0] != self.matrix.shape[1]:
            raise ValueError("非方阵不可逆")

        # 构造增广矩阵 [A | I]
        augmented_matrix = np.hstack((self.matrix, np.eye(n, dtype=int)))

        # 高斯消元法
        for i in range(n):
            # 找到第 i 列中第 i 行及以下第一个非零元素
            if augmented_matrix[i, i] == 0:
                for j in range(i + 1, n):
                    if augmented_matrix[j, i] == 1:
                        augmented_matrix[[i, j]] = augmented_matrix[[j, i]]  # 交换行
                        break
                else:
                    raise ValueError("矩阵不可逆")

            # 将第 i 行归一化
            if augmented_matrix[i, i] == 0:
                raise ValueError("矩阵不可逆")

            # 消去第 i 列的其他行
            for j in range(n):
                if j != i and augmented_matrix[j, i] == 1:
                    augmented_matrix[j] ^= augmented_matrix[i]

        # 提取逆矩阵
        inverse_matrix = augmented_matrix[:, n:]
        return GF2Matrix(inverse_matrix)


X1M = GF2Matrix([[0, 1, 1, 1, 1, 1, 1, 1],
                 [1, 1, 1, 1, 1, 0, 1, 1],
                 [1, 0, 1, 1, 1, 0, 1, 1],
                 [1, 0, 0, 1, 0, 0, 1, 1],
                 [1, 0, 0, 0, 1, 0, 1, 1],
                 [1, 0, 0, 1, 0, 1, 0, 0],
                 [0, 0, 1, 0, 0, 0, 1, 0],
                 [0, 0, 1, 0, 0, 0, 1, 1]])

X1C = GF2Matrix([[1],
                 [0],
                 [1],
                 [0],
                 [1],
                 [0],
                 [1],
                 [0]])

MX = GF2Matrix([[0, 0, 0, 0, 1, 0, 0, 1],
                [0, 1, 0, 1, 1, 1, 0, 1],
                [1, 1, 0, 1, 1, 1, 1, 0],
                [0, 0, 1, 1, 1, 1, 1, 0],
                [0, 0, 0, 0, 1, 0, 1, 1],
                [1, 0, 0, 1, 1, 0, 1, 0],
                [0, 0, 1, 1, 1, 0, 1, 1],
                [1, 0, 1, 0, 0, 1, 1, 1]])

C = GF2Matrix([[1],
               [1],
               [0],
               [1],
               [0],
               [0],
               [1],
               [1]])


def x(x):
    return x ^ 1


def cx(x, y):
    return x ^ y


def get_mtx(x):
    ans = [[0 for _ in range(8)]]
    for i in range(8):
        ans[0][i] = (x >> (7 - i)) & 1
    return GF2Matrix(ans)


def solve_qt1(x):
    b = [0 for _ in range(8)]
    for i in range(8):
        b[i] = (x >> (7 - i)) & 1
    b[7] = cx(b[6], b[7])
    b[6] = cx(b[2], b[6])
    b[5] = cx(b[0], b[5])
    b[0] = cx(b[7], b[0])
    b[7] = cx(b[2], b[7])
    b[4] = cx(b[0], b[4])
    b[0] = cx(b[3], b[0])
    b[2] = cx(b[3], b[2])
    b[3] = cx(b[5], b[3])
    b[2] = cx(b[4], b[2])
    b[1] = cx(b[2], b[1])
    b[5] = cx(b[1], b[5])
    b[0], b[3] = b[3], b[0]
    b[0], b[5] = b[5], b[0]
    b[0] ^= 1
    b[2] ^= 1
    b[4] ^= 1
    b[6] ^= 1
    return GF2Matrix([b])


def solve_qt10(x):
    a = [0 for _ in range(8)]
    for i in range(8):
        a[i] = (x >> (7 - i)) & 1
    a[2] = cx(a[6], a[2])
    a[4] = cx(a[7], a[4])
    a[3] = cx(a[4], a[3])
    a[1] = cx(a[5], a[1])
    a[2] = cx(a[3], a[2])
    a[5] = cx(a[2], a[5])
    a[0] = cx(a[7], a[0])
    a[7] = cx(a[5], a[7])
    a[0] = cx(a[3], a[0])
    a[5] = cx(a[0], a[5])
    a[0] = cx(a[6], a[0])
    a[6] = cx(a[4], a[6])
    a[3] = cx(a[1], a[3])
    a[1] = cx(a[0], a[1])
    a[0], a[4] = a[4], a[0]
    a[5], a[4] = a[4], a[5]
    a[7], a[4] = a[4], a[7]
    a[3], a[4] = a[4], a[3]
    a[1], a[4] = a[4], a[1]
    a[2], a[4] = a[4], a[2]
    a[6], a[4] = a[4], a[6]
    a[0] ^= 1
    a[1] ^= 1
    a[3] ^= 1
    a[6] ^= 1
    a[7] ^= 1
    return GF2Matrix([a])


def compare(A, C):
    for i in range(8):
        if A[0][i] != C[0][i]:
            return False
    return True


if __name__ == "__main__":
    for i in range(256):
        B = get_mtx(i)
        B.T()
        A1 = X1M * B + X1C
        A2 = MX * B + C
        A1.T()
        A2.T()
        C1 = solve_qt1(i)
        C2 = solve_qt10(i)
        if not compare(A1.matrix, C1.matrix):
            print("error")
            exit(-1)
        if not compare(A2.matrix, C2.matrix):
            print("error")
            exit(-1)
    print("OK")
