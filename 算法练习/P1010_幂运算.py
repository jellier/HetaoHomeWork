# 137 = 2**7 + 2**3 + 2**0
# 方次用括号来表示,137 可表示为 2(7)+2(3)+2(0)
# 思路1：幂次方的题，要看数据范围，根据范围可以暴力枚举 2**10=1024 2**14=16384 2**15 = 32768
# 如果数据 <=20000，说明幂最大为14
# 思路2：幂运算 pow(10, 2)=100; 幂运算的逆运算为对数运算 math.log(100,10)=2.0
import math
# print(pow(10, 2))
# print(math.log(100,10))

def f(n):
    if n ==1:
        return '2(0)'
    elif n == 2:
        return '2'
    elif n == 3:
        return '2+2(0)'
    y = int(math.log(n,2)) # 取最接近n的幂值
    tmp = 2 ** y
    if tmp == n:
        return '2('+f(y)+')'
    else:
        return '2('+f(y)+')+'+f(n-tmp)


n = int(input())
print(f(n))

# 思路三：位运算
