#coding:utf-8
import poplib
import email
from email.parser import Parser
from email.header import Header 
from email.utils import parseaddr

def guess_charset(msg):
	charset = msg.get_charset()
	if charset is None:
		content_type = msg.get('Content-Type','').lower()
		pos = content_type.find('charset=')
		if pos >= 0:
			charset = content_type[pos + 8:].strip()
	return charset

def decode_str(s):
	value,charset = decode_header(s)[0]
	if charset:
		value = value.decode(charset)
	return value

def print_info(msg,indent = 0):
	if indent == 0:
		for header in ['Form','To','Subject']:
			value = msg.get(header,'')
			if value :
				if header == "Subject":
					value = decode_str(value)
				else:
					hdr,addr = parseaddr(value)
					name = decode_str(hdr)
					value = u'%s<%s>'%(name,addr)
			print "%s%s:%s"%(' '*indent,header,value)
	if (msg.is_multipart()):
		parts = msg.get_playoad()



















	