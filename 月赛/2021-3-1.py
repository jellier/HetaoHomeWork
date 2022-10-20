n = int(input())
list_a = input().split(' ')
list_a = [int(i) for i in list_a]
a = max(list_a, key=list_a.count)
print(a)
