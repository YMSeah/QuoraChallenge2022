
def getCumuXor(m): # return 1 ^ 2 ^ ... m
    # 1 ^ 2 ^ ... (4x - 1) = 0
    u = ((m + 1) // 4) * 4 - 1
    ans = 0
    for i in range(u + 1, m + 1):
        ans ^= i
    return ans

def chk(m, removeCnt): # check if can get xor of 0 after removing removeCnt
    xor = getCumuXor(m)
    if removeCnt == 0 and xor == 0: return []
    if removeCnt == 1:
        if 1 <= xor <= m:
            return [xor]
    if removeCnt == 2:
        for i in range(1, m):
            j = i ^ xor
            if i < j <= m:
                return [i, j]
    if removeCnt == 3:
        for i in range(1, m):
            for j in range(i + 1, m):
                k = i ^ j ^ xor
                if j < k <= m:
                    return [i, j, k]
    if removeCnt == 4:
        for i in range(1, m):
            for j in range(i + 1, m):
                for k in range(j + 1, m):
                    l = i ^ j ^ k ^ xor
                    if k < l <= m:
                        return [i, j, k, l]
    return -1 # impossible

def solve(n):
    # m is between [n, n + 4]
    for m in range(n, n + 5):
        res = chk(m, m - n)
        if res != -1:
            return m, res

def solve3(n): # n % 4 == 3
    m = n
    omit = []
    return (m, omit)

def solve0(n): # n % 4 == 0
    m = n + 1
    omit = [1]
    return (m, omit)

def solve1(n): # n % 4 == 1
    # it could be 1, some power of 2, some other number
    xor = getCumuXor(n + 3)
    z = 4
    while z <= n + 3:
        y = 1 ^ z ^ xor
        if y <= n + 3 and y != 1 and y != z:
            m = n + 3
            omit = list(sorted([1, z, y]))
            return (m, omit)
        z *= 2
    
    # else, it is 1, 2, 4, 6
    if n + 4 >= 6 and getCumuXor(n + 4) == 1:
        m = n + 4
        omit = list(sorted([1, 2, 4, 6]))
        return (m, omit)
    
    assert False

def solve2(n): # n % 4 == 2
    # it could be a power of 2 and some other number
    xor = getCumuXor(n + 2)
    z = 2
    while z <= n + 2:
        y = z ^ xor
        if y != z and 1 <= y <= n + 2:
            m = n + 2
            omit = list(sorted([y, z]))
            return (m, omit)
        z *= 2
    
    # else, it is 2, 4, some other number
    xor = getCumuXor(n + 3)
    other = xor ^ 2 ^ 4
    assert 1 <= other <= n + 3
    m = n + 3
    omit = list(sorted([2, 4, other]))
    return (m, omit)

def solveFast(n):
    if n % 4 == 0:
        m, omit = solve0(n)
    if n % 4 == 1:
        m, omit = solve1(n)
    if n % 4 == 2:
        m, omit = solve2(n)
    if n % 4 == 3:
        m, omit = solve3(n)
    return (m, omit)

def main():
    
    # m = 24
    # numbers = list(range(1, m + 1))
    
    # zeroArrs = []
    
    # for mask in range(1 << m):
    #     arr = []
    #     for i in range(m):
    #         if (mask & (1 << i) > 0):
    #             arr.append(numbers[i])
    #     bwXor = 0
    #     for x in arr:
    #         bwXor ^= x
    #     if bwXor == 0:
    #         zeroArrs.append(arr)
    # # print(zeroArrs)
    
    # from collections import defaultdict
    # zeroByLen = defaultdict(lambda : [])
    # for arr in zeroArrs:
    #     if arr:
    #         zeroByLen[max(arr)].append(arr)
    
    # # for n in range(1, m + 1):
    # #     print('n:{} arrs:{}'.format(n, zeroByLen[n]))
    
    # minM = defaultdict(lambda: [999999]) # {length:arr with min Max value}
    # for arr in zeroArrs:
    #     if arr and max(arr) < max(minM[len(arr)]):
    #         minM[len(arr)] = arr
    # ans = [-1] * (40)
    # for k, v in minM.items():
    #     ans[k] = v
    
    # for n, x in enumerate(ans):
    #     print('n:{} arr:{}'.format(n, x))
    
    
    # for n in range(3, 1000):
    #     m1, omit1 = solve(n)
    #     m2, omit2 = solveFast(n)
    #     assert m1 == m2
    #     assert len(omit2) == m2 - n
    #     assert len(omit2) == len(set(omit2))
        
    #     arr = list(range(1, m2 + 1))
    #     xor = 0
    #     for i in arr:
    #         if i not in omit2:
    #             xor ^= i
    #     if xor != 0:
    #         print('n:{} m:{} omit1:{} omit2:{} xor:{}'.format(n, m2, omit1, omit2, xor))
    
    n = int(input())
    m, omit = solveFast(n)
    print(m)
    oneLineArrayPrint(omit)
    
    return

# n:0 arr:-1
# n:1 arr:-1
# n:2 arr:-1
# n:3 arr:[1, 2, 3]
# n:4 arr:[2, 3, 4, 5]
# n:5 arr:[3, 4, 6, 8, 9]
# n:6 arr:[1, 2, 4, 6, 8, 9]
# n:7 arr:[1, 2, 3, 4, 5, 6, 7]
# n:8 arr:[2, 3, 4, 5, 6, 7, 8, 9]
# n:9 arr:[2, 3, 4, 5, 7, 8, 9, 10, 12]
# n:10 arr:[1, 2, 3, 4, 5, 6, 8, 9, 10, 12]
# n:11 arr:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
# n:12 arr:[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# n:13 arr:[1, 2, 3, 4, 5, 6, 7, 9, 10, 12, 14, 16, 17]
# n:14 arr:[1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 17]
# n:15 arr:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# n:16 arr:[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
# n:17 arr:[1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 13, 14, 16, 17, 18, 20]
# n:18 arr:[1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20]
# n:19 arr:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
# n:20 arr:[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
# n:21 arr:[2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20, 21, 22, 24]
# n:22 arr:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 24]
# n:23 arr:[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]

import sys
# input=sys.stdin.buffer.readline #FOR READING PURE INTEGER INPUTS (space separation ok)
input=lambda: sys.stdin.readline().rstrip("\r\n") #FOR READING STRING/TEXT INPUTS.

def oneLineArrayPrint(arr):
    print(' '.join([str(x) for x in arr]))
def multiLineArrayPrint(arr):
    print('\n'.join([str(x) for x in arr]))
def multiLineArrayOfArraysPrint(arr):
    print('\n'.join([' '.join([str(x) for x in y]) for y in arr]))
 
def readIntArr():
    return [int(x) for x in input().split()]
# def readFloatArr():
#     return [float(x) for x in input().split()]
 
def makeArr(defaultValFactory,dimensionArr): # eg. makeArr(lambda:0,[n,m])
    dv=defaultValFactory;da=dimensionArr
    if len(da)==1:return [dv() for _ in range(da[0])]
    else:return [makeArr(dv,da[1:]) for _ in range(da[0])]
 
def queryInteractive(a, b, c):
    print('? {} {} {}'.format(a, b, c))
    sys.stdout.flush()
    return int(input())
 
def answerInteractive(ansArr):
    print('! {}'.format(' '.join([str(x) for x in ansArr])))
    sys.stdout.flush()
 
inf=float('inf')
# MOD=10**9+7
# MOD=998244353

from math import gcd,floor,ceil
import math
# from math import floor,ceil # for Python2
 
for _abc in range(1):
    main()