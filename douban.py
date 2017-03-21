#coding=utf-8
from bs4 import BeautifulSoup
import requests
url = 'https://movie.douban.com/chart'
response = requests.get(url).text
bsobj = BeautifulSoup(response,'html.parser')
bsobj = bsobj.find_all('div',{'class':'pl2'})
#使用chrome分析网页结构找到自己要的内容
for tag in bsobj:
    div_tag = tag.contents[1].get_text()#取得文本内容
    movie_name = div_tag.strip('\n').replace(' ','')+'\n'
    #剔除换行将换行变成空
    print(movie_name)
    #打印结果
