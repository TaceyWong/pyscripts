#coding:utf-8
import urllib
import BeautifulSoup

'''
脚本功能：从一个存储有不同地点名字的文本文档读取数据获得地点的经纬度并保存到文本
作者：王新勇（Tacey Wong）
时间：2014年12月12号
环境：Win8、Python2.7
输入数据格式：文本，每行存储一个地点（学校名）
输出数据格式：文本，[ID] [经度] [纬度] [地点名称]
-_-:代码很大一部分在处理中文问题
'''

####################从文件读取学校列表并存储到一个列表##############################

schoollist = []
count = 0

fr = open("testdata.txt")                                                        
for line in fr.readlines():
    line = line.strip()
    if line not in schoollist:
        schoollist.append(line)
        count += 1
        print count,
        print line

fr.close()            
print u"共计",
print str(count),
print u"个地点"

print raw_input(u"从网络获取经纬度信息？[任意键回车继续，CTR+C结束]\n>>")
####################通过百度地图API获得学校经纬度并输出到文件########################################
count = 0
fail = 0
length = len(schoollist)
data = open("data.txt","w")
schoollist_temp = []
fail_get = []

for add in schoollist:
    addcoded = urllib.quote(add)
    try:
        p = urllib.urlopen("http://api.map.baidu.com/geocoder/v2/?address="+addcoded+"&output=xml&ak=7948ee8bad7d78cb9cff9081a0f44767&callback=showLocation")
        info = p.read()

        #print info

        soup = BeautifulSoup.BeautifulSoup(info,fromEncoding="gb2312")

        j = soup.find('lng').text
        w = soup.find('lat').text
        count += 1
    except:
        count += 1
        fail += 1
        print u"无法获取",
        print add,
        print u"的经纬信息"
        print u"完成",
        print str(int(count*1.0/length*100))+"%"
        #print str(count)+" null"+" null"
        fail_get.append(add)
        data.write(str(count)+"  null  null   ")
        data.write(add)
        data.write('\n')
        continue
    print u"完成",
    print str(int(count*1.0/length*100))+u"%"
    #schoollist_temp.append(str(count)+" "+j+" "+w)
    data.write(str(count)+"  "+j+"  "+w+"  ")
    data.write(add)
    data.write('\n')
data.close()

print "Done!"
print u"成功："+str(count-fail)
print u"失败："+str(fail)
print u"获取经纬度失败的地点：\n"
if ( fail > 0 ):
    for i in fail_get:
        print i
    


