# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,233。。。。
# 斐波那契的传统解法：递归
# N超过40就贼慢，会超时。提交答案第2个测试点就会挂
# n = int(input())
# def louti(n):
#     num = 0
#     if n<=2:
#         num = n
#     else:
#         num += louti(n-1)+louti(n-2)
#     return num
# print(louti(n))

# 用递推
n = int(input())
def louti(n):
    a = 1
    b = 1
    if n <= 1:
        return n
    else:
        # 可以直接用while，但 n=0时过不去
        while n > 1:
            c = a + b
            a = b
            b = c
            n -= 1
        return b

print(louti(n))
