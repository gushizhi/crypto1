def left_shift(str, bit):
    return str[bit:] + str[:bit]

def convertFileToBinary(path):
    f = open(path,'rb')
    src = f.read()
    b = []
    for i in src:
        tmp = bin(ord(i))[2:]
        tmp = '0' * (8-len(tmp)) + tmp
        b.append(tmp)

    return ''.join(b)

def convertBinaryToFile(src, path):
    result = []
    for i in range(0, len(src), 8):
        result.append(chr(int(src[i:i+8], 2)))
    f = open(path, 'wb')
    f.write(''.join(result))
    f.close()

# Initial permutation
IP = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17,  9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7,
]

# Final permutation
FP = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41,  9, 49, 17, 57, 25,
]

# Permutation choice 1 for left side
PC1_left = [
    57, 49, 41, 33, 25, 17,  9,
     1, 58, 50, 42, 34, 26, 18,
    10,  2, 59, 51, 43, 35, 27,
    19, 11,  3, 60, 52, 44, 36,
]

# Permutation choice 1 for right side
PC1_right = [
    63, 55, 47, 39, 31, 23, 15,
     7, 62, 54, 46, 38, 30, 22,
    14,  6, 61, 53, 45, 37, 29,
    21, 13,  5, 28, 20, 12,  4,
]

# Permutation choice 2
PC2 = [
    14, 17, 11, 24,  1,  5,  3, 28,
    15,  6, 21, 10, 23, 19, 12,  4,
    26,  8, 16,  7, 27, 20, 13,  2,
    41, 52, 31, 37, 47, 55, 30, 40,
    51, 45, 33, 48, 44, 49, 39, 56,
    34, 53, 46, 42, 50, 36, 29, 32,
]

# Expansion
E = [
    32,  1,  2,  3,  4,  5,
     4,  5,  6,  7,  8,  9,
     8,  9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32,  1,
]

# S-boxes from 1 to 8
S1 = [
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
    [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
]
S2 = [
    [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
    [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
    [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
    [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
]
S3 = [
    [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
    [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
    [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
    [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
]
S4 = [
    [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
    [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
    [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
    [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
]
S5 = [
    [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
    [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
    [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
    [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
]
S6 = [
    [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
    [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
    [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
    [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
]
S7 = [
    [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
    [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
    [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
    [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
]
S8 = [
    [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
    [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
    [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
    [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
]
SBoxes = [S1, S2, S3, S4, S5, S6, S7, S8]

# Permutation
P = [
    16,  7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26,  5, 18, 31, 10,
     2,  8, 24, 14, 32, 27,  3,  9,
    19, 13, 30,  6, 22, 11,  4, 25,
]

def finalPermutate(s):
    fp = ""
    for i in range(64):
        fp += s[FP[i] - 1]
    return fp

def permutate(s):
    f = ""
    for i in range(32):
        f += s[P[i] - 1]
    return f

def getSubkeys(k):
    K_left = ""
    K_right = ""
    for i in PC1_left:
        K_left += k[i-1]
    for i in PC1_right:
        K_right += k[i-1]
    L = []
    R = []
    l = K_left
    r = K_right
    L.append(l)
    R.append(r)
    l = left_shift(l, 1)
    r = left_shift(r, 1)
    L.append(l)
    R.append(r)
    l = left_shift(l, 1)
    r = left_shift(r, 1)
    L.append(l)
    R.append(r)
    for i in range(6):
        l = left_shift(l, 2)
        r = left_shift(r, 2)
        L.append(l)
        R.append(r)
    l = left_shift(l, 1)
    r = left_shift(r, 1)
    L.append(l)
    R.append(r)
    for i in range(6):
        l = left_shift(l, 2)
        r = left_shift(r, 2)
        L.append(l)
        R.append(r)
    l = left_shift(l, 1)
    r = left_shift(r, 1)
    L.append(l)
    R.append(r)
    LR = []
    for i in range(17):
        LR.append(L[i] + R[i])
    subKeys = [""]*16
    for i in range(0, 16):
        key = ""
        for j in range(48):
            key += LR[i+1][PC2[j] - 1]
        subKeys[i] = key
    return subKeys

def getIP(m):
    ip = ""
    for i in range(64):
        ip += (m[IP[i]-1])
    return ip

def expand(r):
    e = ""
    for i in range(48):
        e += r[E[i]-1]
    return e

def XOR(x, y):
    return '{1:0{0}b}'.format(len(x), int(x, 2) ^ int(y, 2))

def func(r, k):
    e = expand(r)
    B = XOR(e, k)
    Bi = [""] * 8
    for i in range(8):
        Bi[i] = B[i*6:i*6+6]
    Sresult = ""
    for k in range(8):
        sbox = SBoxes[k]
        b = Bi[k]
        i = b[0] + b[5]
        j = b[1:5]
        p = sbox[int(i, 2)][int(j, 2)]
        st = [str(x) for x in bin(p)[2:]]
        Sresult += "0" * (4 - len(st))
        for x in st:
            Sresult += x
    return permutate(Sresult)

def DES(m="0000000100100011010001010110011110001001101010111100110111101111", k="0001001100110100010101110111100110011011101111001101111111110001", decrypt=False):
    subKeys = getSubkeys(k)
    if decrypt == True:
        subKeys = subKeys[::-1]
    ip = getIP(m)
    l = ip[0:32]
    r = ip[32:]
    for i in range(16):
        ln = r
        rn = XOR(l, func(r, subKeys[i]))
        l = ln
        r = rn
    return finalPermutate(r + l)

def encrypt(bin_input):
    num = int(len(bin_input) / 64)

    encrypted_blocks = []

    for i in range(num):
        block = bin_input[i*64:i*64+64]
        en = DES(m=block)
        encrypted_blocks.append(en)
    num_zeroes = (64 - len(bin_input) % 64)
    last = "0" * num_zeroes + bin_input[(num)*64:]
    encrypted_blocks.append(DES(m=last))
    
    return (encrypted_blocks, num_zeroes)

def decrypt(encrypted_blocks, num_zeroes):
    total_decrypted = ""
    for e in encrypted_blocks[:-1]:
        mes = DES(m=e, decrypt=True)
        total_decrypted += mes
    e = encrypted_blocks[-1]
    mes = DES(m=e, decrypt=True)
    mes = mes[num_zeroes:]
    total_decrypted += mes
    return total_decrypted