card = input()
allow_int = '0123456789'
allow_last = '0123456789x'


def is_day_right(y,m,d):
    day_right = True
    if d <= 0 or d>31:
        day_right = False
    else:
        m_31 = [1,3,5,7,8,10,12]
        m_30 = [4,6,9,11]
        if (m in m_30) and d == 31:
            day_right = False
        elif m == 2:
            if d > 29:
                day_right = False
            else:
                if not((y % 4 == 0 and y % 100 != 0) or y % 400 == 0) and d ==29:
                    day_right = False

    return day_right

if len(card) == 18:
    is_right = True
    for idx,num in enumerate(card):
        if idx == 17:
            # 校验最后一位
            if num not in allow_last:
                print('最后1位错误')
                is_right = False
        else:
            if num not in allow_int:
                print('前17位错误')
                is_right = False
                break
    year = int(card[6:10])
    month = int(card[10:12])
    day = int(card[12:14])
    if year < 1900 or year >2100:
        print('年信息非法')
        is_right = False
    elif month <= 0 or month > 12:
        print('月信息非法')
        is_right = False
    elif not is_day_right(year,month,day):
        print('日信息非法')
        is_right = False
    if is_right:
        print('合法')

else:
    print('长度非法')