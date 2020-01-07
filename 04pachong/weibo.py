import requests
import re
def get_myuid(cookies):
    url = 'http://weibo.cn/'
    html = requests.get(url,cookies=cookies).content
    #用get请求加入cookies参数登陆微博主页
    print(html)
    a = html.find('[\'uid\']=')
    b = html[a:].find(';')
    myuid = html[a + len('[\'uid\']='): a + b][1:-1] #获取我的uid
    a = html.find('[\'nick\']=')
    b = html[a:].find(';')
    myname = html[a + len('[\'nick\']='): a + b][1:-1] #获取我的用户名
    return myuid,myname
cookie = {}
cookie['SUHB'] ='0YhRyYrPor8BrP'
cookie['SSOLoginState'] ='1545640641'
cookie['SCF'] ='AjvA1qZ_5sy21xNdCyTnzjpNAeorqFjUllXqy5nXdA2mzbUOO5iDn6GXRkbb7t5BElMQsAIPCPPo9OGOZIueUvw.'
cookie['SUB'] ='_2A25xJOqRDeRhGeNL6lYX-SbFzjiIHXVS5vbZrDV6PUJbkdAKLXjmkW1NSTP6yZWvrVeGxYDgWWBDi2XejV_Z7pkX'
cookie['_T_WM'] ='bec86c56ca6c0b2577cd8eaef68bd105'
uid, name = get_myuid(cookie)

SUHB:"0S7CwLVphy18Yy"
SSOLoginState:"1549222422"
SCF:"AmowoxZAGkrN07EYyA2y_1lUe0wNNtu2RDgHdXCBxALaLN9PHR42pNCSBZGjs3YYDzZj4A5kC5X8vn6j0G_MxeY."
SUB:"_2A25xUzJGDeRhGeNL6lYX-SbFzjiIHXVSvF4OrDV6PUJbktANLXalkW1NSTP6yYiZNH8vkbA5C0JEKOkwRaOQ78UY"
_T_WM:"f001ebd2ba040ada8a9443847ba68fab"