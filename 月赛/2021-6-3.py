t = int(input())
n = [0]*t
l = [0]*t
num = 1
def sortList(lis):
    global num

    dist_list = sorted(lis)
    if dist_list == lis:
        return 0
    min_num = min(lis)
    idx = lis.index(min_num)
    if idx != 0:
        lis[0],lis[idx] = lis[idx],lis[0]
        new_lis = lis[1:]

        sortList(new_lis)
        num += 1
    return num

for i in range(t):
    n[i] = int(input())
    l[i] = input().split(' ')

for i in range(t):
    print(sortList(l[i]))
