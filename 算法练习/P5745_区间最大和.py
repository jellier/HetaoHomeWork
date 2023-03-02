n, m = [int(i) for i in input().split(' ')]
a = [0] * (n + 1)
s = input().split(' ')
for i in range(n):
    a[i + 1] = int(s[i])
# 用下面这种方法会RE
# a = [int(i) for i in input().split(' ')]
#
# 解法一
# ans1, ans2, ans3 = 0, 0, 0
#
# for i in range(n):
#     for j in range(i, n):
#         a_sum = 0
#         for k in range(i, j+1):
#             a_sum += a[k]
#
#         if a_sum > ans3 and a_sum <= m:
#             ans1 = i
#             ans2 = j
#             ans3 = a_sum
# print(ans1+1,ans2,ans3)

# 解法二--使用队列，C++能到满分，python只能到60
i, j, ansi, ansj = 1, 1, 1, 1
ansmax = 0
a_sum = 0
while i <= n:
    while j <= n and a_sum + a[j] <= m:
        a_sum = a_sum + a[j]
        j += 1
        if a_sum <= m and a_sum > ansmax:
            ansmax = a_sum
            ansi = i
            ansj = j - 1
    a_sum -= a[i]
    i += 1

print(ansi, ansj, ansmax)
