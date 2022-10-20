ipt = input().split()
n,m = [int(i) for i in ipt]
ipt_a = input().split()
a = [int(i) for i in ipt_a]

sum = 0
for i in range(m):
    sum += n // a[i]

# if n == m and a.count(n) == m:
if sum >= n:
    print('Inf')
else:
    # n 记录未喝的数量
    # num 记录已喝的数量
    num = 0
    card = [0]*len(a)
    while True:
        if n > 0:
            num += n
            for i in range(m):
                card[i] += n
            n = 0
            continue
        elif n == 0:
            flag = 0
            for i in range(m):
                # tmp记录当前种类的卡片能换的瓶数
                tmp = card[i]//a[i]
                if tmp > 0:
                    card[i] -= tmp * a[i]
                    n += tmp
                    flag = 1
            if flag == 0:
                break
    print(num)