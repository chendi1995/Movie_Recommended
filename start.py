#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import MySQLdb as mdb
from math import *
reload(sys)
sys.setdefaultencoding('utf-8')
import bottle
from bottle import *

#bottle.TEMPLATE_PATH.insert(0, "./template/")
DBaddress='127.0.0.1'

@route('/login')
def login_form():
    return static_file('login.html',root='./views/')
@post('/login')
def login():
    global DBaddress
    con=mdb.connect(DBaddress,'root','chendi1995','Movie_Recommend',charset='utf8')
    cur=con.cursor()
    cur.execute('set names utf8')
    name=request.forms.get('name')
    if name=='admin': 
        return template('admin-index.html',root='./views/')
    sex=request.forms.get('sex')
    age=request.forms.get('age')
    email=request.forms.get('email')
    try:
        cur.execute("INSERT INTO user VALUES ('%s','%s',%d,'%s')"%(name,sex,int(age),email))
        #print cur
        con.commit()
        con.close()
        #return '<META HTTP-EQUIV="Refresh" CONTENT="5;URL=localhost:8080/survey"><登录成功，等待3秒自动跳转...>'
        return '<META HTTP-EQUIV="Refresh" CONTENT="3;URL=survey/%s "><登录成功，等待3秒自动跳转...>'%name
    except:
        con.rollback()
        return '<META HTTP-EQUIV="Refresh" CONTENT="3;URL=survey/%s "><登录成功，等待3秒自动跳转...>'%name

@route('/admin_movie')
def movie():
    global DBaddress
    con=mdb.connect(DBaddress,'root','chendi1995','Movie_Recommend',charset='utf8')
    cur=con.cursor()
    cur.execute('set names utf8')
    cur.execute('SELECT * FROM movie')
    results=cur.fetchall()
    return template('admin-movie',msg=results)

@route('/admin_user')
def movie():
    global DBaddress
    con=mdb.connect(DBaddress,'root','chendi1995','Movie_Recommend',charset='utf8')
    cur=con.cursor()
    cur.execute('set names utf8')
    cur.execute('SELECT * FROM user')
    results=cur.fetchall()
    return template('admin-user',msg=results)
    
@route('/admin_edit/<id>')
def movie_edit(id):
    return static_file('admin-movie_add.html',root='./views')
@post('/admin_edit/<id>')
def movie_edit_post(id):
    global DBaddress
    con=mdb.connect(DBaddress,'root','chendi1995','Movie_Recommend',charset='utf8')
    cur=con.cursor()
    cur.execute('set names utf8')
    name=request.forms.get('name')
    picurl=request.forms.get('picurl')
    Dtor=request.forms.get('Dtor')
    ator=request.forms.get('ator')
    url=request.forms.get('url')
    info=request.forms.get('info')
    try:
        cur.execute('select * from movie')
        results=cur.fetchall()
        cur.execute("UPDATE `movie` SET `Mname` = '%s',`MURL` = '%s',`Mpic` = '%s',`dtor` = '%s',`ator` = '%s',`info` = '%s' WHERE `Mname` = '%s'"%(name,url,picurl,Dtor,ator,info,results[int(id)-1][0]))
        con.commit()
        con.close()
        return '<META HTTP-EQUIV="Refresh" CONTENT="0;URL=/admin_movie ">'
    except:
        return '<META HTTP-EQUIV="Refresh" CONTENT="1;URL=/admin_movie "><p>不能有重复的电影名,修改失败</p>'

@route('/admin_user_edit/<id>')
def user_edit(id):
    return static_file('admin-user_add.html',root='./views')
@post('/admin_user_edit/<id>')
def user_edit_post(id):
    global DBaddress
    con=mdb.connect(DBaddress,'root','chendi1995','Movie_Recommend',charset='utf8')
    cur=con.cursor()
    cur.execute('set names utf8')
    name=request.forms.get('name')
    sex=request.forms.get('sex')
    age=request.forms.get('age')
    email=request.forms.get('email')
    try:
        cur.execute('select * from user')
        results=cur.fetchall()
        cur.execute("UPDATE `user` SET `Uname` = '%s',`Usex` = '%s',`Uage` = %d,`email` = '%s' WHERE `Uname` = '%s'"%(name,sex,int(age),email,results[int(id)-1][0]))
        con.commit()
        con.close()
        return '<META HTTP-EQUIV="Refresh" CONTENT="0;URL=/admin_user ">'
    except:
        return '<META HTTP-EQUIV="Refresh" CONTENT="1;URL=/admin_user "><p>不能有重复的用户姓名,修改失败</p>'

