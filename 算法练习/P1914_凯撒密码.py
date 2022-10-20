# 密码是由原文字符串（由不超过 50 个小写字母组成）中每个字母向后移动 n 位形成的。
# z 的下一个字母是 a，如此循环。他现在找到了移动前的原文字符串及 n，请你求出密码。
# 思路：
# 1、ASCII码解法：z-122,a-97，Z-90，A-65

n = int(input())
s = input()
new_s = ''
for i in s:
    ord_s = ord(i)
    ord_s += n
    if ord_s > ord('z'):
        ord_s = ord_s % ord('z') + (ord('a')-1)
    new_s += chr(ord_s)

print(new_s)

