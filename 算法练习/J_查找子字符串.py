# 输入两个字符串，输出第2个字符串在第一个字符串中出现的N个位置
# 样例：输入：fadsfa fa，输出：0 4
a, b = input().split(' ')
# print(a,b)
l_a = len(a)
l_b = len(b)

c = 0
flag = False
# c 代表索引值，所以要-1
while c + l_b -1< l_a:
    if a[c:c+l_b] == b:
        print(c, end=' ')
        flag = True
    c += 1

if not flag:
    print('No')