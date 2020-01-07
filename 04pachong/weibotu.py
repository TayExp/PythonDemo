import requests
from bs4 import BeautifulSoup as bs
import os
import re
#uid即进入对方微博主页后网址部分/u/后的那一串数字
# uid = '5514698954'
# # url = 'https://weibo.cn/u/' + uid

url = 'https://weibo.cn/5514698954/profile?filter=1&'
# url = 'https://weibo.cn/u/5311595890?'
cookie = {'SCF':'AoFH1fFdQam2SPMd3SI2aMqNdFP3FlJ5rGUkKFjx9lZ2zgwA3v5u3CdcsvFnHzc_Svz7HxOZxE4kRhcSwRM0GZU.',
    'SUHB':'0S7CwLVphwkkt1',
    'ALF':'1580999295',
    'SSOLoginState':'1578407298',
    'SUB':'_2A25zEOXSDeRhGeNL6lYX-SbFzjiIHXVQ-ouarDV6PUNbktAKLXX5kW1NSTP6yVUXvHHjb77njgUs4u34DZT6uig-',
    'SUBP':'0033WrSXqPxfM725Ws9jqgMF55529P9D9W5Nv5sIppesYuSBzHmCCMa65JpX5KMhUgL.Fo-feKBc1Kn4SKB2dJLoIpWkPcUadcxbwg-EMNH_dgHE',
    '_T_WM':'43500383d6566d51b95a1bbc5653db8f'}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'}
r = requests.get(url, headers=headers,cookies=cookie)
soup = bs(r.text, 'html.parser')
# 所访问的微博用户名
weibo_user_name = soup.find('title').text.replace('的微博', '')
#  存放图片的根目录
rootDir = 'F://我的微博//' + weibo_user_name + '配图' + '//'
# 微博总页数,通过审查元素可知
totalPage = int(soup.find('input', attrs={'name': 'mp'}).attrs['value'])
print('总共检测到%d页微博页面' % totalPage)
# 每页微博的URL的列表
weibo_urlList = [url + 'page=' + str(i + 1) for i in range(totalPage)]
#当前已爬取的图片总数
pictrue_num = 0
for page, weibo_url in enumerate(weibo_urlList):
    r = requests.get(weibo_url, headers=headers, cookies=cookie)
    soup = bs(r.text, 'html.parser')
    #每条微博所对应的标签代码块列表
    weibo_tags_list = soup.find_all('div', attrs={'class': 'c'}, id=True)
    #微博发送时间与微博配图的字典
    imgs_urls_dic = {}
    for entry, weibo_tag in enumerate(weibo_tags_list):
        print('正在爬取第%d页第%d条微博' % (page + 1, entry + 1))
        #获取微博发送时间
        hms_cct = weibo_tag.find('span', attrs={'class': 'ct'})
        if(hms_cct == None):
            continue
        hms = ' '.join(hms_cct.text.replace('\xa0', ' ').replace(':', '：').split(' ')[:2])
        #该条微博若带有组图，获取组图中所有图片的URL
        if weibo_tag.find('a', text=re.compile(r'组图')):
            imgs_url = weibo_tag.find('a', text=re.compile(r'组图')).attrs['href']
            html = requests.get(imgs_url, headers=headers, cookies=cookie)
            imgs_soup = bs(html.text, 'html.parser')
            imgs_tags_List = imgs_soup.find_all('img', alt='图片加载中...')
            img_urls_list = [imgs_tag.attrs['src'].replace( 'thumb180', 'large') for imgs_tag in imgs_tags_List]
            imgs_urls_dic[hms] = img_urls_list
        #该条微博仅有一张配图，或者没有图片，获取图片的URL
        else:
            img_tags_List = weibo_tag.find_all('img', alt='图片')
            img_urls_list = [img_tag.attrs['src'].replace( 'wap180', 'large') for img_tag in img_tags_List]
            imgs_urls_dic[hms] = img_urls_list
        print('第%d页第%d条微博爬取完毕,开始生成图片' % (page + 1, entry+1))
        for hms, img_urls_list in imgs_urls_dic.items():
            for index, img_url in enumerate(img_urls_list):
                #生成图片的存放路径，图片被命名为微博发送时间
                path = rootDir + hms
                #如果一条微博在同一时间发送了多张图片(即组图)的命名处理
                if(index > 0):
                     path = path + '(' + str(index) + ')'
                path = path + '.jpg'
                try:
                    if not os.path.exists(rootDir):#makedirs递归生成多级目录，mkdir仅能生成一级目录
                        os.makedirs(rootDir)
                    if not os.path.exists(path):
                        r = requests.get(img_url)
                        with open(path, 'wb') as f:
                            f.write(r.content)
                            pictrue_num = pictrue_num + 1
                            print('success,成功爬取第%d张图片' % pictrue_num)
                    else:
                        print('%s已经存在' % path)
                except:
                    print('爬取失败,%s' % img_url)
        imgs_urls_dic = {}
print('总共爬取了%d张图片，存放在 %s 目录下' % (pictrue_num, rootDir))