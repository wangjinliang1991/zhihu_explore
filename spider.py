import requests
from pyquery import PyQuery as pq

url = 'https://www.zhihu.com/explore'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.04; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
}
html = requests.get(url, headers=headers).text
# print(html)
# 引入pyquery对象，别名pq，声明长HTML字符串，当做参数传给PyQuery类，完成初始化
doc = pq(html)
# 传入css选择器，调用items()方法，得到生成器，再进行遍历
items = doc('.explore-tab .feed-item')
for item in items.items():
    question = item.find('h2').text()
    author = item.find('.author-link-line').text()
# pq可以二次筛选,item.find('.content')得到的是HTML格式的字符串，需要整理，再进行提取
    answer = pq(item.find('.content').html()).text()
#     answer = item.find('.content').text()

    # file = open('explore.txt', 'a', encoding='utf-8')
    # file.write('\n'.join([question, author, answer]))
    # file.write('\n' + '='*50 + '\n')
    # file.close()
    with open('explore.txt', 'a', encoding='utf-8') as file:
        file.write('\n'.join([question, author, answer]))
        file.write('\n' + '='*50 + '\n')