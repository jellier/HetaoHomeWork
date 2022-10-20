# 字典按value排序

a = ['e', 'b', 'f', 'd']
b = [4, 2, 3, 7]
a_b = dict(zip(a, b))

# print(a_b)
#
#
# for item in a_b.items():
#     print(item)
# print('*****')

# 按key排序，使用字典的items()
sort_ab = sorted(a_b.items())
print(sort_ab)

# 按value排序，使用lambda
# sorted 的 key 参数，用于指定在进行比较之前对每个元素调用的函数(或其他可调用的函数)
sort_ab_2 = sorted(a_b.items(), key=lambda x: x[1])
print(sort_ab_2)

# 参考：
# https://blog.csdn.net/weixin_38739735/article/details/117005077