import random
yzm = random.randint(100000, 999999)
print('您的登录验证码为：', yzm)


def getUserInfo():
    with open('userpass.txt', 'r', encoding='utf-8') as f:
        user_info = f.read().split(',')
        return user_info


def getGoodsInfo():
    with open('goods.txt', 'r', encoding='utf-8') as f:
        goods = f.read().split(';')
        return goods


def showGoods():
    with open('goods.txt', 'r', encoding='utf-8') as f:
        goods = f.read().split(';')
        for i in goods:
            print(i)


user_list = getUserInfo()
uname_ipt = input('请输入用户名：')
pwd_ipt = input('请输入密码：')
yzm_ipt = input('登录验证码：')

if user_list[0] == uname_ipt and user_list[1] == pwd_ipt and str(yzm) == yzm_ipt:
    print('身份验证通过，欢迎登录！')
    goods_list = getGoodsInfo()
    while True:
        cmd = input('::')
        if cmd == 'add':
            new_no = input('商品编号：')
            new_name = input('商品名：')
            new_type = input('商品类型：')
            new_num = input('库存数量：')

            if new_no == '' or new_name == '' or new_type == '' or new_num == '':
                print('输入项不得为空，请重新输入')
                continue

            try:
                new_num = int(new_num)
            except ValueError:
                new_num = 0

            new_item = new_no + ',' + new_name + \
                ',' + new_type + ',' + str(new_num)
            goods_list.append(new_item)
            with open('goods.txt', 'w', encoding='utf-8') as f:
                f.write(';'.join(goods_list))
            showGoods()

        elif cmd == 'count':
            sum = 0
            for item in goods_list:
                num = item.split(',')[3]
                sum += int(num)
            print(sum)
            showGoods()
        else:
            exit()

else:
    print('身份验证失败！')
