import galois


'''
确定 T,N,t,n 时，判断 GF(2^8)/GF(2^4) 和 GF(2^4)/GF(2^2) 下的两个多项式是否不可约
'''

def check_param():
    GF_4 = galois.GF(2 ** 2, repr='poly')
    GF_16 = galois.GF(2 ** 4, repr='poly')

    T, N = GF_4(1), GF_4(0b10)
    print("In GF(2^2), T,N =", T, N)

    # 判断 z^2 + T * z + N 在 GF(2^2) 是否可约
    flag = False
    for i in range(GF_4.order):
        z = GF_4(i)
        if z ** 2 + T * z + N == 0:
            flag = True
            break
    if not flag:
        print("OK, [z^2 + T * z + N] is irreducible")
    else:
        print("Error parameters, [z^2 + T * z + N] is reducible")

    T, N = GF_16(T), GF_16(N)
    # 在 GF(2^4) 上找到 z^2 + T * root + N 的两个解
    root = []
    for i in range(GF_16.order):
        Z = GF_16(i)
        if Z ** 2 + T * Z + N == 0:
            root.append(Z)
    print("|root| =", len(root))

    # 判断 y^2 + t * y + n 在 GF(2^4) 是否可约
    flag = False
    for Z in root:
        t = GF_16(1)    # t = 1
        n = GF_16(0b1001)   # n = N * Z + 1
        for i in range(GF_16.order):
            y = GF_16(i)
            if y**2 + t * y + n == 0:
                flag = True
                break
        if flag:
            break
    if not flag:
        print("OK, [y^2 + t * y + v] is irreducible")
    else:
        print("Error parameters, [y^2 + t * y + n] is reducible")


if __name__ == '__main__':
    check_param()
