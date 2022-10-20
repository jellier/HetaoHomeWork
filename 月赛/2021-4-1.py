n = int(input())
sum = 1
tmp = 1
for i in range(2, n + 1):
    if i % 5 == 0 or i % 7 == 0:
        sum += 1
        tmp = 1
    else:
        tmp = tmp * 2
        sum += tmp

print(sum)
