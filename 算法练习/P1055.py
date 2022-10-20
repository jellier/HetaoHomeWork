ipt = input().strip('\r')
isbn_c = ipt[-1]
ff = ipt[0:-1]
isbn_f = ff.replace('-','')
l = len(isbn_f)
sum = 0
for i in range(l):
    tmp = int(isbn_f[i])*(i+1)
    sum += tmp
x = sum % 11

if x == 10:
    if isbn_c == 'X':
        print('Right')
    else:
        print(ff + 'X')

else:
    if str(x) == isbn_c:
        print('Right')
    else:
        print(ff + str(x))
