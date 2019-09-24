import datetime
import pymysql

my_ball_list_ex = [['02', '06' ,'15','28'],['10']]

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