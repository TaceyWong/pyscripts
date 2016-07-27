# coding:utf-8

import urllib2
print "test"

#urlopen(url,data,timeout)
#timeout = socket._GLOBAL_DEFAULT_TIMEOUT
response = urllib2.urlopen("http://www.baidu.com")
print response.read()

request = urllib2.Request("http://www.baidu.com")
response = urllib2.urlopen(request)
print response.read()

import urllib

values = {
    "input1":"tacey",
    "input2":"xxxxxx",
    "remember":"true"
    }
data = urllib.urlencode(values)
url = "http://passport.cnblogs.com/user/signin"
data = urllib.urlencode(values)
request = urllib2.Request(url,data)
response = urllib2.urlopen(request)

print response.read().decode("utf-8")

url = ""
useragent =""
values = {}
headers = {"useragent":useragent}
data = urllib.urlencode(values)
request = urllib2.Request(url,data,headers)
response = urllib2.urlopen(request)


enable_proxy = True
proxy_handler = urllib2.ProxyHandler({"http":"http://"})
null_proxy_handler = urllib2.ProxyHandler({})
if enable_proxy:
    opner = urllib2.build_opener(proxy_handler)
else:
    opner = urllib2.build_opener(null_proxy_handler)

urllib2.install_opener(opener)


request = urllib2.Request(url,data=None)
request.get_method = lambda : 'PUT' #DELETE 或者更底层的httplib


httpHandler = 








