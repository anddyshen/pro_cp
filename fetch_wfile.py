#from sys import argv
import requests
import sqlite3
from lxml import etree

conn = sqlite3.connect(r"C:\mypyfiles\projects\more_ex\pro_ssq\db\ssq.db")

cu = conn.cursor()



#input("请输入文件名：>>")
f1 = open('ssq.txt','w')
f1.truncate()

for i in range(1,4):
    print(f"第{i}页页眉")

    try:
        f1 = open('ssq.txt','a',encoding='utf-8')
        f1.writelines(f"第{i}页页眉")
        f1.writelines("\n")
    except FileExistsError as ex:
        print('文件不存在')
    finally:
        f1.close()


    response = requests.get(f"https://www.17500.cn/widget/_ssq/kjlist/p/{i}.html")
    res_html = etree.HTML(response.text)
    
    tr_list = res_html.xpath('//tbody/tr/td')
    #tr_ball = res_html.xpath('//tbody/tr/td/font')
    for tr in tr_list:
        print(str(tr.text))
             
        try:
            f1 = open('ssq.txt','a',encoding='utf-8')
            f1.writelines(str(tr.text))
            f1.writelines("\n")
        except FileExistsError as ex:
                print('文件不存在')
        finally:
                f1.close()
       

        #input("按回车键继续")
    print(f"第{i}页页尾")
 
    try:
        f1=open('ssq.txt','a',encoding='utf-8')
        f1.writelines(f"第{i}页页尾")
        f1.writelines("\n")
    except FileExistsError as ex:
        print('文件不存在')
    finally:
        f1.close()
 
 


sql = 'INSERT INTO ball_history(xiang,kjqh,kjrq,kjhm,yizs,yijj,erzs,erjj,sanzs,sanjj,sizs,sijj,wuzs,wujj,liuzs,liujj,xse,jc,gg) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'