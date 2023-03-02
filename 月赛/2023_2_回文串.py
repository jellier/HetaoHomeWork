# 第5个样例会超时，字符串特别长的时候，如何避免超时？
s = input().strip('\r')

def isHui(x):
    flag = True
    for i in range(len(x) // 2):
        if x[i] != x[-i - 1]:
            flag = False
            break
    return flag

l_s = len(s)
num = l_s
if l_s%2 ==0:
    stop = l_s-1
else:
    stop = l_s
# i 代表子字符串长度
for i in range(3,stop+1,2):
    #逐个获取子字符串
    for j in range(l_s):
        t_s = s[j:j+i]
        if len(t_s) == i:
            if isHui(t_s):
                num +=1

print(num)