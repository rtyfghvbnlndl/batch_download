import re
import requests


class get_pic(object):
    def __init__(self,url,num):
        self.url = url
        self.num = num
    def topic(self):
        r = requests.get('https://%s/%i.html' % (self.url,self.num))
        title = re.findall(r'<title>(.+)&.+</title>|<title>(.+);.+</title>|<title>(.+)</title>',r.text)
        return title
    def get_imgurl(self):
       r = requests.get('https://%s/%i.html' % (self.url,self.num))
       list = re.findall(r'"(http.+[jpgpngwebgif])" alt=', r.text)
       return list
if __name__ == '__main__':

    p1 = get_pic(input('网址?'),input('序号?'))
    t = p1.topic()
    i = p1.get_imgurl()
    print(t,i)
    