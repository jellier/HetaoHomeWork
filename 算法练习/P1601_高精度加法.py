# a = input()
# b = input()
# print(int(a)+int(b))

# 以下解法为书中解法，但用python写出来会RE
a = list(input())[::-1]
b = list(input())[::-1]
# 用数组模拟高精度
l = max(len(a),len(b))
# 因为要考虑进位，所以数组c要开l+1的长度，否则下面c[i+1]的时候会超出索引
c = [0]*(l+1)
for i in range(l):
    c[i] +=int(a[i])+int(b[i])
    # 进位
    if c[i] >= 10:
        c[i+1] = c[i]//10
        c[i] = c[i] % 10

s = ''.join([str(i) for i in c[::-1]])
if s[0] == '0':
    s = s[1:]
print(s)
