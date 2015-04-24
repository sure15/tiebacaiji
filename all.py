#-*- coding:utf-8 -*-
#生成要采集的索引页面链接
import urllib,urllib2,re,os
import getpagedata as g

url=raw_input('input the primary url:')
startp=int(raw_input('StarPage:'))
endp=int(raw_input('EndPage:'))
data=[]
startp=startp-1
while startp<endp:
	x=url+str(startp*50)
	data.append(x)
	startp +=1
	print x
bigurls=[]
for x in data:
	data1=g.getpagedata(x)
	urls=re.findall(r'<div class="threadlist_title.*?">.*?<a href="(.*?)" title=".*?" target="_blank" class="j_th_tit">',data1)
	for x in range(len(urls)):
		urls[x]='http://tieba.baidu.com'+urls[x]+'?see_lz=1'
	bigurls=bigurls+urls
print bigurls
for x in bigurls:
	data2=g.getpagedata(x)
	authorname=re.findall(r'<a data-field=.*?alog-group="p_author".*?href=".*?" target="_blank">(.*?)</a>',data2)
	print authorname[0]
	picurl=re.findall(r'<img class="BDE_Image".*?src="(.*?)".*?>',data2)
	os.mkdir('d:\\pic\\'+authorname[0]+'\\')
	i=0
	for xx in picurl:
		name=str(i)+'.jpg'
		picpath='d:\\pic\\'+authorname[0]+'\\'+name
		data1=urllib2.urlopen(xx).read()
		file=open(picpath,'wb')
		file.write(data1)
		file.close()
		i=i+1
	readme='d:\\pic\\'+authorname[0]+'\\'+'readme.txt'
	with open(readme,'w') as f:
		f.write(x)
print 'finished!'