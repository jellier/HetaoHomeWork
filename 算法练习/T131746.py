# 统计数字字符个数
# In: Peking University is set up at 1898
# Out: 4
s = input().strip('\r')
cnt = 0
for i in s:
    if i.isdigit():
        cnt += 1
print(cnt)