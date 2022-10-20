pg = input().split(' ')
a = [int(i) for i in pg]
h = int(input())
num = 0
for i in a:
    if h+30 >= i:
        num += 1
print(num)

