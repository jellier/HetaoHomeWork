# 输入格式：第一行为数值i
# 接着的i行为需要输入的算式，每行可能有三个数据或两个数据。
# 若该行为两个数据，则表示本题的运算类型与上一题的运算类型相同，而这两个数据为运算数。
# 输出格式：输出2*i行。对于每个输入的算式，输出完整的运算式及结果，第二行输出该运算式的总长度

# 0分原因是没有.strip('\r')
# 70分原因是忽略了连续多个没有运算符的情况

n = int(input())
s = [' ']*n
for i in range(n):
    s[i] = input().strip('\r').split(' ')

def operate_me(op1, op2,opt):
    cnt = 0
    _s = ''
    _opt = ''
    if opt == 'a':
        cnt = int(op1) + int(op2)
        _opt = '+'
    elif opt == 'b':
        cnt = int(op1) - int(op2)
        _opt = '-'
    elif opt == 'c':
        cnt = int(op1) * int(op2)
        _opt = '*'

    _s = op1 + _opt + op2 + '=' + str(cnt)
    return _s

op = ''
for i in range(len(s)):
    item = s[i]

    rul = ''
    if len(item) == 3:
        rul = operate_me(item[1],item[2],item[0])
        op = item[0]
    else:
        rul = operate_me(item[0], item[1], op)
    print(rul)
    print(len(rul))
