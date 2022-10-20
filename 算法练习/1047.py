# 一维数组，有重叠
l, m = [int(i) for i in input().split(' ')]
# 注意：这里要开 l+1 个数组，否则index out of range
tree = [0]*(l+1)

for i in range(m):
    u, v = [int(i) for i in input().split(' ')]
    for j in range(u, v+1):
        tree[j] = 1

print(tree.count(0))