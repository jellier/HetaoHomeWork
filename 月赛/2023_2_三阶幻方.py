start, stop = [int(i) for i in input().strip('\r').split()]


a=[0]*3
for j in range(3):
    a[j]= [int(i) for i in input().strip('\r').split()]

# 求中心数和幻和
z_x_sh = (stop-start)//2+start
hh = z_x_sh * 3
sum = hh*3

if a[1][1]==0:
    a[1][1] = z_x_sh

def lis_sum(a):
    _sum = 0
    for i in range(3):
        for j in range(3):
            _sum += a[i][j]
    return _sum

while lis_sum(a) <sum:
    # 横着扫一遍
    for i in range(3):
        sum1 = a[i][0] + a[i][1] + a[i][2]
        # 数每行里面0的个数，找出有两个自然数的，填剩下的那个
        num0 = a[i].count(0)
        if num0 == 1:
            dif = hh - sum1
            for j in range(3):
                if a[i][j] == 0:
                    a[i][j] = dif

    # 竖着扫一遍
    for j in range(3):
        num0_col=0
        sum1 = a[0][j] + a[1][j] + a[2][j]
        if a[0][j] == 0:
            num0_col +=1
        if a[1][j] == 0:
            num0_col +=1
        if a[2][j] == 0:
            num0_col +=1
        if num0_col == 1:
            dif = hh - sum1

            for i in range(3):
                if a[i][j] == 0:
                    a[i][j] = dif

    # 斜着扫，左对角线和右对角线
    left_l = a[0][0] + a[1][1] +a[2][2]
    right_l = a[0][2] + a[1][1] +a[2][0]
    if left_l > start * 2 and left_l != hh:
        dif = hh - left_l
        if a[0][0]==0:
            a[0][0] = dif
        else:
            a[2][2] = dif
    if right_l > start * 2 and right_l != hh:
        dif = hh - right_l
        if a[0][2]==0:
            a[0][2] = dif
        else:
            a[2][0] = dif



for i in range(3):
    print(" ".join(str(i) for i in a[i]))


