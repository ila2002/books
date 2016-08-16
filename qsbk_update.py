
#coding:utf-8
import requests,time,datetime,MySQLdb
from lxml import etree
header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
datetime1=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
datetime2=datetime.datetime.strptime(datetime1,'%Y-%m-%d %H:%M:%S')
conn=MySQLdb.connect(host="127.0.0.1",user="root",passwd="",db="books",charset="utf8")
cursor=conn.cursor()
for i in range(1,6):
    site="http://www.qiushibaike.com/text/page/"+str(i)
    r=requests.get(site,headers=header)
    print r.encoding
    root=etree.HTML(r.text)
    joks=root.xpath("//div[@class='content-block clearfix']/div[@id='content-left']/div[@class='article block untagged mb15']")
    num=len(joks)
    print num
    for i in range(1,num+1):
      author0=root.xpath("//div[@class='content-block clearfix']/div[@id='content-left']/div[@class='article block untagged mb15']["+str(i)+"]/div[1]/a[2]")
      if author0:
        author=author0[0].get("title").replace("'","`")
      else:
        author=u"匿名用户"
      #print author
      
      contents0=root.xpath("//div[@class='content-block clearfix']/div[@id='content-left']/div[@class='article block untagged mb15']["+str(i)+"]/div[2]")[0].xpath('string(.)')
      contents=contents0.replace("\n\n","").replace("\n","<br>").replace("'","`")
      #上句把“'符号过滤掉
      #print contents
      
      funny0=root.xpath("//div[@class='content-block clearfix']/div[@id='content-left']/div[@class='article block untagged mb15']["+str(i)+"]/div[3]/span[1]/i")
      funny=funny0[0].text.encode('gb18030',"ignore") 
      #print funny
      
      reply0=root.xpath("//div[@class='content-block clearfix']/div[@id='content-left']/div[@class='article block untagged mb15']["+str(i)+"]/div[3]/span[2]/a/i")
      if reply0:
        reply=reply0[0].text.encode('gb18030',"ignore") 
      else:
        reply="0"
      #print reply

      link0=root.xpath("//div[@class='content-block clearfix']/div[@id='content-left']/div[@class='article block untagged mb15']["+str(i)+"]/div[4]/ul/li[3]/a")
      link="http://www.qiushibaike.com"+link0[0].get("href").encode('gb18030',"ignore") 
      #print link

      print "**************************************************"
      sql1="select content from qsbk where link='%s'"%(link)
      cursor.execute(sql1)
      alldata=cursor.fetchall()
      if alldata:
          pass
      else:
        sql2="insert into qsbk(link,author,content,funny,reply,gettime) values('%s','%s','%s','%s','%s','%s')"\
            %(link,author,contents,int(funny),int(reply),datetime1)
        try:
            cursor.execute(sql2)
            conn.commit()
        except Exception,e:
            print Exception,":",e
cursor.close()
conn.close()
