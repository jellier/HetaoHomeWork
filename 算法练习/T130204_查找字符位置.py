
n,m = [int(i) for i in input().strip('\r').split(' ')]
lis = [int(j) for j in input().strip('\r').split(' ')]
for i in range(m):
    x = int(input().strip('\r'))
    if x in lis:
        print(lis.index(x)+1)
    else:
        print(-1)