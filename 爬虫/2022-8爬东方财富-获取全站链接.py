# 参考：https://blog.csdn.net/wxfghy/article/details/80308825
import re
from bs4 import BeautifulSoup
import requests
import time
import json

DOMAIN = 'eastmoney.com/'
# 获取并检验要爬取的网站

def url_get():
    # url = input("please input the url:")
    url = 'https://www.eastmoney.com/'

    try:
        kv={'user_agent':'Mozilla/5.0'}
        requests.get(url,headers=kv)
        return url

    except:
        print("your url is incorrect!!")
        return url_get()

'''
找出url中的域名
比如从https://www.xiaogeng.top/article/page/id=3筛选出www.xiaogeng.top

def url_same(url):

    #判断输入的网站使用的是https还是http
    urlprotocol=re.findall(r'.*(?=://)',url)[0]
    print('该站使用的协议是：' + urlprotocol)

    if len(re.findall(r'/',url)) >2:
        if urlprotocol=='https':
            sameurl = re.findall(r'(?<=https://).*?(?=/)', url)[0]
        else:
            sameurl = re.findall(r'(?<=http://).*?(?=/)', url)[0]
    else:
        url = url + '/'
        if urlprotocol=='https':
            sameurl = re.findall(r'(?<=https://).*?(?=/)',url)[0]
        else:
            sameurl = re.findall(r'(?<=http://).*?(?=/)',url)[0]
    print('域名地址：' + sameurl)

    return sameurl
'''



# 爬取url页面中的所有链接
def spiderpage(url):
    h = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'}

    r=requests.get(url,headers=h)
    r.encoding=r.apparent_encoding
    if r.status_code != 200:
        print(r.status_code)

    soup = BeautifulSoup(r.content, features="html.parser")

    a_links = soup.find_all('a', href=True)
    pagelinks = []

    for i in a_links:
        i_href = i.get('href')
        # 筛掉只有javascript的
        if 'javascript' not in i_href:
            # 如果是相对路径，则补全网址
            if DOMAIN not in i_href or i_href[0] == '/':
                tail = url.split('/').pop()
                if tail == '':
                    new_url = url + i_href.lstrip('/')
                else:
                    new_url = url.replace(tail, i_href.lstrip('/'))

                pagelinks.append(new_url)
            else:
                pagelinks.append(i_href)

    return pagelinks


# 去重
def url_filtrate(pagelinks):
    #去除重复url
    unrepect_url = list(set(pagelinks))

    return unrepect_url

#将一个列表写入文件
def writetofile(list):
    print('write')
    file = open('urls.txt','w')
    print(list)
    for url in list:
        file.write(url)
        file.write('\n')
        file.close()

def save_txt(list):
    f = open("urls.txt", "a", encoding="utf8")
    for i in list:
        f.write(i)
        f.write('\n')
    f.close()

# url集合，循环遍历会用到
class linkQuence:
    def __init__(self):
        #已访问的url集合
        self.visited=[]
        #待访问的url集合
        self.unvisited=[]

    #获取访问过的url队列
    def getvisitedurl(self):
        return self.visited

    #获取未访问的url队列
    def getunvisitedurl(self):
        return self.unvisited

    #添加url到访问过得队列中
    def addvisitedurl(self,url):
        return self.visited.append(url)

    #移除访问过得url
    def removevisitedurl(self,url):
        return self.visited.remove(url)

    #从未访问队列中取一个url
    def unvisitedurldequence(self):
        return self.unvisited.pop()

    #添加url到未访问的队列中
    def addunvisitedurl(self,url):
        if url!="" and url not in self.visited and url not in self.unvisited:
            return self.unvisited.insert(0,url)

    #获得已访问的url数目
    def getvisitedurlount(self):
        return len(self.visited)

    #获得未访问的url数目
    def getunvistedurlcount(self):
        return len(self.unvisited)

    #判断未访问的url队列是否为空
    def unvisitedurlsempty(self):
        return len(self.unvisited)==0

# 真正的爬取函数
class Spider():
    def __init__(self,url):
        self.linkQuence = linkQuence() #引入linkQuence类
        self.linkQuence.addunvisitedurl(url) #并将需要爬取的url添加进linkQuence对列中

    def crawler(self):
        total = 1
        while not self.linkQuence.unvisitedurlsempty():# 若未访问队列非空

            visitedurl = self.linkQuence.unvisitedurldequence()# 取一个url
            print('当前地址：',visitedurl)
            if visitedurl is None or visitedurl == '':
                continue

            initial_links = spiderpage(visitedurl) # 爬出该url页面中所有的链接

            right_links = url_filtrate(initial_links) # 链接去重

            self.linkQuence.addvisitedurl(visitedurl) # 将该url放到访问过的url队列中
            total -= 1

            for link in right_links: # 将筛选出的链接放到未访问队列中
                self.linkQuence.addunvisitedurl(link)
                # print(self.linkQuence.unvisited)

            total += len(right_links)
            print("这一页的链接数量", len(right_links))
            print('当前已找到的链接数量：',total)
            print('当前已访问的链接数量：',len(self.linkQuence.visited))
            print('当前未访问的链接数量：',len(self.linkQuence.unvisited))
            print()

            save_txt(self.linkQuence.visited)

            time.sleep(0.3)

        print('网站所有链接爬取结束,共',total,'个')

        # 如果在crawler里面写，就不需要返回了
        # return self.linkQuence.visited

if __name__ == '__main__':

    url=url_get()

    # sameurl=url_same(url)

    spider = Spider(url)

    urllist = spider.crawler()

    # writetofile(urllist)