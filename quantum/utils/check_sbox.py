def get_bit(x, i):
    return (x >> i) & 1


def get_num(nums, i):
    ans = 0
    for x in nums:
        ans <<= i
        ans |= x
    return ans


'''
Stofflen方法得到的S盒
'''
def sbox1(alpha: int) -> int:
    t0, t1, t2, t3 = get_bit(alpha, 3), get_bit(alpha, 2), get_bit(alpha, 1), get_bit(alpha, 0)
    # Here
    # 输入
    a0 = t1 ^ t2
    a1 = t0 ^ t1
    a2 = t2 ^ t3
    a3 = t0 ^ t2
    a4 = t1 ^ t3
    a5 = t3
    b0 = t0
    # 非线性部分
    b1 = a0 ^ 1
    c0 = b0 & b1
    d0 = a0 ^ a5
    b2 = d0 ^ c0
    b3 = a1 ^ c0 ^ 1
    c1 = b2 & b3
    b4 = b3 ^ a2 ^ c1
    b5 = a0 ^ c1
    c2 = b4 & b5
    d1 = a3 ^ c2
    b6 = d1 ^ a5
    b7 = d0 ^ c2
    c3 = b6 & b7
    b8 = d1 ^ c0 ^ c1
    b9 = a1 ^ a5 ^ c1
    c4 = b8 & b9
    # 输出
    c5 = c2 ^ c3
    z0 = b2 ^ c5 ^ c4
    z1 = a4 ^ c2 ^ c4
    z2 = b4 ^ c3 ^ 1
    z3 = b3 ^ c5 ^ 1

    return get_num([z0, z1, z2, z3], 1)


t0, t1, t2, t3 = [0] * 4
c0, c1, c2, c3, c4 = [0] * 5


def x(a):
    return a ^ 1


def cx(nums, a):
    for i in nums:
        a ^= i
    return a


def ccx(a, b, c):
    return a * b ^ c


def sbox2(alpha: int):
    global t0, t1, t2, t3, c0, c1, c2, c3, c4
    t0, t1, t2, t3 = get_bit(alpha, 3), get_bit(alpha, 2), get_bit(alpha, 1), get_bit(alpha, 0)
    # part1
    t1 = x(t1)
    t1 = cx([t2], t1)
    c0 = ccx(t0, t1, c0)
    t1 = cx([t2], t1)
    t1 = x(t1)
    # part2
    c4 = cx([t1, t2], c4)
    c3 = cx([t2, t3], c3)
    t2 = cx([t1, t3, c0], t2)
    t1 = x(t1)
    t1 = cx([t0, c0], t1)
    c1 = ccx(t1, t2, c1)
    t1 = cx([c3, c1], t1)
    c4 = cx([c1], c4)
    c2 = ccx(t1, c4, c2)
    c4 = cx([c1], c4)
    t1 = cx([c3, c1], t1)
    t1 = cx([t0, c0], t1)
    t1 = x(t1)
    t2 = cx([t1, t3, c0], t2)
    c3 = cx([t2, t3], c3)
    c4 = cx([t1, t2], c4)
    # part3
    t0 = cx([t2, t3, c2], t0)
    t1 = cx([t2, t3, c2], t1)
    c3 = ccx(t0, t1, c3)
    t1 = cx([t2, t3, c2], t1)
    t0 = cx([t2, t3, c2], t0)
    # part4
    t2 = cx([t0, c0, c1, c2], t2)
    t1 = cx([t0, t3, c1], t1)
    c4 = ccx(t1, t2, c4)
    t1 = cx([t0, t3, c1], t1)
    t2 = cx([t0, c0, c1, c2], t2)
    # part5
    t0 = cx([c0, c3], t0)
    c0 = cx([t1, t2, t3, c2, c3, c4], c0)
    c4 = cx([t1, t3, c2], c4)
    c1 = cx([t0, t1, t2, t3], c1)
    c2 = cx([t0, t1], c2)


