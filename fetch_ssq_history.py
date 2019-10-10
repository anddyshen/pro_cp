# -*- coding:utf-8 -*-

#from sys import argv
#import sqlite3
import requests
import datetime
import pymysql
from lxml import etree

starttime = datetime.datetime.now()

def write_txt():
    f1 = open('ssq.txt','w')
    f1.truncate()
    print(f"每次测试前写入文件清空，成功\n\n")
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

#conn = sqlite3.connect(r"./db/ssq.db")#sqlite语句
#conn = sqlite3.connect(r"C:\mypyfiles\projects\more_ex\pro_ssq\db\ssq.db")
#conn = sqlite3.connect(r"C:\Users\Anddy\Documents\GitHub\MyPyFiles\Projects\more_ex\pro_ssq\db\ssq.db")
conn = pymysql.connect(host='127.0.0.1', user='root', password='abcd', database='cp', charset='utf8')
cur = conn.cursor()




def db_reset():#测试时用于清空删除全部库后重置
    try: 
        sql = 'delete from rewards_history'
        sql2 = 'delete from ball_history'
        sql3 = 'delete from ball_detail'
        cur.execute(sql)
        cur.execute(sql2)
        cur.execute(sql3)
        conn.commit()
        print(f"测试前数据库重置清空，成功\n\n")
    except Exception as e:
        print(e)
        print(f"数据库清空失败\n\n")
        conn.rollback()
    finally:
        cur.close()
        conn.close()
    


try: #每次对比数据库最新数据
    sql = 'SELECT count(kjqh) FROM ball_history ' #数据库内记录总数
    sql2 = "SELECT * FROM ball_history ORDER BY kjqh DESC LIMIT 1"#数据库内最新一期期数
    cur.execute(sql0)
    conn.commit()
    result0 = cur.fetchone()
    cur.execute(sql2)
    conn.commit()
    result1 = cur.fetchall()
    result1 = result1[0][1]

    print(f"对比奖期前数据库操作，成功\n\n")
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
    row_list = [] #取回后的所有元素，以一维列表形式存储
    for tr in tr_list:
        row_list.append(str(tr.text))  
    
    #将红篮球组成一组二维数组
    ball_row_list = []
    for tr_ball in tr_ball_list:
        ball_row_list.append(str(tr_ball.text)) 
        total_ball = len(ball_row_list)
       
    ball_temp_list = []
    ball_list = [] #当前页下的所有中奖号码的二维列表，以红球（字符串）+篮球位形式，准备写入相同结构的数据库
    ball_detail_temp = []
    ball_detail = [] #当前页下以每一期为结果，开奖期与所有球号码为元素的临时列表
    ball_detail_f = [] #当前页下以开奖期与所有球号码为元素的一维列表，准备写入相同结构的数据库表
    ball_t_temp = []
    ball_t = [] #中奖号码的以 中奖期号+33红+16蓝 为形式的二维列表，准备写入相同结构的数据库表

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
            sql = 'INSERT INTO rewards_history(xiang,kjqh,kjrq,kjhmhq,kjhmlq,yizs,yijj,erzs,erjj,sanzs,sanjj,sizs,sijj,wuzs,wujj,liuzs,liujj,xse,jc,gg) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            cur.execute(sql,db_row)
            sql1 = 'INSERT INTO ball_history(kjqh,r1,r2,r3,r4,r5,r6,b1) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)'
            cur1.execute(sql1, db_ball_f)
            sql2 = 'INSERT INTO ball_detail(kjqh,r1,r2,r3,r4,r5,r6,r7,r8,r9,r10,r11,r12,r13,r14,r15,r16,r17,r18,r19,r20,r21,r22,r23,r24,r25,r26,r27,r28,r29,r30,r31,r32,r33,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
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
     
    #与当前页最新一条比较，如果相同则退出，如记录> 1，取最大几条写入数据库，
    #如>30本页全部写入数据库后跳出，并前往下一页继续.如相差 ==1则前往官网抓取调取记录，返回值为0时，停止。
    def compare_lastest_record():
        if x - k == 1:
            result1 - r = xxx
            print("已经将最新的{x}条开奖结果记入数据库")
        else:
            print("当前已经是最新的数据，无需更新")



    print(f"完成抓取第{i}页，并写入\n")
    if i % 100 == 0:#隔几页停顿一次，>84为无需停顿
        input("按回车键继续\n")

endtime = datetime.datetime.now()
total_times = (endtime - starttime).seconds 
print(f"本次执行共耗时： {total_times} 秒")  