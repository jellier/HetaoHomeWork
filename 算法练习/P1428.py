# 递归-诚哥
res = []
def fun(array):
    if len(array) == 0:
        return
    x = array[-1]
    count = 0
    for i in array:
        if i < x:
            count += 1
    res.append(count)
    fun(array[:-1])

n = int(input())
arr = [int(i) for i in input().split()]

fun(arr)
for i in res[::-1]:
    print(i, end=' ')
# 普通方式
# n = int(input())
# ipt = input().split(' ')
# lis = [int(i) for i in ipt]
#
# count =[] * len(lis)
# for i in range(len(lis)):
#     now = lis[i]
#     cnt = 0
#     for j in range(i):
#         if now > lis[j]:
#             cnt += 1
#     count.append(cnt)
# for i in count:
#     print(i,end=' ')

# 递归没搞定

# def cutefish(idx):
#     if idx == 0:
#         return 0
#
#     if lis[idx] > lis[idx -1]:
#         cnt += 1
#         print(cnt)
#     return cutefish(idx - 1)
#
#
# s = []
# for i in range(n):
#     s.append(cutefish(i))
#
# print(s)