@route('/admin_user_add')
def movie_add():
    return static_file('admin-user_add.html',root='./views')
@post('/admin_user_add')
def movie_edit_post():
    global DBaddress
    con=mdb.connect(DBaddress,'root','chendi1995','Movie_Recommend',charset='utf8')
    cur=con.cursor()
    cur.execute('set names utf8')
    name=request.forms.get('name')
    sex=request.forms.get('sex')
    age=request.forms.get('age')
    email=request.forms.get('email')
    try:
        cur.execute("insert into user VALUES('%s','%s',%d,'%s')" %(name,sex,int(age),email))
        con.commit()
        con.close()
        return '<META HTTP-EQUIV="Refresh" CONTENT="0;URL=/admin_user ">'
    except:
        return '<META HTTP-EQUIV="Refresh" CONTENT="1;URL=/admin_user "><p>添加失败</p>'

@route('/admin_add')
def movie_add():
    return static_file('admin-movie_add.html',root='./views')
@post('/admin_add')
def movie_edit_post():
    global DBaddress
    con=mdb.connect(DBaddress,'root','chendi1995','Movie_Recommend',charset='utf8')
    cur=con.cursor()
    cur.execute('set names utf8')
    name=request.forms.get('name')
    picurl=request.forms.get('picurl')
    Dtor=request.forms.get('Dtor')
    ator=request.forms.get('ator')
    url=request.forms.get('url')
    info=request.forms.get('info')
    try:
        cur.execute("insert into movie VALUES('%s','%s','%s','%s','%s','%s')" %(name,url,picurl,Dtor,ator,info))
        con.commit()
        con.close()
        return '<META HTTP-EQUIV="Refresh" CONTENT="0;URL=/admin_movie ">'
    except:
        return '<META HTTP-EQUIV="Refresh" CONTENT="1;URL=/admin_movie "><p>添加失败</p>'


@route('/admin_delete/<id>')
def movie_delete(id):
    global DBaddress
    con=mdb.connect(DBaddress,'root','chendi1995','Movie_Recommend',charset='utf8')
    cur=con.cursor()
    cur.execute('set names utf8')
    cur.execute('select * from movie')
    results=cur.fetchall()
    try:
        cur.execute("DELETE FROM `movie` WHERE `Mname` = '%s'" %results[int(id)-1][0])
        con.commit()
        con.close()
        return '<META HTTP-EQUIV="Refresh" CONTENT="0;URL=/admin_movie ">'
    except:
        return '<META HTTP-EQUIV="Refresh" CONTENT="1;URL=/admin_movie "><p>删除失败</p>'

@route('/admin_user_delete/<id>')
def user_delete(id):
    global DBaddress
    con=mdb.connect(DBaddress,'root','chendi1995','Movie_Recommend',charset='utf8')
    cur=con.cursor()
    cur.execute('set names utf8')
    cur.execute('select * from user')
    results=cur.fetchall()
    cur.execute("DELETE FROM `user` WHERE `Uname` = '%s'" %results[int(id)-1][0])
    try:
        con.commit()
        con.close()
        return '<META HTTP-EQUIV="Refresh" CONTENT="0;URL=/admin_user ">'
    except:
        return '<META HTTP-EQUIV="Refresh" CONTENT="1;URL=/admin_user "><p>删除失败</p>'
@route('/survey/:name')
def survey(name):
    global DBaddress
    print name
    con=mdb.connect(DBaddress,'root','chendi1995','Movie_Recommend',charset='utf8')
    cur=con.cursor()
    cur.execute('set names utf8')
    cur.execute('SELECT * FROM movie')
    results=cur.fetchall()
    return template('survey',movielist = results)
#css和js的路由设置    
@route('/FlatUI/<filename1>/<filename2>')
def server_static(filename1,filename2):
    return static_file(filename2, root='./views/FlatUI/'+'/'+filename1)

@route('/FlatUI/<filename1>/<filename2>/<filename3>')
def server_static(filename1,filename2,filename3):
    return static_file(filename3, root='./views/FlatUI/'+'/'+filename1+'/'+filename2)

@route('/FlatUI/<filename1>/<filename2>/<filename3>/<filename4>')
def server_static(filename1,filename2,filename3,filename4):
    return static_file(filename4, root='./views/FlatUI/'+filename1+'/'+filename2+'/'+filename3+'/')

@route('/assets/<filename1>/<filename2>')
def server_static(filename1,filename2):
    return static_file(filename2, root='./views/assets/'+'/'+filename1)

