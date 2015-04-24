#-*- coding:utf-8 -*-
import re,urllib,urllib2,cookielib
def getpagedata(url):
	headers={
			'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
			'Cookie':'',
			'Host':'tieba.baidu.com',
			'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'
	}
	request=urllib2.Request(url,headers=headers)
	data=urllib2.urlopen(request).read().decode('utf-8')
	return data