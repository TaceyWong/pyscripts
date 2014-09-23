"""
核心：
    from email.mime.text import MIMEText
    import smtplib
    ①msg = MIMEText("字符串"，'类型','编码格式')
    ②server = smtplib.SMTP(smtp服务器地址,端口号)
    ③server.login(发送地址,密码)
    ④server.sendmail(发送地址,[接收地址],msg.as_string())
    server.quit()
"""
from email.mime.text import MIMEText

msg = MIMEText(u"""Hello,This is Tacey Wong .
                    你好，我是王新勇""",'plain','utf-8')

from_addr = "i10000010001@126.com"

password = "12081536"

smtp_server = "smtp.126.com"

to_addr = "285289578@qq.com"

import smtplib
import time


for x in range(0,100000):
    server = smtplib.SMTP(smtp_server,25)#谷歌的是587
    server.starttls
    #server.set_debuglevel(1)
    server.login(from_addr,password)

    try:
        server.sendmail(from_addr,[to_addr],msg.as_string())
        #time.sleep(3)
    finally:
        print x
        
    server.quit()


