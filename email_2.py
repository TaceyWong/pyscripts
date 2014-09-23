#coding:utf-8
"""
	①添加邮件主题
	②收件人显示有好的民资
"""

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseader,formataddr
import smtplib

def _format_addr(s):
	name,addr = parseader(s)
	return formataddr((\
			Header(name,'utf-8').encode(),\
			addr.encode('utf-8') if isinstance(addr,unicode)else addr))

from_addr = raw_input("From:")
password = raw_input("Password:")
to_addr = raw_input("To:")
smtp_server = raw_input("Smtp server:")

#讲第二个参数plain改为html即可发送html邮件
msg = MINEText("hello,send by python",'plain','utf-8')
msg['From'] = _format_addr(u"Python爱好者<%s>"%from_addr)
msg['To'] = _format_addr(u"管理员<%s>"%from_addr)
msg['Subject'] = Header(u"来自SMTP的问候","utf-8").encode()

server = smtplib.SMTP(smtp_server,25)
server.set_debuglevel(1)
server.login(from_addr,password)
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()















