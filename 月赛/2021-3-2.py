n = int(input())
list_url =['http://hetao101.com']
now_url = list_url[0]
b_url = ''
f_url = ''
list_index = 0

def findWeizhi(_str):
    _idx = list_url.index(_str)
    return _idx


def getNewArray(_str):
    _idx = findWeizhi(_str)
    return list_url[0:_idx+1]


for i in range(n):
    _tmp = input()

    if 'http' in _tmp:
        b_url = now_url
        now_url = _tmp
        f_url = ''
        list_url = getNewArray(b_url)
        list_url.append(now_url)
    else:
        if _tmp == 'B':
            f_url = now_url
            now_url = b_url
            list_index -= 1
            b_url = list_url[list_index]

        elif _tmp == 'F':
            b_url = now_url
            now_url = f_url
            list_index += 1
            f_url = list_url[list_index]

print(now_url)
