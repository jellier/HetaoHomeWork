# NOIP真题
# 考察点较多，求质数、字符出现次数
def isPrime(n):
    if n == 0 or n == 1:
        return False
    flag = True
    # range(2, n)也可以
    for i in range(2, n//2+1):
        if n % i == 0:
            flag = False
            break
    return flag

s = input().strip('\r')
l = len(s)
list_a = [0]*l
for i in range(l):
    list_a[i] = s.count(s[i])
maxn = max(list_a)
minn=min(list_a)
dif = maxn - minn
if isPrime(dif):
    print('Lucky Word')
    print(dif)
else:
    print('No Answer')
    print(0)