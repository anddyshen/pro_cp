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

ball_rpt= input(f"请问需要查找红球连续出现几次（<=6）：")
if int(ball_rpt) > 6:
    ball_rpt= input(f"请问需要查找红球连续出现几次（<=6）：")
c_qty_input = input(f"请问需要在之前的多少期内查找：")

try:
    sql = 'SELECT * FROM ball_history ORDER BY kjqh DESC LIMIT '+ str(c_qty_input)
    cur.execute(sql)
    conn.commit()
    result0 = cur.fetchall()
    #print(result0)
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
    for i in range(1,6):
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
       
print(rpt_array)

if int(ball_rpt) > 2:
    for k in range(0,len(rpt_array)):
        if len(rpt_array[k]) - 1 == int(ball_rpt):
            rpt_array_sum.append(rpt_array[k])
            ball_rpt_sum += 1
else:
    for k in range(1,len(rpt_array)):
        if rpt_array[k-1][0] == rpt_array[k][0] and len(rpt_array[k]) == 3 :
            rpt_array_s = rpt_array[k-1] + rpt_array[k] 
            rpt_array_s.pop(3)
            rpt_array_sum.append(rpt_array_s)
            a += 1
        else:
            if len(rpt_array[k]) == 3 :
               rpt_array_t2.append(rpt_array[k])
        #rpt_array_sum.append(rpt_array_t2)
        ball_rpt_sum += 1    

    for k in range(0,len(rpt_array_sum)):
        for p in range(0,len(rpt_array_t2)):
            if rpt_array_sum[k][0] == rpt_array_t2[p][0]:
                rpt_array_t2[p] = rpt_array_sum[k]

if ball_rpt_sum == 0:
    print("在指定的开奖期内，没有出现连续出球的情况！")
else:
    print(f"摇出 {ball_rpt} 个连续的红球号码的情况共出现了 {ball_rpt_sum} 次，分别是 \n{rpt_array_sum} \n\n")
    if int(ball_rpt) == 2:
        print(f"其中有 {a} 个 两次2个连续红球的情况，具体是 {rpt_array_sum}")

# reds = []
# blues = []
# for i in selector.xpath('//tr[@class="t_tr1"]'):
#     datetime = i.xpath('td/text()')[0]
#     red = i.xpath('td/text()')[1:7]
#     blue = i.xpath('td/text()')[7]
#     for i in red:
#         reds.append(i)
#     blues.append(blue)

# s_blues = Series(blues)
# s_blues = s_blues.value_counts()
# s_reds = Series(reds)
# s_reds = s_reds.value_counts()
# print(s_blues)
# print(s_reds)

# labels = s_blues.index.tolist()
# sizes = s_blues.values.tolist()
# rect = plt.bar(range(len(sizes)) , sizes , tick_label = labels)
# plt.show()



endtime = datetime.datetime.now()
total_times = (endtime - starttime).seconds 
print(f"本次执行共耗时： {total_times} 秒")  