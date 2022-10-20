tmp=[]
tmp2=[]
flag = 0


def isDup(strs):
    global flag
    lens = len(strs)
    i = 0
    while i < lens:
        j = i + 1
        while j < lens:
            if strs[j] == strs[i]:
                # tmp.append(strs[j])
                tmp2.append(i)
                flag = 1
            j += 1
        i += 1


def findSub(_idxs,_string):

    _len = len(_string)
    for c in _idxs:
        idx = c
        # idx = 2, 4, 5, 9, 10, 11, 14
        for i in range(1,_len+1):
            tmp_s = _string[idx:i]
            # print(tmp_s)
            cnt = _string.count(tmp_s)
            if cnt > 1:
                tmp.append(tmp_s)

    return list(set(tmp))
def theLong(stringlist):
    ml = max(len(s) for s in stringlist)
    return list(set(s for s in stringlist if len(s) == ml))

str = input()
isDup(str)

if flag == 1:
    lis = findSub(tmp2,str)
    # print(lis)
    lis = theLong(lis)
    print(sorted(lis)[0])
else:
    print('So Sad!')

