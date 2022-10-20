# 8月python月赛题：

# 给出被东方财富网内部引用最高的100个，且前缀是 finance.eastmoney.com 的链接（finance.eastmoney.com这个网址不计入）。
# 也就是前缀是 finance.eastmoney.com的网页在eastmoney.com 里被引用次数排名

# 提交格式：被引用链接，引用链接。按照被引用次数排序，并给出统计的时间点。

import requests
from bs4 import BeautifulSoup


#请求网页, 返回响应
def download_page(url):
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "Connection": "close",
        "Cookie": "_gauges_unique_hour=1; _gauges_unique_day=1; _gauges_unique_month=1; _gauges_unique_year=1; _gauges_unique=1",
        "Referer": "http://www.infoq.com",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36 LBBROWSER"
    }
    data = requests.get(url, headers=headers).content
    return data

# 获取当前页上所有的链接
def parseHtml(html):
    global a_links,f_links
    soup = BeautifulSoup(html, features="html.parser")


    page_a = soup.find_all('a',href=True)
    for i in page_a:
        i_href = i.get('href')
        # 筛掉只有javascript的
        if 'http' in i_href:
            if i.get('href') not in a_links:
                a_links.append(i.get('href'))




def filterLink(url):
    pass


INDEX_URL = 'https://www.eastmoney.com/'
TARGET_URL = 'https://finance.eastmoney.com'
a_links = []
f_links = []
def main():
    # 从主页开始，逐级向下找链接


    url = INDEX_URL

    # 第一步：获取当前页面上所有链接，存到列表a_links中，同时将finance域名下的放到f_links
    html = download_page(url)
    links = parseHtml(html)



if __name__ == '__main__':
    main()