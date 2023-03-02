m = input()
n = int(m)
a = []
if m == '1':
    print(m)
else:
    while n != 1:
        if n %2 ==0:
            n = n //2
        else:
            n = n*3+1
        a.append(n)

    print(' '.join(str(i) for i in a[::-1])+' '+str(m))