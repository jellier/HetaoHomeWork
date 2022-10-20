# 100分的答案，借助列表存储遍历过的字符，
# 先检查遍历过的，再检查未遍历的
s = input().strip('\r')
l = len(s)
flag =0
visited = []
for i in range(l):
    c = s[i]
    if c not in visited:
        visited.append(c)
        if c not in s[i+1:]:
            print(c)
            flag = 1
            break
if flag == 0:
    print('no')
# 仍然30分的答案，换汤不换药，仍然使用for + s.count
# s = input().strip('\r')
# l = len(s)
# flag = 0
#
#
# def find_c(r_start, r_stop):
#     for i in range(r_start, r_stop):
#         if s.count(s[i]) == 1:
#             return s[i]
#     return ''
#
# c = ''
# for i in range(l // 10 + 1):
#     c = find_c(i * 10, i * 10 + 9)
#     if c != '':
#         print(c)
#         flag = 1
#         break
#
# if flag == 0:
#     print('no')


# 30分的答案
# s = input().strip('\r')
# flag = 0
# for i in s:
#     if s.count(i) == 1:
#         print(i)
#         flag = 1
#         break
# if flag == 0:
#     print('no')
