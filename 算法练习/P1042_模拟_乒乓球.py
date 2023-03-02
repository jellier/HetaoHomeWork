# https://blog.csdn.net/weixin_45450206/article/details/123688365
# WWWWWWWWWWWWWWWWWWWWWWLW --其中 W表示华华获得一分，L 表示华华对手获得一分
# 11分制：WWWWWWWWWWW/WWWWWWWWWWW/LW  11:0/11:0/1:1
# 21分制：WWWWWWWWWWWWWWWWWWWWW/WLW   21:0/2:1
# 坑点：
# 1：输入过程中需要有换行，C++可以把cin>>写进循环条件里，但python不行
# 2：样例是连续11/21个W，但积分规则是每一局达到11分且领先对方2分。不能按11个或者21个划分一组

re_str = ''

while True:
    re_str += input().strip()
    if 'E' in re_str:
        re_str = re_str[:re_str.find("E")+1]
        break
# print(re_str)
# 逐个字符判断
def count_wl(num):
    w = 0
    l = 0
    for c in re_str:
        if c == 'W':
            w += 1
        elif c == 'L':
            l += 1
        elif c =='E':
            print('%d:%d' % (w, l))
        if (w >= num or l >= num) and (w-l>=2 or l-w>=2):
            print('%d:%d' % (w, l))
            w =0
            l =0
count_wl(11)
print()
count_wl(21)

#====以下为40分答案，按照11个或者21个分组，再挨组统计
# re_str = ''
# while True:
#     re_str += input().strip()
#     if 'E' in re_str:
#         re_str = re_str[:re_str.find("E") + 1]
#         break
#
#
# def count_WL(num):
#     n_temp = len(re_str)//num+1
#     for i in range(n_temp):
#         str_temp = re_str[i*num:i*num+num]
#         n_W = 0
#         n_L =0
#         for c in str_temp:
#             if c == 'W':
#                 n_W += 1
#             elif c == 'L':
#                 n_L += 1
#         print(str(n_W)+':'+str(n_L))
#
# count_WL(11)
# print()
# count_WL(21)