import urllib,urllib2,re,os
import getpagedata as g
x='http://tieba.baidu.com/p/3719947505'
data2=g.getpagedata(x)
authorname=re.findall(r'<a data-field=.*?alog-group="p_author".*?href=".*?" target="_blank">(.*?)</a>',data2)
print data2