n = int(input())
s = [int(i) for i in input().split(' ')]
for i in range(n):
    if i+1 not in s:
        print(i+1)