n = int(input())
lis = [' '] * n
severList = [' '] * n
clientList = {}
resultList = [' '] * n

for i in range(n):
    lis[i] = input()

def isAdCorrect(ad):
    if ':' not in ad:
        return False
    if ad.count('.') != 3:
        return False
    # 冒号前的字符
    f_m = ad.split(':')[0]
    # 冒号后的字符
    b_m = ad.split(':')[1]

    # 冒号后
    if not b_m.isdigit():
        return False
    elif int(b_m) < 0 or int(b_m) > 65535:
        return False
    elif len(b_m) > 1 and b_m[0] == '0':
        return False
    # 冒号前
    f_lis = f_m.split('.')
    f_f = True
    for _item in f_lis:
        if not _item.isdigit():
            f_f = False
            break
        elif int(_item) < 0 or int(_item) > 255:
            f_f = False
            break
        elif len(_item) > 1 and _item[0] == '0':
            f_f = False
            break

    if f_f == False:
        return False

    return True

def findServer():
    s = -1
    for i in range(len(severList)):
        if severList[i] != ' ':
            s = i
            severList[i] = ' '
    if s >= 0:
        return s + 1
    else:
        return 'FAIL'

for i in range(n):
    item = lis[i]
    op = item.split(' ')[0]
    ad = item.split(' ')[1]
    _rul = ' '
    if isAdCorrect(ad) == False :
        _rul = 'ERR'
    elif op == 'Server':
        if ad in severList:
            _rul = 'FAIL'
        else:
            severList[i] = ad
            _rul = 'S:'+ ad
    elif op == 'Client':
        if ad not in clientList:
            _rul = findServer()
            clientList[ad] = _rul
        else:
            _rul = clientList[ad]

    resultList[i] = _rul

for i in resultList:
    print(i)

