import math
n = int(input())
prList =[]


def getNumLen(n):
    p = 1
    while n // math.pow(10,p) != 0:
        p += 1

    return p
m = getNumLen(n)


def getChildren(num):
    isPr = True
    i = 2
    square = int(math.sqrt(num)) + 1
    while i <= square:
        if num % i == 0:
            prList.append(i)
            isPr = False
            getChildren(num / i)
            i += 1
            break
        i += 1
    if isPr:
        prList.append(int(num))

getChildren(n)

print(str(n)+'=', end='')
# 正常输出
for idx, num in enumerate(prList):
    if idx == len(prList)-1:
        print(num)
    else:
        print(num, end='x')

# 有重复质因数的
mList_a = []
mList_b = []
for num in prList:
    cnt = prList.count(num)
    if cnt > 1:
        tmp = str(num)+'^'+str(cnt)
        mList_a.append(tmp)
    else:
        mList_b.append(num)

if len(mList_a)!=0:
    mList_a = list(set(mList_a))
    mList_a.sort()

    print(' '*m+'='+'x'.join(mList_a),end='')
    for idx, num in enumerate(mList_b):
        print('x'+str(num),end='')




