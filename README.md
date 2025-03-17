# SM4量子电路设计与实现

## 经典电路

### 步骤一

1. `test/sm4_sbox.py` 验证了 SM4 代数结构的正确性；
2. `test/param_chosen.py` 验证塔域结构下四个参数的取值是否合法。

### 步骤二

1. `utils/tower_basis_normal.py` 验证了 Canright 论文中 AES 的指定正规基的同构矩阵正确性；
2. 确定四个参数对应的不可约多项式后，`utils/tower_basis_poly.py` 获得本研究中的多个同构矩阵；
3. 代入同构矩阵后，`utils/check_sbox.py` 验证塔域结构下对应运算是否能得到 S 盒

### 步骤三

1. GF4, GF16, GF256 是对 `utils/check_sbox.py` 下塔域运算的层次拆解；
2. `GF16/gf16.py` 包含了 GF(16) 求逆运算通过 SAT 得到的布尔表达式，`GF256/gf256.py` 包含了 GF(256) 中各个运算采用最小线性逻辑组合算法求出的布尔表达式；
3. `GF256/inverse1.py`, `GF256/inverse2.py`, `GF256/inverse3.py` 是数字电路根据不同算法优化的布尔表达式，验证 S 盒的正确性；
4. `GF256/inverse4.py` 由 inverse1 的数字电路转化为量子电路，模拟了 Clifford+T 门集的运算，并验证 S 盒的正确性；

## 量子电路

1. `linear/check.py` 验证了 Xiang 等人基于矩阵分解的算法，对线性变换矩阵构造可逆逻辑电路；
2. `quantum` 目录下根据塔域的不同运算构建量子电路，并未对所有运算作出整合；
3. `quantum/cpp` 目录下主要使用 C++ 程序模拟 Clifford+T 量子电路。 