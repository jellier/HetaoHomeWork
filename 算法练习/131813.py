n= int(input())
def isHui(n):
    s = str(n)
    l = len(s)
    if l == 1:
        return True
    else:

        flag =True
        for i in range(0,l//2):
            if s[i] != s[-(i+1)]:
                flag = False
                break
        return flag

cnt = 0
for i in range(1,n+1):
    if isHui(i):
        cnt += 1
print(cnt)