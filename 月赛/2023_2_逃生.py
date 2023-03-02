
n = int(input().strip('\r'))
a = [int(i) for i in input().strip('\r').split()]
l = [-1]*n


# 存2所在位置的索引值
l_idx = [0]*(a.count(2))
m=0
for i in range(len(a)):
    if a[i] == 2:
        l_idx[m] = i
        m += 1

def getMin(idx):
    t = [0]* len(l_idx)
    for i in range(len(l_idx)):
        if l_idx[i]-idx>0:
            t[i] = l_idx[i]-idx
        else:
            t[i] = idx - l_idx[i]
    return min(t)

for idx,item in enumerate(a):
    if item == 2:
        l[idx] =0
    else:
        # 先算两头的
        if idx < l_idx[0]:
            l[idx] = l_idx[0]-idx
        elif idx > l_idx[-1]:
            l[idx] = idx - l_idx[-1]
        else:
            # 再算两侧都有2的
            l[idx] = getMin(idx)


print(" ".join(str(i) for i in l))