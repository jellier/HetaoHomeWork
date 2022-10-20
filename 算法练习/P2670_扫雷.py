# 扫雷游戏是一款十分经典的单机小游戏。在n行m列的雷区中有一些格子含有地雷（称之为地雷格），其他格子不含地雷（称之为非地雷格）。玩家翻开一个非地雷格时，该格将会出现一个数字——提示周围格子中有多少个是地雷格。游戏的目标是在不翻出任何地雷格的条件下，找出所有的非地雷格。
# 现在给出n行m列的雷区中的地雷分布，要求计算出每个非地雷格周围的地雷格数。
# 注：一个格子的周围格子包括其上、下、左、右、左上、右上、左下、右下八个方向上与之直接相邻的格子。
# 如：输入：
# 3 3
# *??
# ???
# ?*?
# 则：输出：
# *10
# 221
# 1*1
# 输入

n, m = [int(i) for i in input().split(' ')]
a = [['' for col in range(m+2)] for row in range(n+2)]
b = [[0 for col in range(m+2)] for row in range(n+2)]

for i in range(1,n+1):
    _s = input()
    for j in range(1,m+1):
        a[i][j] = _s[j-1]
print(a)
print(b)
# 计算
for i in range(1,n+1):
    for j in range(1, m+1):
        if a[i][j] == '*' :

            # 上一行
            b[i - 1][j - 1] += 1
            b[i - 1][j] += 1
            b[i - 1][j + 1] += 1

            # 当前行
            b[i][j - 1] += 1
            b[i][j] = -1
            b[i][j + 1] += 1

            # 下一行
            b[i + 1][j - 1] += 1
            b[i + 1][j] += 1
            b[i + 1][j + 1] += 1

print(b)

# 输出
for i in range(1,n+1):
    for j in range(1,m+1):
        if b[i][j] == -1:
            print('*', end='')
        else:
            print(b[i][j], end='')
    print()
