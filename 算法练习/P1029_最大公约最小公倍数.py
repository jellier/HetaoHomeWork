ipt = input().split()
x, y = [int(i) for i in ipt]
s = 0
def gongyueshu(n,m):
    # 获取最小值
    if n > m:
        small = m
    else:
        small = n

    for i in range(1, small + 1):
        if n % i == 0 and m % i == 0:
            tmp = i
    return tmp
for i in range(x,y+1):
    P = i
    Q = int(x * y / P)
    if gongyueshu(P,Q) == x and  P * Q/ gongyueshu(P,Q) == y:
        s +=1

print(s)