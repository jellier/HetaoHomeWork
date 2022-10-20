row = int(input())
col = 0
a = []
num = 0

def findStr(a,b):
    l_a = len(a)
    l_b = len(b)
    n = 0
    c = 0

    # c 代表索引值，所以要-1
    while c + l_b - 1 < l_a:
        if a[c:c + l_b] == b:
            n += 1
        c += 1
    return n


def calNum(l):
    global num
    for item in l:
        temp_s = ''
        for i in item:
            temp_s += str(i)
        num += findStr(temp_s, '2022')

# 生成二维列表
for i in range(row):
    s = input()
    col = len(s)
    temp =[]
    for ss in s:
        temp.append(int(ss))
    a.append(temp)


# 生成纵向的二维列表
b =list(map(list,zip(*a)))
#
# 生成斜向的二维列表
def djx_l(ll):
    if not ll:
        return []
    row = len(ll)
    col = len(ll[0])
    col2 = col
    result = []
    for i in range(row):
        for j in range(col2 - 1, -1, -1): #j倒序遍历
            lst = []
            i1,j1 = i,j
            while i1 <= row - 1 and j1 <= col - 1:
                lst.append(ll[i1][j1])
                j1 += 1
                i1 += 1
            result.append(lst)
            if i == 0 and j == 0:
                col2 = 1
    return(result)


calNum(a)
calNum(b)
calNum(djx_l(a))

print(num)


#====test===
# a = [[1,2,3],[4,5,6],[7,8,9]]
# 横向2个，纵向1个，斜向2个
a = [[2,0,2,2,0,2,2],
     [0,0,0,0,0,0,0],
     [2,0,2,0,0,0,0],
     [2,0,0,2,0,0,0],
     [0,0,0,0,0,0,0],
     [0,0,0,0,0,2,0],
     [0,0,0,0,0,0,2]]

## 对角线从右往左
# def djx_r(lst:list):
#     lst_result = []
#     m = len(lst)
#     start = 0
#     for j in range(m):
#         for i in range(start,m):
#             lst1 = []
#             i1,j1 = i,j
#             while i1>=0 and j1<=i:
#                 lst1.append(lst[i1][j1])
#                 i1 -= 1
#                 j1 += 1
#             while len(lst1) != m:
#                 lst1.append(0)
#             lst_result.append(lst1)
#         #当进行到（lst[m-i][0],0)开头时，固定i为m-1
#         if i == m-1 and j == 0:
#             start = m-1
#     return lst_result
# print(djx_r(a))
#
## 对角线从左往右
# def djx_l(ll):
#     if not ll:
#         return []
#     row = len(ll)
#     col = len(ll[0])
#     col2 = col
#     result = []
#     for i in range(row):
#         for j in range(col2 - 1, -1, -1): #j倒序遍历
#             lst = []
#             i1,j1 = i,j #i1,j1用于方便同一对角线元素的添加，否则改变i,j影响开头元素的选择
#             while i1 <= row - 1 and j1 <= col - 1:
#                 lst.append(ll[i1][j1])
#                 j1 += 1
#                 i1 += 1
#             result.append(lst)
#             if i == 0 and j == 0:#当遍历完(0,0)开头的一条对角线后，让j固定为0
#                 col2 = 1
#     return(result)
#
# print(djx_l(a))
#
#
