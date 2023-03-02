s = [int(i) for i in input().strip('\r').split()]
s.pop(-1)
s = s[::-1]
print(" ".join(str(i) for i in s))
