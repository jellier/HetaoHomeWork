

# 以下代码能过，但只有20分，会TLE
# 题解里面大多是这个思路，C++可以全部AC
n,m = [int(i) for i in input().split()]

# 生成一个n*n 的二维列表
multilist = [[0 for col in range(n)] for row in range(n)]

def changeList(x1,y1,x2,y2):
    for i in range(x1,x2+1):
        for j in range(y1,y2+1):
            multilist[i][j] += 1

for m in range(m):
    x1,y1,x2,y2 = [int(j) for j in input().split()]
    changeList(x1-1,y1-1,x2-1,y2-1)

for i in range(n):
    print(" ".join(str(i) for i in multilist[i]))