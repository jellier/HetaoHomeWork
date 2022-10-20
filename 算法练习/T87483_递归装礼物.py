# 有点类似数学里的抽屉原理
# 可以转化为整数n的m种划分
m,n = [int(i) for i in input().split(' ')]


def q(n, m):
    if n < 1 or m < 1:
        #不符合实际情况
        return 0
    if n == 1 or m == 1:
        return 1
    if n < m:
        #m不能大于n
        return q(n, n)
    if n == m:
        # 动规思想，正整数n的划分由n1=n的划分和n1<=n-1的划分组成
        return q(n,m-1)+1
        #动规思想，正整数n最大加数n1不大于m的划分由n1 = m的划分和n1 <= m - 1的划分组成
    return q(n,m-1)+q(n-m,m)
sum =0
for i in range(1,m+1):
    sum +=q(n,m)
print(sum)