# https://www.luogu.com.cn/problem/P1996 约瑟夫问题
# 约瑟夫的正常解法应该是循环链表，或者循环队列

# 题目描述
# n个人围成一圈，从第一个人开始报数,数到 m 的人出列，再由下一个人重新从 1 开始报数，数到 m 的人再出圈，依次类推，直到所有的人都出圈，请输出依次出圈人的编号。
#
# 注意：本题和《深入浅出-基础篇》上例题的表述稍有不同。书上表述是给出淘汰 n−1 名小朋友，而该题是全部出圈。
# 输入：10 3  输出：3 6 9 2 7 1 8 5 10 4

ipt = input().split()
n, m = [int(i) for i in ipt]
l =0
k = 0
# 存放编号
c = []
a = [] # 存出圈的编号
for i in range(n):
    c.append(i+1)
while len(a) != n:
    for i in range(len(c)):
        if c[i] != 0:
            k += 1
            if k == m:
                k =0
                a.append(c[i])
                c[i] = 0

                if len(a) == n:
                    break
s =''
for i in a:
    s += str(i) + ' '
print(s.strip(' '))








# 以下为80分答案
# # 有n个小鱿鱼围成一个圆圈，从12点开始，顺时针把它们编号为1，2，3，4，5…n。从1号小鱿鱼开始顺时针报数，每逢报到m的小鱿鱼就放生。下一位小鱿鱼再次从1开始报数。请输出留到最后的小鱿鱼的编号。
# #
# # 输入格式
# # 2行，第一行是小鱿鱼的数量n，第二行是幸运数字m
#
# # 如 输入：
# # 10
# # 3
# # 输出：4
#
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
