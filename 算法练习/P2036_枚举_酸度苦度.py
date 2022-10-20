n = int(input())
lis = [[]]*n
for i in range(n):
    t = [int(i) for i in input().split(' ')]
    lis[i] = t

suan = 1
ku = 0
for i in range(n):
    suan *= lis[i][0]
    ku += lis[i][1]
if suan >= ku:
    dif = suan - ku
else:
    dif = ku - suan
print(dif)