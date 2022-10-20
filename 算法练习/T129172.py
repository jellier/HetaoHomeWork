n = int(input())
ipt = input().split(' ')
lis = [int(i) for i in ipt]
maxx = max(lis)
minn = min(lis)
lis.remove(maxx)
lis.remove(minn)
sum = 0
for i in range(len(lis)):
    sum += lis[i]
print(sum // len(lis))