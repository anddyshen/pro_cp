import requests
from lxml import etree
#import matplotlib.pyplot as plt
from pandas import Series
import pymysql
import datetime

starttime = datetime.datetime.now()
# url = "http://datachart.500.com/ssq/history/newinc/history.php?start=18081&end=19116"
# response = requests.get(url)
# response = response.text
# selector = etree.HTML(response)


def load_data():

    conn = pymysql.connect(host='127.0.0.1', user='root', password='abcd', database='cp', charset='utf8')
    cur = conn.cursor()

    try:
        #sql = 'SELECT * FROM ball_history ORDER BY kjqh DESC LIMIT '+ str(c_qty_input)
        #sql1 = 'SELECT kjqh,r1,r2,r3,r4,r5,r6,b1 FROM ball_history ORDER BY kjqh DESC LIMIT '+ str(c_qty_input)
        sql1 = 'SELECT kjqh,r1,r2,r3,r4,r5,r6,b1 FROM ball_history ORDER BY kjqh DESC '
        cur.execute(sql1)
        conn.commit()
        sql_result0 = cur.fetchall()
        #print(result0)
    except Exception as e:
        print(e)
        print(f"读取数据库失败\n\n")
        conn.rollback()
    finally:
        cur.close()
        conn.close()

    return sql_result0



def cal_ball_in_x():
    result0 = load_data()
    result_x = []
    rpt_array = []
    ball_rpt_sum = 0
    rpt_array_t = []
    rpt_array_s = []
    rpt_array_t2 = []
    rpt_array_s1 = []
    rpt_array_sum = []
    b2x2red = 0

    ball_rpt= input(f"请问需要查找红球连续出现几次（<=6）：")
    if int(ball_rpt) > 6 and int(ball_rpt) < 1 :
        ball_rpt = input(f"输入错误，请问需要查找红球连续出现几次（<=6）：")
    c_qty_input = input(f"请问需要在之前的多少期内查找：")
    starttime = datetime.datetime.now()



    for j in range(0,len(result0)):
        result_0 = list(result0[j])
        result_x.append(result_0)

    for j in range(0,int(c_qty_input)):
        for i in range(1,6):
            if int(result_x[j][i+1]) - int(result_x[j][i]) == 1 :#如果相邻号码相差1，则为连续数，加入待整理临时数组
                if len(rpt_array_t) == 0:
                    rpt_array_t.append(result_x[j][0] + " 期 : ")
                    rpt_array_t.append(result_x[j][i])
                    rpt_array_t.append(result_x[j][i+1])         
                else:
                    rpt_array_t.append(result_x[j][i+1])
                if i == 5:#最后两位为连续号码的的话，需要强制添加至列表，并清空临时列表
                    rpt_array.append(rpt_array_t)
                    rpt_array_t = []
            else:#如果不是连续数字，原来列表数组清零，空列表传递给下一次使用
                if rpt_array_t != []:
                    rpt_array.append(rpt_array_t)
                rpt_array_t = []
        
    #print(rpt_array)

    if int(ball_rpt) > 2:#出现连续3次以上的算法
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
            else:
                if len(rpt_array[k]) == 3 :
                    rpt_array_t2.append(rpt_array[k])
            #rpt_array_sum.append(rpt_array_t2)
            ball_rpt_sum += 1    

        for k in range(0,len(rpt_array_sum)):
            for p in range(0,len(rpt_array_t2)):
                if rpt_array_sum[k][0] == rpt_array_t2[p][0]:
                    rpt_array_t2[p] = rpt_array_sum[k]
        
        for k in range(0,len(rpt_array_t2)):
            if len(rpt_array_t2[k]) == 5:
                rpt_array_s1.append(rpt_array_t2[k])
        b2x2red = len(rpt_array_s1)



    # 输出统计结果
    rate = ""#出现该现象在所选期数中的出现的概率
    rate = ball_rpt_sum / int(c_qty_input)
    rate = "%.2f%%" % (rate * 100)
    rate2 = b2x2red/ int(c_qty_input)
    rate2 = "%.2f%%" % (rate2 * 100)

    newest  = ""#最近该现象的期号
    Min_show = ''#所有结果中出现的最小期数间距
    Max_show = ''#所有结果中出现的最大期数间距




    a=""
    b=""

    if ball_rpt_sum == 0:
        print("\n 在指定的开奖期内，没有出现连续出球的情况！")
    else:
        if int(ball_rpt) == 2:
            print(f" \n 摇出 {ball_rpt} 个连续的红球号码的情况:在 {c_qty_input} 期中共出现了 {ball_rpt_sum} 次\n\n 出现几率是 {rate}")
            print(f"\n 其中有 {b2x2red} 个 两次连续2个红球的情况，出现几率是 {rate2} ，具体是: \n ")
            for i in range(0,(len(rpt_array_s1) // 2 +1)):
                if i*2 < len(rpt_array_s1):
                    a = rpt_array_s1[i*2]
                else:
                    break
                if (i*2 + 1) >= len(rpt_array_s1):
                    b = "数据结束"
                else:
                    b = rpt_array_s1[i*2 + 1]
                print(f"{a} --{i*2 +1} 项--第{i+1}行--{i*2+2} 项-- {b}")
        else:
            print(f" \n 摇出 {ball_rpt} 个连续的红球号码的情况:在 {c_qty_input} 期中共出现了 {ball_rpt_sum} 次\n\n 出现几率是 {rate}\n")
            for j in range(0,(len(rpt_array_sum) // 2 +1)):
                if j*2 < len(rpt_array_sum):
                    c = rpt_array_sum[j*2]
                else:
                    break
                if (j*2 + 1) >= len(rpt_array_sum):
                    d = "数据结束"
                else:
                    d = rpt_array_sum[j*2 + 1]
               
                print(f"{c} --{j*2+1} 项--第{j+1}行--{j*2+2} 项-- {d}")
       
    endtime = datetime.datetime.now()
    return rpt_array_sum


def count_num():
    reds = []
    blues = []
    resultx = []
    result1 = []
    starttime = datetime.datetime.now()
    result0 = load_data()
    for j in range(0,len(result0)):
        resultx = list(result0[j])
        result1.append(resultx)

    for i in range(0,len(result1)):
        red = result1[i][1:6]
        blue = result1[i][7]
        for i in red:
            reds.append(i)
        blues.append(blue)


    s_blues = Series(blues)
    s_blues = s_blues.value_counts()
    s_reds = Series(reds)
    s_reds = s_reds.value_counts()
    print(f"红球出现次数：{s_blues}")
    print(f"篮球出现次数：{s_reds}")

    # labels = s_blues.index.tolist()
    # sizes = s_blues.values.tolist()
    # rect = plt.bar(range(len(sizes)) , sizes , tick_label = labels)
    # plt.show()

    endtime = datetime.datetime.now()

    return s_reds,s_blues,rect


if __name__ == "__main__":

    cal_ball_in_x()
    ask_if_ctn = input("是否继续查找其他相关数据,quit退出，其他任意键继续 \n")
    if ask_if_ctn == "quit":
        pass
    else:
        cal_ball_in_x()
    
    ask_if_ctn = input("是否进行全部数字统计,quit退出，其他任意键继续 \n")
    if ask_if_ctn == "quit":
        exit()
    else:
        count_num()



endtime = datetime.datetime.now()
total_times = (endtime - starttime) #.seconds 
print(f"本次执行共耗时： {total_times} 秒")  