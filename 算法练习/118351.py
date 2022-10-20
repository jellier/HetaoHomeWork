n = int(input())
t = 1
s = 0

def f(n):
    if n <= 2:
        return n
    return n * f(n-1)

while t <= n:
    s += f(t)
    t += 1
print(s)