# -*- coding:utf-8 -*-

import datetime
import pymysql

class LoadSsqEngine(object):
    
    def __init__(self):
        self.LoadSsqEngine = ""


    def load_history(self):

        conn = pymysql.connect(host='127.0.0.1', user='root', password='abcd', database='cp', charset='utf8')
        cur = conn.cursor()

        try:
            sql = 'SELECT count(kjqh) FROM ball_history '
            sql2 = "SELECT * FROM ball_history ORDER BY kjqh DESC LIMIT 1"
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

        try:
            sql2 = "SELECT * FROM ball_history ORDER BY kjqh DESC LIMIT 1"
            cur.execute(sql2)
            conn.commit()
            result2 = cur.fetchall()
            
        except Exception as e:
            print(e)
            print(f"读取数据库失败\n\n")
            conn.rollback()
        finally:
            cur.close()
            conn.close()


        conn = pymysql.connect(host='127.0.0.1', user='root', password='abcd', database='cp', charset='utf8')
        cur = conn.cursor()
        c_qty = int(input(f"最新一期为 {result2[0][1]} 期，共 {result0[0]} 条记录，你想对比之前多少期的数据 :>>"))

        if c_qty > result0[0]:
            print(f"数据库内共有 {result0[0]} 条记录，您输入{c_qty}已超出上限，按最大记录进行搜索对比")
            c_qty =result0[0]
        
        try:
            sql = 'SELECT * FROM ball_history ORDER BY kjqh DESC LIMIT '+ str(c_qty)
            cur.execute(sql)
            conn.commit()
            result1 = cur.fetchall()

    
            print(f"读取了所有确认的期号号码的第{c_qty}条数据\n\n")

        except Exception as e:
            print(e)
            print(f"读取数据库失败\n\n")
            conn.rollback()
        finally:
            cur.close()
            conn.close() 

        num_his_tmp = []

        for i in range(0,c_qty):
            tmp = result1[i]
            tmp_list = []
            for j in range(0,len(tmp)):
                if tmp[j] != None:
                    tmp_list.append(tmp[j])
            num_his_tmp.append(tmp_list)

        print(f"第 {result2[0][1]} 期之前 {c_qty}  期开奖号码列表: {num_his_tmp} \n\n")

        return num_his_tmp

if __name__ == "__main__":
    load_ssq = LoadSsqEngine()
    load_ssq.load_history()