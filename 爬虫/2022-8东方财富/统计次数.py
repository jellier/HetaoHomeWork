# -*- coding: utf-8 -*-
# @Time    : 2022/8/16 4:02 PM
'''
读取data.json文件，统计各个地址被引用的次数，输出排名靠前的100个地址
{u1:[u2,u3,...], ux:[u11, u13,...], ...}
'''
import json
import pandas as pd

file = open('data.json')

dicta = json.load(file)

count = {}  # 各个链接及被引用的次数

# 将引用的链接存储起来
details = {}

for k, v in dicta.items():
    for url in v:
        if "finance.eastmoney.com" in url:
            if url not in count:
                count[url] = 1
            else:
                count[url] += 1
            if url not in details:
                details[url] = []
                details[url].append(k)
            else:
                details[url].append(k)

# 按照引用次数进行排序，并将前100保存下来
a = sorted(list(count.items()), key=lambda x:x[1], reverse=True)
rank100 = a[:100]
print(rank100)

quoted_url = [i[0] for i in rank100]
quoted_times = [i[1] for i in rank100]
transform_dict = {'quoted_url':quoted_url, 'quoted_times':quoted_times}
df = pd.DataFrame(transform_dict)
df.to_csv('rank100.csv')




