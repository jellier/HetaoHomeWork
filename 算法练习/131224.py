n,m = [int(i) for i in input().split(' ')]
# lis = [True]* (n+1)
lis = [True]* (n+1)
for i in range(1,m +1):
    for j in range(1, n+1):
        if j % i == 0:
            lis[j] = not lis[j]

for i,j in enumerate(lis):
    if lis[i] == False:
        print(i,end=' ')