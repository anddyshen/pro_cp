#from sys import argv
import requests
import sqlite3
import datetime
import pymysql
from lxml import etree

starttime = datetime.datetime.now()

f1 = open('ssq.txt','w')
f1.truncate()
print(f"每次测试前写入文件清空，成功\n\n")

#conn = sqlite3.connect(r"./db/ssq.db")
#conn = sqlite3.connect(r"C:\mypyfiles\projects\more_ex\pro_ssq\db\ssq.db")
#conn = sqlite3.connect(r"C:\Users\Anddy\Documents\GitHub\MyPyFiles\Projects\more_ex\pro_ssq\db\ssq.db")
conn = pymysql.connect(host='127.0.0.1', user='root', password='abcd', database='cp', charset='utf8')

cur = conn.cursor()
try:
    sql = 'delete from ball_history'
    sql2 = 'delete from ball_detail_history'
    sql3 = 'delete from ball_table'
    cur.execute(sql)
    cur.execute(sql2)
    cur.execute(sql3)
    conn.commit()
    print(f"每次测试前数据库清空，成功\n\n")
except Exception as e:
    print(e)
    print(f"数据库清空失败\n\n")
    conn.rollback()
finally:
    cur.close()
    conn.close()


for i in range(1,84):
    #print(f"第{i}页页眉\n\n")
  
    response = requests.get(f"https://www.17500.cn/widget/_ssq/kjlist/p/{i}.html")
    res_html = etree.HTML(response.text)
    
    tr_list = res_html.xpath('//tbody/tr/td')
    tr_ball_list = res_html.xpath('//tbody/tr/td/font')
    
    #列出取得所有除号码外的所有数据组成一个最大的一维数组
    row_list = []
    for tr in tr_list:
        row_list.append(str(tr.text))  
    
    #将红篮球组成一组二维数组
    ball_row_list = []
    for tr_ball in tr_ball_list:
        ball_row_list.append(str(tr_ball.text)) 
        total_ball = len(ball_row_list)
       
    ball_temp_list = []
    ball_list = []
    ball_detail_temp = []
    ball_detail = []
    ball_detail_f = []
    ball_t_temp = []
    ball_t = []

    for b in range(0, len(ball_row_list), 2):
        for c in range(0,2):
            if (b + c) % 2 == 0:
                ball_temp_list.append(ball_row_list[b + c])
                ball_detail = ball_row_list[b + c]
                ball_detail = ball_detail.replace(" ",",")
                ball_detail = ball_detail.split(",")

            else:
                ball_temp_list.append(ball_row_list[b + c])
       
        for d in range(0,2):
            if (b + d) % 2 == 1:
                ball_detail_temp.append(ball_row_list[b + d])

        ball_detail = ball_detail + ball_detail_temp
        
        #"""
        #把结果写入完整纵横二维表内
        u = 0
        for z in range(0,33):
            if int(ball_detail[u]) != (z+1):
                ball_t_temp.append("")
            else:
                ball_t_temp.append(str(z+1))
                u += 1  

        u = 6       
        for z in range(0,16):
            if int(ball_detail[u]) != (z+1):
                ball_t_temp.append("")
            else:
                ball_t_temp.append(str(z+1)) 
        


        ball_list.append(ball_temp_list)
        ball_detail_f.append(ball_detail)
        ball_t.append(ball_t_temp)
        ball_t_temp =[]
        #ball_t = ball_t_temp
        ball_temp_list = []
        ball_detail_temp = []
    #print(f"红篮球号码二维数组：{ball_list} \n\n")

    
    
    rows = len(row_list) / 19
    total_elements = len(row_list) # + 1 - 19

    #准备将号码按顺序以列表元素形式填入所有详细详细列表
    x = 0
    for r in range(3, total_elements, 19):
        row_list[r] = ball_row_list[x]
        x += 2

    x = -1
    y = 0
    for r in range(4, total_elements, 19):
        row_list.insert((r + y), ball_row_list[x + 2])
        x += 2
        y += 1
            
    
    #print(f"取回的完整的详细信息20位一维数组（缺红球）：{row_list} \n\n")

    print(f"本页总共有：{len(row_list)}个元素\n\n")
    print(f"本页总共有：{rows}行\n\n")

    #row_list 为一组以1位步长为单位的排序列表，以下算法将row_list中的元素排列成每19个元素为一个一维列表的二维列表
    row_split = []
    row_all = []
    total_elements = len(row_list)
    for p in range(0, total_elements, 20):
        for t in range(0,20):
            row_temp = row_list[p+t]
            row_split.append(str(row_temp)) 


        row_all.append(str(row_split))
        row_split = []

    #print(f"第{i}页详细信息二维数组内容：{row_all} \n\n")
    #print(f"准备将详细信息写入数据库>>> \n\n")

    #row_all 为字符串形式，用eval改为列表形式
    db_row = []
    db_ball_t = []
    #ball_row_list = []
    for k in range(len(row_all)):
        db_row = eval(row_all[k])
        db_ball_f = ball_detail_f[k]
        db_ball_t = ball_t[k]
        db_kjqh = db_row[1]
        db_ball_f.insert(0,db_kjqh) 
        db_ball_t.insert(0,db_kjqh)

        if ((i-1)*30+k+1) % 60 == 0:
            print(f"第{(i-1)*30+k+1}条内容，正添加至数据库 \n\n")# {db_row} \n\n")
        #conn = sqlite3.connect(r"./db/ssq.db")
        #conn = sqlite3.connect(r"C:\mypyfiles\projects\more_ex\pro_ssq\db\ssq.db")
        #conn = sqlite3.connect(r"C:\Users\Anddy\Documents\GitHub\MyPyFiles\Projects\more_ex\pro_ssq\db\ssq.db")
        #conn = pymysql.connect(host='127.0.0.1', user='root', password='abcd', database='cp', port='3306',charset='utf8')
        conn = pymysql.connect(host='127.0.0.1', user='root', password='abcd', database='cp', charset='utf8')
        cur = conn.cursor()
        cur1 = conn.cursor()
        cur2 = conn.cursor()

        try:
            sql = 'INSERT INTO ball_history(xiang,kjqh,kjrq,kjhmhq,kjhmlq,yizs,yijj,erzs,erjj,sanzs,sanjj,sizs,sijj,wuzs,wujj,liuzs,liujj,xse,jc,gg) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            cur.execute(sql,db_row)
            sql1 = 'INSERT INTO ball_detail_history(kjqh,r1,r2,r3,r4,r5,r6,b1) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'
            cur1.execute(sql1, db_ball_f)
            sql2 = 'INSERT INTO ball_table(kjqh,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15,r16,r17,r18,r19,r20,r21,r22,r23,r24,r25,r26,r27,r28,r29,r30,r31,r32,r33,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            cur2.execute(sql2, db_ball_t)
            conn.commit()
            if ((i-1)*30+k+1) % 50 == 0:
                print(f"第{(i-1)*30+k+1}条详细信息插入成功\n\n")               
        except Exception as e:
            print(e)
            print(f"第{(i-1)*30+k+1}条详细信息插入失败\n\n")
            conn.rollback()
        finally:
            cur.close()
            conn.close()
     
        try:
            f1 = open('ssq.txt','a',encoding='utf-8')
            db_row_str = " | ".join(db_row)
            f1.writelines(db_row_str)
            f1.writelines("\n")
        except FileExistsError as ex:
                print(ex)
                print('文件不存在')
        finally:
                f1.close()   


    print(f"完成第{i}页\n")
    if i % 85 == 0:
        input("按回车键继续\n")

endtime = datetime.datetime.now()
total_times = (endtime - starttime).seconds 
print(f"本次执行共耗时： {total_times} 秒")  