from os import path
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus'] = False

d = path.dirname(__file__)
string = open(path.join(d,  "image/shopcart_jieba.txt")).read()

textlist = string.split(' ')
print(textlist)
child=['儿童', '宝宝', '青少年', '幼儿', '中大童', '小童', '男孩', '女孩', '12 ', '7 ', '15 ', '3 ', '4 ', '5', '亲子']
adult = ['男', '女', '妈妈', '爸爸', '成人', '中老年']
food =['早餐', '代餐 ', '饱腹 ', '食品 ', '五谷杂粮', '粗粮 ', '小吃', '主食', '零食', '奶酪 ', '烘焙', '海鲜', '糖果']
toy =['滑板车 ', '闪光']
book=['进口 ', '小说 ', '桥梁 ', '书', '英文原版 ', '全彩', '卡通', '启蒙 ', '绘本 ', '图画书 ', '新华 ', '正版', '数学 ', '书籍', '平装 ', '套装', '系列 ', '全套']
cloth = ['套头毛衣 ', '线衣 ', '针织 ', '上衣', '纯棉', '羽绒服']
family = ['户外 ', '手推车 ', '家居服']
rword = '其他'
counts={}
for word in textlist:
    # 去标点符号
    if word == ' ':
        continue
    elif word in child or word in toy or word in book:
        rword = '孩子'
    elif word in adult or word in cloth:
        rword = '大人'
    elif word in food or word in family:
        rword = '全家'

    counts[rword] = counts.get(rword,  0) + 1
print(counts)

labels = counts.keys()
sizes = counts.values()
# 获取最大值的位置
max_index = list(sizes).index(max(sizes))

# explode：指定饼图某些部分的突出显示，即呈现爆炸式
# explode = (0,0,0.1,0)
explode_list = [0]*len(counts)
explode_list[max_index] = 0.1
explode = tuple(explode_list)

plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=150)
plt.title("老母亲的购物车")
plt.show()