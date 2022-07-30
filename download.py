import collections
import os
import requests
import find

url =  str(input('输入网址（不需要http'))
min = int(input('输入编号'))
max = int(input('它是一个范围吗（输入上限值或0）'))
if max <= min:
    max = min+1
else:
     max += 1
print(min,max)
for num in range (min,max):
    print(url,num)
    p1 = find.get_pic(url,num)
    name = p1.topic()
    name = re.sub('[/*\:;|, ]','',name[0][0])
    #title中可能不再有&,此时更改第二位数字。 
    print(name)
    url_ed = p1.get_imgurl()
    print(url_ed,name)
    d = './%s' % name
    print(d)
    if not os.path.exists(d):
        os.mkdir(d)
    pic_num = 1
    for pic_url in url_ed:
         print(pic_url)
         r = requests.get(pic_url)
         from contextlib import closing
         with closing(r) as response:
            with open('%s/%s%i.jpg' % (d,name,pic_num), 'wb') as fd:
                for chunk in response.iter_content(128):
                   fd.write(chunk)
         print('保存为%s/%s%i.jpg' % (d,name,pic_num))
         print('保存图片循环%i次' % pic_num)
         pic_num += 1
         sleep(1)
    print('序号循环到%i' % num)
    sleep(2)
print('结束')
