import requests
from lxml import etree
import matplotlib.pyplot as plt
from pandas import Series
import pymysql
import datetime

starttime = datetime.datetime.now()
# url = "http://datachart.500.com/ssq/history/newinc/history.php?start=18081&end=19116"
# response = requests.get(url)
# response = response.text
# selector = etree.HTML(response)

conn = pymysql.connect(host='127.0.0.1', user='root', password='abcd', database='cp', charset='utf8')
cur = conn.cursor()

#ball_rpt= input(f"请问需要查找红球连续出现几次（<=6）：")
ball_rpt= 4
if int(ball_rpt) > 6:
    ball_rpt= input(f"请问需要查找红球连续出现几次（<=6）：")
#c_qty_input = input(f"请问需要在之前的多少期内查找：") 
c_qty_input = 10

try:
    sql = 'SELECT * FROM ball_history where kjqh <= 2018111  ORDER BY kjqh DESC LIMIT '+ str(c_qty_input)
    cur.execute(sql)
    conn.commit()
    result0 = cur.fetchall()
    print(f"数据库读取的 {c_qty_input} 条内容\n")
    print(result0)
    print(f"\n\n")
except Exception as e:
    print(e)
    print(f"读取数据库失败\n\n")
    conn.rollback()
finally:
    cur.close()
    conn.close()


rpt_array = []
ball_rpt_sum = 0
rpt_array_t = []
rpt_array_s = []
rpt_array_t2 = []
rpt_array_2bx2 = []
rpt_array_sum = []
a = 0
for j in range(0,int(c_qty_input)):
    print(f" 当前全部数据： {result0[j]} \n")
    for i in range(1,7):
        if int(result0[j][i*2+2]) - int(result0[j][i*2]) == 1 :#如果相邻号码相差1，则为连续数，加入待整理临时数组
            if len(rpt_array_t) == 0:
                rpt_array_t.append(result0[j][1] + " 期 : ")
                rpt_array_t.append(result0[j][i*2])
                rpt_array_t.append(result0[j][i*2+2])         
            else:
                rpt_array_t.append(result0[j][i*2 + 2])
        else:#如果不是连续数字，原来列表数组清零，空列表传递给下一次使用
            if rpt_array_t != []:
                rpt_array.append(rpt_array_t)
            rpt_array_t = []
    
    print(f" 当前数据： {rpt_array} \n")


print ("连续球 200期查找，结果：")       
print(rpt_array)
