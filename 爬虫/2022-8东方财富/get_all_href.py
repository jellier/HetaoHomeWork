# -*- coding: utf-8 -*-
# @Time    : 2022/8/16 10:36 AM
'''
从首页开始尽可能遍历所有的子页面，返回所有的href值
'''
import requests
from bs4 import BeautifulSoup
import time
import json
h = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36 Edg/103.0.1264.77'}

# 保存已经爬过的地址，在每次爬取前先检查之前是否有爬过
check_list = list()

index_url = 'https://finance.eastmoney.com'


# 获取一个网页所有的a标签的地址，返回字典{'url': [a_href1, a_href2,...]}
def get_tag_a(url):
    global check_list
    set_a_href = dict()  # 存储当前页面地址和子页面地址的字典
    temp_list = list()  # 存储页面中所有属于本站的子页面链接地址
    try:
        if url not in check_list:
            check_list.append(url)
            r = requests.get(url, headers=h)
            r.encoding = 'utf-8'
            soup = BeautifulSoup(r.text, 'lxml')
            a_list = soup.find_all('a')
            # if len(a_list) < 1:
            #     return None  #
            for i in a_list:
                try:
                    a_href = i['href']
                    if 'eastmoney.com' in a_href:  # 需要有相应字符;姑且认为如果地址中没有该字符，那么就属于站外地址了
                        temp_list.append(a_href)
                except:
                    pass
    except:
        pass
    set_a_href[url] = temp_list

    return set_a_href




# 递归来获取所有的链接
def main(url):
    time.sleep(0.3)
    # 获取地址列表
    dicta = get_tag_a(url)
    url_list = dicta[url]
    # 将数据保存为本地
    # 先读取json文件，更新数据
    file = open('data.json')
    d = json.load(file)
    d[url] = url_list
    file.close()

    file = open('data.json', 'w')
    json.dump(d, file)
    file.close()

    if len(url_list) > 0:
        # 递归
        for url_i in url_list:
            main(url_i)
    else:
        return




if __name__ == '__main__':
    url = 'https://finance.eastmoney.com/'
    main(url)