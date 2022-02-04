
def main():
    
    n, m = readIntArr()
    
    # userStories = [[] for _ in range(m)] # userStories[user] = [stories]
    storyCreator = [-1 for _ in range(n)] # storyCreator[story] = user
    for story in range(n):
        u = int(input())
        u -= 1 # 0-indexing
        # userStories[u].append(story)
        storyCreator[story] = u
    
    p, q = readIntArr()
    # userfollowers = [[] for _ in range(m)] # userfollowers[i] = [users who follows i]
    userfollowing = [set() for _ in range(m)] # userfollowing[i] = [users i follows]
    for _ in range(p):
        i, j = readIntArr()
        i -= 1; j -= 1
        userfollowing[i].add(j)
        # userfollowers[j].append(i)
    
    storyfollowers = [[] for _ in range(n)] # storyfollowers[story] = [follower]
    followsStory = [set() for _ in range(m)] # followsStory[user] = [stories]
    for _ in range(q):
        i, k = readIntArr()
        i -= 1; k -= 1
        storyfollowers[k].append(i)
        followsStory[i].add(k)
    
    followsMap = [[False for _ in range(n)] for __ in range(n)] # for calcA
    # followsMap[i][j] = True if ui follows stories created by uj
    for story in range(n):
        j = storyCreator[story]
        for i in storyfollowers[story]:
            followsMap[i][j] = True
    
    shareStories = [[False for _ in range(n)] for __ in range(n)] # for calcA
    for arr in storyfollowers:
        z = len(arr)
        for i in range(z):
            for j in range(i + 1, z):
                shareStories[arr[i]][arr[j]] = True
                shareStories[arr[j]][arr[i]] = True
    
    
    def calcA(i, j):
        if i == j: return 0
        elif j in userfollowing[i]: return 3
        
        # check if ui follows stories created by uj
        if followsMap[i][j]:
            return 2
        # for story in followsStory[i]:
        #     if storyCreator[story] == j:
        #         return 2
        
        # check if ui follows stories followed by uj
        if shareStories[i][j]:
            return 1
        # for story in followsStory[i]:
        #     if story in followsStory[j]:
        #         return 1
        
        return 0
    
    def calcB(j, k):
        if storyCreator[k] == j: return 2
        if k in followsStory[j]: return 1
        return 0
    
    userStoryScore = [[] for _ in range(m)] # userStoryScore[user] = [(story, score), ...]
    
    for user in range(m):
        for story in range(n):
            if storyCreator[story] == user or story in followsStory[user]:
                score = -1
            else:
                score = 0
                for user2 in range(m):
                    score += calcA(user, user2) * calcB(user2, story)
            userStoryScore[user].append((story, score))
    
    for user in range(m):
        arr = userStoryScore[user]
        arr.sort(key = lambda x : (-x[1], x[0]))
        # print('user:{} arr:{}'.format(user, arr))
        arr2 = []
        for i in range(3):
            arr2.append(arr[i][0] + 1)
        oneLineArrayPrint(arr2)
    
    # for uj in range(m):
    #     print('uj:{} a:{} b:{}'.format(uj, calcA(0, uj), calcB(uj, 6)))
    
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