# 获取教程、习题、案例，共同学习、讨论、打卡
# 请关注：Crossin的编程教室
# QQ群：155816967，微信：sunset24678


宽度 = 6
高度 = 4
# 1
for i in range(高度):
    for j in range(宽度):
        print('*', end="")
    print()

# 2
for i in range(宽度*高度):
    print('*', end="")
    if (i + 1) % 宽度 == 0:
        print()

# 3
for i in range(高度):
    print('*'*宽度)

# 4
print((('*'*宽度)+'\n')*高度)