# 洛谷有些题目输入的数据末尾有一个\r
# 所以input()后要使用split()
# split()也会把它当作分隔符从而去掉它，但是会获得一个列表
# 如果题目不需要split()，就使用strip()去掉这个东西

n = input().strip('\r')
sum = 0
for i in n:
    sum += int(i)
print(sum)