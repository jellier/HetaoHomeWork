n, k = [int(i) for i in input().split(' ')]

a = [0]*n
l,r =0,0
tmp = 0

for i in range(n):
    a[i] = float(input())*100
    tmp += a[i]
r = tmp//k+1


while r-l > 1e-4:
    mid = (l+r)/2

    tmp = 0
    for i in range(n):
        tmp = tmp + a[i]//mid
    if tmp < k:
        r = mid
    else:
        l = mid


t = int(r*1.00)/100
print(t)


