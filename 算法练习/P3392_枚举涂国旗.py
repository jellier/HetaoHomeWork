# 思路：先做预处理，再枚举
# lis_w[i]/lis_b[i]/lis_r[i] 分别代表把前i行 都变成某种颜色的成本
# 设第1-i行是白色，第 i+1 行到第j行是蓝色， 第 j+1行到第n行是红色
# 枚举就要从 白色[i]+(蓝色[j]-蓝色[i])+ (红色[n]-红色[j])

ipt = input().strip('\r').split(' ')
n,m = [int(i) for i in ipt]
# lis_n =[]
lis_w = [0]*51
lis_b = [0]*51
lis_r = [0]*51

def notThisColor(s,c):
    t = 0
    for i in range(m):
        if s[i] != c:
            t += 1
    return t

# step1.预处理
# 从第1行开始算，第0行都是0
for i in range(1, n+1):
    s = input().strip('\r')
    # lis_n.append(s)
    lis_w[i] = lis_w[i-1] + notThisColor(s, 'W')
    lis_b[i] = lis_b[i-1] + notThisColor(s, 'B')
    lis_r[i] = lis_r[i-1] + notThisColor(s, 'R')

# step2.枚举
# cnt记录最小值，最大的次数也就是 N*M,将它设为初始值
cnt = 50 * 50
for i in range(1,n-1):
    for j in range(i+1,n):
        num = lis_w[i]+(lis_b[j]-lis_b[i])+(lis_r[n]-lis_r[j])
        if num < cnt:
            cnt = num
print(cnt)



