
def convToInt(ipv4Front):
    res = 0
    for x in ipv4Front.split('.'):
        res *= 256
        res += int(x)
    return res

def convToIpv4Front(num):
    arr = []
    for _ in range(4):
        arr.append(num % 256)
        num //= 256
    arr.reverse()
    return '.'.join(str(x) for x in arr)

def main():
    
    n = int(input())
    ranges = []
    for _ in range(n):
        arr = input().split('/')
        low = convToInt(arr[0])
        hi = low + (1 << (32 - int(arr[1])))
        ranges.append((low, hi))
    
    ranges.sort()
    st = []
    for x, y in ranges:
        xp = x
        while st and x <= st[-1][1]: # merge range
            xp, yp = st.pop()
        st.append((xp, y))
    
    twoPowers = []; b = 1; i = 0
    while b < (1 << 33):
        twoPowers.append((b, i))
        i += 1
        b *= 2
    twoPowers.reverse()
    # print(st)
    for lo, hi in st:
        front = convToIpv4Front(lo)
        x = lo
        for b, i in twoPowers:
            if x + b <= hi:
                print(front + '/' + str(32 - i))
                x += b
    
    return


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