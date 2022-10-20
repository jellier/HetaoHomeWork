# 第一次没通过是用了数组，太大，超时
n = int(input().strip('\r'))
cnt = 0
s = ''
for a in range(1,4):
    for b in range(1,4):
        for c in range(1,4):
            for d in range(1,4):
                for e in range(1,4):
                    for f in range(1,4):
                        for g in range(1,4):
                            for h in range(1,4):
                                for i in range(1,4):
                                    for j in range(1,4):
                                        if a+b+c+d+e+f+g+h+i+j == n:
                                            s += str(a)+' '+str(b)+' '+str(c)+' '+str(d)+' '+str(e)+' '+str(f)+' '+str(g)+' '+str(h)+' '+str(i)+' '+str(j)+'\n'
                                            cnt += 1
if cnt > 0:
    print(cnt)
    print(s.strip('\n'))
else:
    print(0)