import datetime
import pymysql


conn = pymysql.connect(host='127.0.0.1', user='root', password='abcd', database='cp', charset='utf8')
cur = conn.cursor()

try:
    sql = "SELECT * FROM ball_history ORDER BY kjqh DESC LIMIT 1"
    cur.execute(sql)
    conn.commit()
    result0 = cur.fetchall()
    print(f" {result0} \n\n")

except Exception as e:
    print(e)
    print(f"读取数据库失败\n\n")
    conn.rollback()
finally:
    cur.close()
    conn.close()
