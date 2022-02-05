
from types import GeneratorType
def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

def main():
    
    n = int(input())
    adj = [[] for _ in range(n)]
    for _ in range(n - 1):
        x, y, d = readIntArr()
        x -= 1; y -= 1
        adj[x].append((y, d))
        adj[y].append((x, d))
    
    cs = []
    rs = []
    for i in range(n):
        c, r = readIntArr()
        cs.append(c); rs.append(r)
    
    dist = [0] * n # path from 0 to i
    
    path = [] # prev nodes
    minCost = [1e18] * n
    minCost[0] = 0
    @bootstrap
    def dfs(u, d, par):
        dist[u] = d
        
        for prev in path:
            minCost[u] = min(minCost[u], minCost[prev] + rs[prev] + cs[prev] * (d - dist[prev]))
            
        path.append(u)
        for v, dd in adj[u]:
            if v != par:
                yield dfs(v, d + dd, u)
        path.pop()
        yield None
    
    dfs(0, 0, -1)
    minCost.pop(0)
    oneLineArrayPrint(minCost)
    
    return


import sys
input=sys.stdin.buffer.readline #FOR READING PURE INTEGER INPUTS (space separation ok)
# input=lambda: sys.stdin.readline().rstrip("\r\n") #FOR READING STRING/TEXT INPUTS.

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