@route('/assets/<filename1>/<filename2>/<filename3>')
def server_static(filename1,filename2,filename3):
    return static_file(filename3, root='./views/assets/'+'/'+filename1+'/'+filename2)

@route('/assets/<filename1>/<filename2>/<filename3>/<filename4>')
def server_static(filename1,filename2,filename3,filename4):
    return static_file(filename4, root='./views/assets/'+filename1+'/'+filename2+'/'+filename3+'/')
    
@route('/survey/FlatUI/<filename1>/<filename2>')
def server_static(filename1,filename2):
    return static_file(filename2, root='./views/FlatUI/'+'/'+filename1)
@route('/survey/FlatUI/<filename1>/<filename2>/<filename3>')
def server_static(filename1,filename2,filename3):
    return static_file(filename3, root='./views/FlatUI/'+'/'+filename1+'/'+filename2)

@route('/survey/FlatUI/<filename1>/<filename2>/<filename3>/<filename4>')
def server_static(filename1,filename2,filename3,filename4):
    return static_file(filename4, root='./views/FlatUI/'+filename1+'/'+filename2+'/'+filename3+'/')
@post('/survey/:name')
def survey_req(name):
    global DBaddress
    id=0
    con=mdb.connect(DBaddress,'root','chendi1995','Movie_Recommend',charset='utf8')
    cur=con.cursor()
    cur.execute('set names utf8')
    cur.execute('SELECT * FROM movie')
    results=cur.fetchall()
    for row in results:
        score=request.forms.get(str(id))
        id=id+1
        if  score!=None and score.strip():
            cur.execute("INSERT INTO favorite VALUES ('%s','%s',%f)"%(name,row[0],float(score)))
            con.commit()
            print 'insert successfully!' 
    con.close()
    return '<META HTTP-EQUIV="Refresh" CONTENT="3;URL=http://localhost:8080/recommend/%s "><p>系统正在飞速计算中。。。请耐心等等。。。</p>'%name

#皮尔逊相关度
def sim_pearson(prefs,p1,p2):
    si={}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item]=1
    n= len(si)
    if n==0:
        return -1
    sum1=sum([prefs[p1][it] for it in si])
    sum2=sum([prefs[p2][it] for it in si])

    sum1Sq=sum([pow(prefs[p1][it],2) for it in si])
    sum2Sq=sum([pow(prefs[p2][it],2) for it in si])

    pSum=sum(prefs[p1][it] * prefs[p2][it] for it in si)
    num = pSum - (sum1*sum2/n)
    den = sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
    if den == 0:
        return 0
    r = num /den
    return r
#根据皮尔逊相关度算出推荐列表
def getRecommendations(prefs,person):
    totals={}
    simSums={}
    for other in prefs:
        if other == person: continue
        sim=sim_pearson(prefs,person,other)
        if sim==0:
            continue
        for item in prefs[other]:
            if item not in prefs[person] or prefs[person][item]==0:
                totals.setdefault(item,0)
                totals[item]+=prefs[other][item]*sim
                simSums.setdefault(item,0)
                simSums[item]+=sim
    rankings=[(total/simSums[item],item) for item,total in totals.items()]
    rankings.sort()
    rankings.reverse()
    return rankings
    
@route('/recommend/:name')
def recommend(name):
    global DBaddreess
    con=mdb.connect(DBaddress,'root','chendi1995','Movie_Recommend',charset='utf8')
    cur=con.cursor()
    cur.execute('set names utf8')
    cur.execute('SELECT * FROM favorite')
    results=cur.fetchall()
    #构造偏好集
    critics={}
    for row in results:
        critics.setdefault(row[0],{})
        critics[row[0]][row[1]]=float(row[2])
    #print critics
    rank=getRecommendations(critics,name)
    con.close()
    if len(rank)==0:
        return '<META HTTP-EQUIV="Refresh" CONTENT="1;URL=/login "><p>很抱歉，当前用户群太少，无法给出准确的建议，请号召周围的小伙伴都来试试吧！</p>'
    movie="["
    score=[]
    for row in rank:
        movie=movie+"\'"+row[1]+"\'"+","
        score.append(int(row[0]))
    movie=movie+"]"
    print movie
    #str_movie = str(movie).replace('u\'','\'')  
    #str_movie.decode("unicode-escape")  
    #str_score = str(score).replace('u\'','\'')  
    #str_score.decode("unicode-escape")
    #print str_movie
    #print rank
    return template('test',movie=movie,score=score)
'''
@route('/test')
def test():
    msg=['Africa', 'America', 'Asia', 'Europe', 'Oceania']
    return template('test',msg=str(msg))
'''
run(host='localhost',port=8080)
