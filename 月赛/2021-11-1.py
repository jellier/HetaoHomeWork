# 点击以下链接，根据提示修改上方数字，直到输出的结果不是数字。
# http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345
# 打印出这个非数字的字符串。

import requests

num = '12345'
while num.isdigit():
    _url ='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + num
    response = requests.get(_url)
    re_lis = response.text.split(' ')
    num = re_lis[::-1][0]
    # print(num)

print(response.text)