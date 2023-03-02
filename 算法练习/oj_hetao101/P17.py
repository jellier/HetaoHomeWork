# http://oj.hetao101.com/d/hetao/p/17
# # 有n个小鱿鱼围成一个圆圈，从12点开始，顺时针把它们编号为1，2，3，4，5…n。从1号小鱿鱼开始顺时针报数，每逢报到m的小鱿鱼就放生。下一位小鱿鱼再次从1开始报数。请输出留到最后的小鱿鱼的编号。
# #
# # 输入格式
# # 2行，第一行是小鱿鱼的数量n，第二行是幸运数字m
#
# # 如 输入：
# # 10
# # 3
# # 输出：4


# 以下均为80分答案

n = int(input())
m = int(input())

c=list(i for i in range(1,n+1))
while True:
    # ==把前m个人删掉==
    # 先把前m-1个人放到后面
    for i in range(m-1):
        c.append(c[0])
        c.pop(0)
    # 再把第m个人删掉
    c.pop(0)

    # 当人数为1，输出编号
    if len(c) == 1:
        break
print(*c)
# print(c) 打出来的是列表，用*


# n = int(input())
# m = int(input())
# l = 0 # 放生的数量
# k = 0 #计数器
# c =[]
# for i in range(n):
#     c.append(i+1)
#
# # 留下的数量>1
# while n-l>1:
#     for i in range(len(c)):
#         if c[i] != 0:
#             k += 1
#             if k == m:
#                 k = 0
#                 c[i] = 0
#                 l += 1
#                 if n-l == 1:
#                     break
#         else:
#             continue
#
# for i in c:
#     if i !=0:
#         print(i)
#         break