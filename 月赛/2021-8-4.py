n,c = input().split(' ')
n = int(n)
c = int(c)
chapters = [' '] * n
for i in range(n):
    chapters[i] = input()

dic={}
names=[]
for i in chapters:
    info = i.split(' ')
    names.append(info[0])

names = list(set(names))
for i in names:
    dic[i]={}


for chap in chapters:
    info = chap.split(' ')
    name = info[0]
    chap_id = info[1]
    chap_time = info[2]
    if name in dic:
        dic[name][chap_id] = chap_time
        # print(dic['happy'])
for item in dic:
    for i in range(c+1,0,-1):
