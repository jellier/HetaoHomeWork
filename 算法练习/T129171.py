n = int(input())
ipt = input().split(' ')
lis = [int(i) for i in ipt]
setlis = set(lis)
maxx = max(setlis)
setlis.remove(maxx)
nextx = max(setlis)
print(nextx)