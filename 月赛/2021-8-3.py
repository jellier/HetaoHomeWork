
def get_lcm(x, y):
    if x > y:
        max = x
    else:
        max = y
    while True:
        if max % x == 0 and max % y == 0:
            lcm = max
            break
        max += 1

    return lcm

s = input().split(' ')
f1 = s[0]
f2 = s[1]
f1_zi = int(f1.split('/')[0])
f1_mu = int(f1.split('/')[1])
f2_zi = int(f2.split('/')[0])
f2_mu = int(f2.split('/')[1])

lcm_mu = get_lcm(f1_mu,f2_mu)
f1_xishu = lcm_mu // f1_mu
f2_xishu = lcm_mu // f2_mu
new_f1_zi = f1_zi * f1_xishu
new_f2_zi = f2_zi * f2_xishu

new_fenzi = new_f1_zi + new_f2_zi
new_fenmu = lcm_mu

if new_fenzi % new_fenmu == 0:
    print(new_fenzi // new_fenmu)
else:
    print(str(new_fenzi)+'/'+str(new_fenmu))
