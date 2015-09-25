#/usr/bin/env python
# -*- coding: utf-8 -*
# encoding:utf8
import MySQLdb as mdb 
import urllib
import re
count = 0
con=mdb.connect('127.0.0.1','root','chendi1995','Movie_Recommend',charset="utf8")
cur=con.cursor()
def getHtml(url):
    page=urllib.urlopen(url)
    html=page.read()
    return html
def getmovie(html):
    global con
    global cur
    global count
    cur.execute('set names utf8')
    reg=r'<img src="(.*?)" width="96" height="128" alt="(.*?)" class="img_box" /></a></div> <dl> <dd class="clearfix"><h3 class=".*?"><a href="(.*?)" target="_blank">.*?导演： <a href=".*?" target="_blank" class=".*?">(.*?)</a> </dd>  <dd> 主演： <a href=".*?" target="_blank" class=".*?">(.*?)</a>.*?<dd class=".*?">(.*?)</dd>' 
    moviereg=re.compile(reg)
    movielist=re.findall(moviereg,html)
    for l in movielist:
        print l[0]
        print l[1].split('/')[0]
        temp=l[1].split('/')[0]
        print l[2]
        print l[3]
        print l[4]
        print l[5].strip()
        print "\n"
        count=count+1
        try:
            cur.execute("INSERT INTO movie (`Mname`, `MURL`, `Mpic`, `dtor`, `ator`, `info`) values('%s','%s','%s','%s','%s','%s')" %(str(temp),str(l[2]),str(l[0]),str(l[3]),str(l[4]),str(l[5].strip())))
            con.commit()
        except:
            print '重复，略去'
html=getHtml("http://movie.mtime.com/classic/rating/")
getmovie(html)
for i in range(2,11):
    html=getHtml("http://movie.mtime.com/classic/rating/index-%d.html" %i)
    getmovie(html)
con.close()
print "共抓取到%d部电影" %count
