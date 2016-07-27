#encoding = utf-8
"""
单一页面的jpg格式图片抓取
"""
import os
import re
import urllib


def getHtml(url):
    """
    通过给定的url，获得html文件
    """
    page = urllib.urlopen(url)
    html = page.read()
    print "Step 1 ：获得HTML文件"
    return html

def getImg(html):
    """
    通过获得的HTML文件，分析出图片链接，下载保存
    """
    reg =r"""<img\s.*?\s?src\s*=\s*['|"]?([^\s'"]+).*?>"""# r'src="(.+?\.jpg)" pic_ext' #关键的正则匹配表达式（现在图灵不完备，且无法解决js控制的图片显示）

    imgre = re.compile(reg)
    print "Step 2 ：RE编译成功"
    imglist = imgre.findall(html)
    print "该页面共%d张图片"%(int)(len(imglist))
    count = 0
    
    
    for imgurl in imglist :
        try:
            urllib.urlretrieve(imgurl,'%s.jpg' % count)
            count += 1
        except:
            print "RAISE AN ERRO"
        print "第%d张图片保存成功"%count
    raw_input("脚本执行完毕，按任意键结束")
   

getImg(getHtml(raw_input("请输入要下载页面的网址（不保证能够完全成功，正则不是图灵完备的）：\n")))