def sbox2_inv():
    global t0, t1, t2, t3, c0, c1, c2, c3, c4
    # part1
    c2 = cx([t0, t1], c2)
    c1 = cx([t0, t1, t2, t3], c1)
    c4 = cx([t1, t3, c2], c4)
    c0 = cx([t1, t2, t3, c2, c3, c4], c0)
    t0 = cx([c0, c3], t0)
    # part4
    t2 = cx([t0, c0, c1, c2], t2)
    t1 = cx([t0, t3, c1], t1)
    c4 = ccx(t1, t2, c4)
    t1 = cx([t0, t3, c1], t1)
    t2 = cx([t0, c0, c1, c2], t2)
    # part3
    t0 = cx([t2, t3, c2], t0)
    t1 = cx([t2, t3, c2], t1)
    c3 = ccx(t0, t1, c3)
    t1 = cx([t2, t3, c2], t1)
    t0 = cx([t2, t3, c2], t0)
    # part2
    c4 = cx([t1, t2], c4)
    c3 = cx([t2, t3], c3)
    t2 = cx([t1, t3, c0], t2)
    t1 = x(t1)
    t1 = cx([t0, c0], t1)
    t1 = cx([c3, c1], t1)
    c4 = cx([c1], c4)
    c2 = ccx(t1, c4, c2)
    c4 = cx([c1], c4)
    t1 = cx([c3, c1], t1)
    c1 = ccx(t1, t2, c1)
    t1 = cx([t0, c0], t1)
    t1 = x(t1)
    t2 = cx([t1, t3, c0], t2)
    c3 = cx([t2, t3], c3)
    c4 = cx([t1, t2], c4)
    # part1
    t1 = x(t1)
    t1 = cx([t2], t1)
    c0 = ccx(t0, t1, c0)
    t1 = cx([t2], t1)
    t1 = x(t1)


'''
Toffoli深度5，5个辅助量子比特
'''
def sbox3(alpha: int):
    global t0, t1, t2, t3, c0, c1, c2, c3, c4
    t0, t1, t2, t3 = get_bit(alpha, 3), get_bit(alpha, 2), get_bit(alpha, 1), get_bit(alpha, 0)
    # part1
    t1 = x(t1)
    t1 = cx([t2], t1)
    c0 = ccx(t0, t1, c0)
    t1 = cx([t2], t1)
    t1 = x(t1)
    # part2
    c4 = cx([t1], c4)
    c4 = cx([t2], c4)
    c3 = cx([t2], c3)
    c3 = cx([t3], c3)
    # t2 = cx([t1, t3, c0], t2)
    t2 = cx([t1], t2)
    t2 = cx([t3], t2)
    t2 = cx([c0], t2)
    t1 = x(t1)
    # t1 = cx([t0, c0], t1)
    t1 = cx([t0], t1)
    t1 = cx([c0], t1)
    c1 = ccx(t1, t2, c1)
    # t1 = cx([c3, c1], t1)
    t1 = cx([c3], t1)
    t1 = cx([c1], t1)
    c4 = cx([c1], c4)
    c2 = ccx(t1, c4, c2)
    c4 = cx([c1], c4)
    # t1 = cx([c3, c1], t1)
    t1 = cx([c3], t1)
    t1 = cx([c1], t1)
    # t1 = cx([t0, c0], t1)
    t1 = cx([t0], t1)
    t1 = cx([c0], t1)
    t1 = x(t1)
    # t2 = cx([t1, t3, c0], t2)
    t2 = cx([t1], t2)
    t2 = cx([t3], t2)
    t2 = cx([c0], t2)
    # c3 = cx([t2, t3], c3)
    c3 = cx([t2], c3)
    c3 = cx([t3], c3)
    # c4 = cx([t1, t2], c4)
    c4 = cx([t1], c4)
    c4 = cx([t2], c4)
    # part3
    # t0 = cx([t2, t3, c2], t0)
    t0 = cx([t2], t0)
    t0 = cx([t3], t0)
    t0 = cx([c2], t0)
    # t1 = cx([t2, t3, c2], t1)
    t1 = cx([t2], t1)
    t1 = cx([t3], t1)
    t1 = cx([c2], t1)
    c3 = ccx(t0, t1, c3)
    # t1 = cx([t2, t3, c2], t1)
    t1 = cx([t2], t1)
    t1 = cx([t3], t1)
    t1 = cx([c2], t1)
    # t0 = cx([t2, t3, c2], t0)
    t0 = cx([t2], t0)
    t0 = cx([t3], t0)
    t0 = cx([c2], t0)
    # part4
    # t2 = cx([t0, c0, c1, c2], t2)
    t2 = cx([t0], t2)
    t2 = cx([c0], t2)
    t2 = cx([c1], t2)
    t2 = cx([c2], t2)
    # t1 = cx([t0, t3, c1], t1)
    t1 = cx([t0], t1)
    t1 = cx([t3], t1)
    t1 = cx([c1], t1)
    c4 = ccx(t1, t2, c4)
    # t1 = cx([t0, t3, c1], t1)
    t1 = cx([t0], t1)
    t1 = cx([t3], t1)
    t1 = cx([c1], t1)
    # t2 = cx([t0, c0, c1, c2], t2)
    t2 = cx([t0], t2)
    t2 = cx([c0], t2)
    t2 = cx([c1], t2)
    t2 = cx([c2], t2)
    # part5
    # t0 = cx([c0, c3], t0)
    t0 = cx([c0], t0)
    t0 = cx([c3], t0)
    # c0 = cx([t1, t2, t3, c2, c3, c4], c0)
    c0 = cx([t1], c0)
    c0 = cx([t2], c0)
    c0 = cx([t3], c0)
    c0 = cx([c2], c0)
    c0 = cx([c3], c0)
    c0 = cx([c4], c0)
    # c4 = cx([t1, t3, c2], c4)
    c4 = cx([t1], c4)
    c4 = cx([t3], c4)
    c4 = cx([c2], c4)
    # c1 = cx([t0, t1, t2, t3], c1)
    c1 = cx([t0], c1)
    c1 = cx([t1], c1)
    c1 = cx([t2], c1)
    c1 = cx([t3], c1)
    # c2 = cx([t0, t1], c2)
    c2 = cx([t0], c2)
    c2 = cx([t1], c2)


