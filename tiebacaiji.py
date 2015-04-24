#-*- coding:utf-8 -*-
import re,urllib,urllib2,cookielib

headers={
		'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
		'Cookie':'',
		'Host':'tieba.baidu.com',
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36'
}
url=raw_input('url:')
request=urllib2.Request(url,headers=headers)
data=urllib2.urlopen(request).read()
authorname=re.findall(r'<a data-field=.*?alog-group="p_author".*?href=".*?" target="_blank">(.*?)</a>',data)
picurl=re.findall(r'<img class="BDE_Image" src="(.*?)" pic_ext="jpeg"',data)
i=0
for x in picurl:
	filename=str(i)+'.jpg'
	data1=urllib2.urlopen(x).read()
	file=open(filename,'wb')
	file.write(data1)
	file.close()
	i=i+1
print 'finished!'