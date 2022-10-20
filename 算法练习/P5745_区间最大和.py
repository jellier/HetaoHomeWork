n, m = [int(i) for i in input().split(' ')]
a = [0]*n
s = input().split(' ')
for i in range(n):
    a[i] = int(s[i])

# 用下面这种方法会RE
# a = [int(i) for i in input().split(' ')]
#
ans1, ans2, ans3 = 0, 0, 0

for i in range(n):
    for j in range(i, n):
        a_sum = 0
        for k in range(i, j+1):
            a_sum += a[k]

        if a_sum > ans3 and a_sum <= m:
            ans1 = i
            ans2 = j
            ans3 = a_sum
print(ans1+1,ans2+1,ans3)
