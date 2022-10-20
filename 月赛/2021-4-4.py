n = input().split()
coin,soldier = [int(i) for i in n]
a = input().split()
list_a = [int(i) for i in a]
len_a = len(a)

sum = 0
for i in list_a:
    sum += i

num = 0
# 差尽量平均
dis = (sum-coin) // len_a
mod1 = (sum-coin) % len_a


if mod1 == 0:
    for i in range(len_a):
        num += dis ** 2
else:
    for i in range(mod1):
        num += (dis+1)**2
    for i in range(len_a - mod1):
        num += dis**2
print(num)
