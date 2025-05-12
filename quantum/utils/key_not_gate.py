CK = [
        0x00070E15, 0x1C232A31, 0x383F464D, 0x545B6269,
        0x70777E85, 0x8C939AA1, 0xA8AFB6BD, 0xC4CBD2D9,
        0xE0E7EEF5, 0xFC030A11, 0x181F262D, 0x343B4249,
        0x50575E65, 0x6C737A81, 0x888F969D, 0xA4ABB2B9,
        0xC0C7CED5, 0xDCE3EAF1, 0xF8FF060D, 0x141B2229,
        0x30373E45, 0x4C535A61, 0x686F767D, 0x848B9299,
        0xA0A7AEB5, 0xBCC3CAD1, 0xD8DFE6ED, 0xF4FB0209,
        0x10171E25, 0x2C333A41, 0x484F565D, 0x646B7279
]

FK = [0xa3b1bac6, 0x56aa3350, 0x677d9197, 0xb27022dc]

if __name__ == '__main__':
    sum = 0
    for x in CK:
        binary_str = bin(x)[2:]
        count = binary_str.count('1')
        sum += count * 2
    for y in FK:
        binary_str = bin(y)[2:]
        count = binary_str.count('1')
        sum += count
    print(sum)
