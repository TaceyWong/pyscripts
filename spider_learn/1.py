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

