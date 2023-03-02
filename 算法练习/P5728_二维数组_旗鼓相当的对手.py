import math
m = int(input())
# 以下这个赋值方式有问题，但不知道为啥有问题
# m_lis = [{'y':0,'s':0,'e':0,'totle':0}]*m
# for i in range(m):
#     t = [int(j) for j in input().split()]
#     m_lis[i]['y'] = t[0]
#     m_lis[i]['s'] = t[1]
#     m_lis[i]['e'] = t[2]
#     m_lis[i]['totle'] = t[0]+t[1]+t[2]

m_lis = [0]*m
for i in range(m):
    t = [int(j) for j in input().split()]
    tmp = {'y':t[0],'s':t[1],'e':t[2],'totle':t[0]+t[1]+t[2]}
    m_lis[i] = tmp

num = 0
for i in range(m):
    a = m_lis[i]
    for j in range(i+1,m):
        b = m_lis[j]
        if abs(a['totle'] - b['totle']) <= 10:
            if abs(a['y'] - b['y']) <= 5 and abs(a['s'] - b['s']) <= 5 and abs(a['e'] - b['e']) <= 5:
                # print(abs(a['y'] - b['y']),abs(a['s'] - b['s']))
                num += 1
print(num)


