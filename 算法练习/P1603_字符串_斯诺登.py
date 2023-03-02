# 此题坑点在于读题，平方后都是两位数，小于10的前面补0
# 最后没有符合条件的，要输出0，否则测试点3过不去
s = input().strip('\r').split()
a = ['one','two','three','four','five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty']
b1=['a','another','first']
b2=['second','both']
b3=['third']

c=[0]*6
for idx,item in enumerate(s):
    if item in a:
        c[idx] = a.index(item)+1
    elif item in b1:
        c[idx] = 1
    elif item in b2:
        c[idx] = 2
    elif item in b3:
        c[idx] = 3

ss = ''
for item in c:
    if item != 0:
        t = item*item%100
        if t<10:
            ss+=str('0')+str(t)
        else:
            ss += str(t)
if ss == '':
    print(0)
else:
    print(int(ss))