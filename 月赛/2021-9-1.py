n,m = [int(i) for i in input().split(' ')]
lis = [[0]*m]*n
for i in range(n):
    ipt = [int(k) for k in input().split(' ')]
    lis[i] = ipt

def isFront(a,b):
    # 1为在前面，0为在后面
    flag = 1
    for i in range(n):
        idx_a = lis[i].index(a)
        idx_b = lis[i].index(b)
        # 索引大，说明在后面，循环退出
        if idx_a > idx_b:
            flag = 0
            break
    return flag


cnt = [0]*m
for i in range(m):
    for j in range(i,m):
        if lis[0][i]!=lis[0][j]:
            if isFront(lis[0][i],lis[0][j]) == 1:
                cnt[i] += 1
sum = 0
for i in cnt:
    sum += i
print(sum)