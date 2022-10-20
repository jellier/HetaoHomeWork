# 输入1：
# To
# to be or not to be is a question
# 输出1：
# 2 0

# 输入1：
# to
# Did the Ottoman Empire lose its power at that time
# 输出1：
# -1

word = input().lower()
sentense = input().lower()
s = sentense.split(' ')
c = 0
for w in s:
    if w == word:
        c += 1
if c > 0:
    t = ' ' + word + ' '
    idx = sentense.index(t)+1
    print(c, idx)
else:
    print(-1)