a = [0] * 4
d = [0] * 15


'''
15 个辅助量子比特，9个Toffoli门，29个CNOT门，Toffoli深度为2
'''
def sbox4(alpha: int):
    global a, d
    # t0, t1, t2, t3 = get_bit(alpha, 3), get_bit(alpha, 2), get_bit(alpha, 1), get_bit(alpha, 0)
    a[3], a[2], a[1], a[0] = get_bit(alpha, 3), get_bit(alpha, 2), get_bit(alpha, 1), get_bit(alpha, 0)
    # d[0] = cx([a[3], a[2], a[1], a[0]], d[0])
    # d[1] = cx([a[1], a[0]], d[1])
    # d[2] = cx([a[3], a[1]], d[2])
    # d[3] = cx([a[2], a[0]], d[3])
    # d[4] = ccx(d[0], d[1], d[4])
    # d[5] = ccx(d[2], a[1], d[5])
    # d[6] = ccx(d[3], a[0], d[6])
    # d[6] = cx([d[4], a[2]], d[6])
    # d[5] = cx([d[4], a[2], a[3]], d[5])
    # d[2] = cx([a[3], a[1], d[6]], d[2])
    # d[3] = cx([a[2], a[0], d[5]], d[3])
    # d[1] = cx([d[0]], d[1])
    # a[1] = cx([a[3]], a[1])
    # a[0] = cx([a[2]], a[0])
    # d[7] = cx([d[6], d[5]], d[7])
    # d[8] = cx([d[6], d[5]], d[8])
    # d[9] = ccx(d[7], d[1], d[9])
    # d[10] = ccx(d[6], a[3], d[10])
    # d[11] = ccx(d[5], a[2], d[11])
    # d[12] = ccx(d[8], d[0], d[12])
    # d[13] = ccx(d[2], a[1], d[13])
    # d[14] = ccx(d[3], a[0], d[14])
    # d[9] = cx([d[11]], d[9])
    # d[10] = cx([d[11]], d[10])
    # d[12] = cx([d[14]], d[12])
    # d[13] = cx([d[14]], d[13])
    # d[0] = cx([a[3], a[2], a[1], a[0]], d[0])
    d[1] = cx([a[1]], d[1])
    d[1] = cx([a[0]], d[1])
    d[2] = cx([a[3]], d[2])
    d[2] = cx([a[1]], d[2])
    d[3] = cx([a[2]], d[3])
    d[3] = cx([a[0]], d[3])
    d[0] = cx([d[2]], d[0])
    d[0] = cx([d[3]], d[0])
    d[4] = ccx(d[0], d[1], d[4])
    d[5] = ccx(d[2], a[1], d[5])
    d[6] = ccx(d[3], a[0], d[6])
    d[6] = cx([d[4]], d[6])
    d[6] = cx([a[2]], d[6])
    d[5] = cx([d[4]], d[5])
    d[5] = cx([a[2]], d[5])
    d[5] = cx([a[3]], d[5])
    d[2] = cx([a[3]], d[2])
    d[2] = cx([a[1]], d[2])
    d[2] = cx([d[6]], d[2])
    d[3] = cx([a[2]], d[3])
    d[3] = cx([a[0]], d[3])
    d[3] = cx([d[5]], d[3])
    d[1] = cx([d[0]], d[1])
    a[1] = cx([a[3]], a[1])
    a[0] = cx([a[2]], a[0])
    d[7] = cx([d[6]], d[7])
    d[7] = cx([d[5]], d[7])
    d[8] = cx([d[7]], d[8])
    d[9] = ccx(d[7], d[1], d[9])
    d[10] = ccx(d[6], a[3], d[10])
    d[11] = ccx(d[5], a[2], d[11])
    d[12] = ccx(d[8], d[0], d[12])
    d[13] = ccx(d[2], a[1], d[13])
    d[14] = ccx(d[3], a[0], d[14])
    d[9] = cx([d[11]], d[9])
    d[10] = cx([d[11]], d[10])
    d[12] = cx([d[14]], d[12])
    d[13] = cx([d[14]], d[13])



