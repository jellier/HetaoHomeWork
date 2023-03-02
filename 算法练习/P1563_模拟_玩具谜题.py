n,m = [int(i) for i in input().strip('\r').split()]
doll = [0]*n
for i in range(n):
    t = input().split()
    t_dic = {'head':int(t[0]),'job':t[1]}
    doll[i] = t_dic
# print(doll)

now = 0
for i in range(m):
    x,y = [int(i) for i in input().strip('\r').split()]
    if (doll[now]['head'] == 0 and x ==0) or (doll[now]['head'] == 1 and x ==1):
        now = (now + n - y) % n
    elif (doll[now]['head'] == 0 and x ==1) or (doll[now]['head'] == 1 and x ==0):
        now = (now + y) % n

print(doll[now]['job'])