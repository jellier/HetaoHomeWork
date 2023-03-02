n = int(input())
a = [int(i) for i in input().strip('\r').split()]
a.sort()

t = a[0]*2+a[1]*2+a[2]
print(t)