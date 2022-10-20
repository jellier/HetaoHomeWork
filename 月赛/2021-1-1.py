a = int(input())
list_a = input().split(' ')
# 第一次没得分仍然是没有把字符串转成数字就max的问题，同第2题的错误
list_a = [int(i) for i in list_a]
maxI = max(list_a)

count = 0
for i in list_a:
    i = int(i)
    if i == maxI:
        continue
    elif i < maxI:
        count += maxI - i

print(count)