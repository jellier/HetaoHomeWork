ipt = input().split()
n,m = [int(i) for i in ipt]
a = [0]*2000000
t = input().split()
for i in range(m):
    a[i]=int(t[i])
b = a[:m]
c = sorted(b)
print(c)
