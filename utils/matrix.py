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
