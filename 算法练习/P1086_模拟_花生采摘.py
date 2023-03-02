m,n,t = [int(i) for i in input().split()]
a = [[0 for col in range(n+1)] for row in range(m+1)]
for i in range(m):
    a[i+1] = [int(j) for j in input().split()]

b = [{'num':0,'x':1,'y':1}]*(m*n)
k=1
for i in range(1,m+1):
    for j in range(n):
        temp = a[i][j]
        if temp > 0:
            b[k]['num'] = temp
            b[k]['x'] = i
            b[k]['y'] = j
            k += 1

print(b)

