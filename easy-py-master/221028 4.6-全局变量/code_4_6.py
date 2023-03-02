# 获取教程、习题、案例，共同学习、讨论、打卡
# 请关注：Crossin的编程教室
# QQ群：155816967，微信：sunset24678


# 1
def 有个函数(x):
    print(y)
x = '🏀'
y = '🐔'
有个函数(x)


# 2
def 有个函数(x):
    global y
    print(y)
    y = '🎤'

x = '🏀'
y = '🐔'
有个函数(x)
print('全局变量y', y)


# 3
def 全局变量加1():
    global x
    x += 1
    return x
def 另外这个函数():
    global x
    x = 1
    y = 全局变量加1()
    print(x + y)
另外这个函数()
