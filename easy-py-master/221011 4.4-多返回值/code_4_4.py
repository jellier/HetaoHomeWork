# 获取教程、习题、案例，共同学习、讨论、打卡
# 请关注：Crossin的编程教室
# QQ群：155816967，微信：sunset24678

def 交换(a, b):
    temp = a
    a = b
    b = temp
    return a, b

x = '🐔'
y = '🏀'
x, y = 交换(x, y)
x, y = y, x
print(x, y)
