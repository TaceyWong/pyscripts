#coding: utf8
import urllib2,re

#设置数据库变量
db.

url = "http://www.baidu.com"
find_re = re.compile(r'最为困难的一部，分析网页源码，编写正则表达式规则',re.DOTALL )

#定向爬10页最新的视频资源

for i in range(0,10):
    u = url%(i)

    #下载数据

    html = urllib2.urlopen(u).read()

    #找到资源下载

    for x in find_re.findall(html):
        values = dict(
            category = x[0]
            name = x[1]
            magnet = x[2]
            time = x[3]
            size = x[4])
        #保存到数据库

        db.
print "Done!"
