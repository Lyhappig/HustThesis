from typing import List


def get_bit(x: int, i: int) -> int:
    return (x >> i) & 1


def get_bit_list(x: int) -> List[List[int]]:
    ret = [[]]
    for i in range(7, -1, -1):
        ret[0].append(get_bit(x, i))
    return ret


def get_num(nums: List[int], bits: int) -> int:
    ret = 0
    for num in nums:
        ret <<= bits
        ret |= num
    return ret
