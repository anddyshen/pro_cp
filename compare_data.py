import datetime
import pymysql


def rewards_rule(rewards_ball,my_ball):
    match_red = 0
    match_blue = 0
    rewards_level = 0
    for i in range(0,len(my_ball)):
        for j in range(1,9):
            if my_ball[0][i] == rewards_ball[j]
                match_red += 1
        if my_ball[1][0] == rewards_ball[9]
            match_blue = 1

    if match_red <= 2 and match_blue == 1:
        rewards_level = 6
    if match_red == 3 and match_blue == 1:
        rewards_level = 5
    if match_red == 4 and match_blue == 0:
        rewards_level = 5
    if match_red == 4 and match_blue == 1:
        rewards_level = 4
    if match_red == 5 and match_blue == 0:
        rewards_level = 4
    if match_red == 5 and match_blue == 1:
        rewards_level = 3
    if match_red == 6 and match_blue == 0:
        rewards_level = 2
    if match_red == 6 and match_blue == 1:
        rewards_level = 1

    return rewards_level


my_ball_list_ex0 = [['06', '20', '26', '17', '33', '12'], ['08']]
my_ball_list_ex1 = [['02', '06' ,'15','28'],['10']]
my_ball_list_ex2 = [['12', '23', '06'], ['']]
rewards_ball = [['2019110', '01', '18', '22', '26', '27', '28', '08'], ['2019109', '03', '06', '07', '17', '28', '31', '10'], ['2019108', '07', '13', '19', '22', '25', '32', '13']]

conn = pymysql.connect(host='127.0.0.1', user='root', password='abcd', database='cp', charset='utf8')
cur = conn.cursor()


try:
    sql = 'SELECT count(kjqh) FROM ball_history '
    cur.execute(sql)
    conn.commit()
    result0 = cur.fetchone()
    print(f"数据库共有 {result0[0]} 条数据\n\n")

except Exception as e:
    print(e)
    print(f"读取数据库失败\n\n")
    conn.rollback()
finally:
    cur.close()
    conn.close()



conn = pymysql.connect(host='127.0.0.1', user='root', password='abcd', database='cp', charset='utf8')
cur = conn.cursor()
c_qty = int(input(f"你想对比此前多少期的数据 (< {result0[0]}) :>>"))

try:
    sql = 'SELECT * FROM ball_history ORDER BY kjqh DESC LIMIT '+ str(c_qty)
    cur.execute(sql)
    conn.commit()
    result1 = cur.fetchall()

    """
    sql = 'SELECT * FROM ball_history ORDER BY kjqh DESC LIMIT 15'
    cur.execute(sql)
    conn.commit()
    result2 = cur.fetchmany(5)

    sql = 'SELECT * FROM ball_history ORDER BY kjqh DESC LIMIT 15'
    cur.execute(sql)
    conn.commit()
    result3 = cur.fetchall()
    """ #

    print(f"读取了所有确认的期号号码的所有数据 {result1}\n\n")
    print(f"读取了所有确认的期号号码的第{c_qty}条数据 {result1[c_qty - 1]}\n\n")

except Exception as e:
    print(e)
    print(f"读取数据库失败\n\n")
    conn.rollback()
finally:
    cur.close()
    conn.close() 

#号码对比正式开始
num_his_tmp = []

for i in range(0,c_qty):
    tmp = result1[i]
    tmp_list = []
    for j in range(0,len(tmp)):
        if tmp[j] != None:
            tmp_list.append(tmp[j])
    num_his_tmp.append(tmp_list)

print(f"希望对比的奖期列表: {num_his_tmp}")

"""
x = 0
for i in range(0,len(num_his_tmp)):#所有期数
    for j in range(0,len(my_ball_list_ex0)):#自选待对比号码
        for k in range(1,9): #当前奖期的中奖号码
            rewards_b = num_his_tmp[i]
            if my_ball_list_ex0[j] == rewards_b[k]:
                x += 1
            else:
                pass
"""