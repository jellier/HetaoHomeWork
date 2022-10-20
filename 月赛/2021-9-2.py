ipt = input().strip('\r')
p_a,p_b = ipt.split('-')
idx_fgx = ipt.index('-')
pai = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2']
shun = ['3 4 5 6 7','4 5 6 7 8','5 6 7 8 9','6 7 8 9 10','7 8 9 10 J','8 9 10 J Q','9 10 J Q K','10 J Q K A', 'J Q K A 2']

def isBomb(s):
    # 炸弹是连续4张，且相同。如果长度为7的可能是炸弹也可能是顺子
    # s = 1 2 3 4 或者 s = 4 4 4 4
    if len(s) == 7 and s[0] == s[2] == s[4] == s[6]:
        return True
    else:
        return False
def isShun(s):
    # 顺子（连续5张）
    if (len(s.split(' '))) == 5 and (s in shun):
        return True
    else:
        return False
def isKeBi(a,b):
    lis_a = a.split(' ')
    lis_b = b.split(' ')

    if len(lis_a) == len(lis_b) and len(set(lis_a)) == 1 and len(set(lis_b)) == 1:
        return True

    else:
        return False

# 1、有王
if 'joker' in ipt:
    idx_joker = ipt.index('joker')
    if idx_joker > idx_fgx:
        print(p_b)
    else:
        print(p_a)
# 2、有炸弹
elif isBomb(p_a) or isBomb(p_b):
    if isBomb(p_a) == True and isBomb(p_b) == False:
        print(p_a)
    elif isBomb(p_a) == False and isBomb(p_b) == True:
        print(p_b)
    else:
        # 如果都是炸弹
        #if int(p_a[0]) > int(p_b[0]):
        if pai.index(p_a[0]) > pai.index(p_b[0]):
            print(p_a)
        else:
            print(p_b)
# 3、顺子
elif isShun(p_a) and isShun(p_b) and len(p_a.split(' ')) == len(p_b.split(' ')):
    first_char_a = p_a[0]
    first_char_b = p_b[0]
    if pai.index(first_char_a) > pai.index(first_char_b):
        print(p_a)
    else:
        print(p_b)
# 4、其他能比的（个子，对子，三个）
elif isKeBi(p_a,p_b):
    first_char_a = p_a[0]
    first_char_b = p_b[0]
    if pai.index(first_char_a) > pai.index(first_char_b):
        print(p_a)
    else:
        print(p_b)
# 4、不能比的
else:
    print('ERROR')
