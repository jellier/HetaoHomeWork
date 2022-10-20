# 方法一，用字典
a = int(input())
list_a = input().split(' ')
dic = {}
for i in range(len(list_a)):
    dic[i + 1] = list_a[i]
# 之前的错误是没有给value转成数字，导致排序时，'10'会排到'2'前面，小于10个数时发现不了此问题
dic2 = {int(value): key for key, value in dic.items()}

for i in sorted(dic2.keys()):
    print(dic2[i], end=" ")
# 方法二，用列表
# a = int(input())
# list_a = input().split(' ')
# list_b = [0 for i in range(a+1)]
# num = 1
# for i in list_a:
#     list_b[int(i)] = num
#     num +=1
#
# for n in range(1,len(list_b)):
#     print(list_b[n],end=' ')