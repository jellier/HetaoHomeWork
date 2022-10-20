
lis_c = [0]*26
s = ''
# 输入
for i in range(4):
    s += input().strip('\r')

# 统计字符个数
for i in s:
    ord_i = ord(i)
    if 65 <= ord_i <= 90:
        idx = ord_i-65
        lis_c[idx] += 1
max_num = max(lis_c)
# 将*和空格拼全，与最大值找齐
lis = ['']*26
for i in range(26):
    dis = max_num - lis_c[i]
    lis[i] = ' '*dis + '*' * lis_c[i]

for i in range(max_num):
    for j in range(26):
        if j == 25:
            print(lis[j][i],end='')
        else:
            print(lis[j][i], end=' ')
    print()
# 打印最后一行
for i in range(65, 91):
    if i == 90:
        print(chr(i))
    else:
        print(chr(i), end=' ')