def sbox4_inv():
    global a, d
    d[13] = cx([d[14]], d[13])
    d[12] = cx([d[14]], d[12])
    d[10] = cx([d[11]], d[10])
    d[9] = cx([d[11]], d[9])
    d[14] = ccx(d[3], a[0], d[14])
    d[13] = ccx(d[2], a[1], d[13])
    d[12] = ccx(d[8], d[0], d[12])
    d[11] = ccx(d[5], a[2], d[11])
    d[10] = ccx(d[6], a[3], d[10])
    d[9] = ccx(d[7], d[1], d[9])
    d[8] = cx([d[6], d[5]], d[8])
    d[7] = cx([d[6], d[5]], d[7])
    a[0] = cx([a[2]], a[0])
    a[1] = cx([a[3]], a[1])
    d[1] = cx([d[0]], d[1])
    d[3] = cx([a[2], a[0], d[5]], d[3])
    d[2] = cx([a[3], a[1], d[6]], d[2])
    d[5] = cx([d[4], a[2], a[3]], d[5])
    d[6] = cx([d[4], a[2]], d[6])
    d[6] = ccx(d[3], a[0], d[6])
    d[5] = ccx(d[2], a[1], d[5])
    d[4] = ccx(d[0], d[1], d[4])
    d[3] = cx([a[2], a[0]], d[3])
    d[2] = cx([a[3], a[1]], d[2])
    d[1] = cx([a[1], a[0]], d[1])
    d[0] = cx([a[3], a[2], a[1], a[0]], d[0])


if __name__ == '__main__':
    # for i in range(16):
    #     y1 = sbox1(i)
    #     c0 = c1 = c2 = c3 = c4 = 0
    #     sbox3(i)
    #     y2 = get_num([c0, c4, c1, c2], 1)
    #     sbox2_inv()
    #     j = get_num([t0, t1, t2, t3], 1)
    #     k = get_num([c0, c1, c2, c3, c4], 1)
    #     if y1 != y2 or i != j or k != 0:
    #         print("error")
    #         exit(-1)
    # print("OK")
    for i in range(16):
        y1 = sbox1(i)
        for j in range(15):
            d[j] = 0
        sbox4(i)
        y2 = get_num([d[9], d[10], d[12], d[13]], 1)
        sbox4_inv()
        k = get_num([a[3], a[2], a[1], a[0]], 1)
        for j in range(15):
            if d[j] != 0:
                print("error")
                exit(-1)
        if y1 != y2 or i != k:
            print("error")
            exit(-1)
    print("OK")
