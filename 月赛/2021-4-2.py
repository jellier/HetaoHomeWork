ipt = input().split()
# y, m, w = int(ipt[0]), int(ipt[1]), int(ipt[2])
y, m, w = [int(i) for i in ipt]

day31 = [1, 3, 5, 7, 8, 10, 12]
day30 = [4, 6, 9, 11]


def get_year(y):
    if y % 400 == 0 or (y % 4 == 0 and y % 100 != 0):
        _day = 29
    else:
        _day = 28
    return _day


if m == 2:
    day = get_year(y)
elif m in day31:
    day = 31
elif m in day30:
    day = 30

a = [0] * day

for i in range(day):
    a[i] = w
    w += 1
    if w == 8:
        w = 1

print(a.count(6) + a.count(7))
